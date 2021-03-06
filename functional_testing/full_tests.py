import palette
import user_instance_settings
import functional_testing.default_config as default_config
from palette import delimiter, fat_delimiter

import cProfile
import ast
import pstats
import pandas
# import memory_profiler
import multiprocessing
import sys
import subprocess
import pprint


def _combat_loop_instance(data_dct):
    """
    Creates a combat loop instance and returns it after the combat.

    :return:
    """
    user_instance = user_instance_settings.UserSession()
    combat_instance = user_instance.instance_after_combat(data_dct)
    return combat_instance


def _single_user_multiple_combats_instances_lst(repetitions):
    """
    Creates a user instance and then lots of combat instances so that module and class variables are reused.

    :param repetitions: (int)
    :return: (list) List of instances.
    """

    data = default_config.ALL_DATA
    combat_instances_lst = []
    user_instance = user_instance_settings.UserSession()

    for i in range(repetitions):
        combat_instance = user_instance.instance_after_combat(data)
        combat_instances_lst.append(combat_instance)

    return combat_instances_lst


# TODO: Check if it actually works.
def _multiprocessed_single_user_multiple_combats(repetitions):
    """
    Creates a user instance and then lots of combat instances so that module and class variables are reused.

    NOTE: Multiprocessing used.

    :param repetitions: (int)
    :return: (list) List of instances.
    """

    data = default_config.ALL_DATA
    processes_lst = []
    user_instance = user_instance_settings.UserSession()

    for i in range(repetitions):

        mc_target = user_instance.instance_after_combat
        mc_args = (data, )

        process = multiprocessing.Process(target=mc_target, args=mc_args)

        processes_lst.append(process)
        process.start()

    for i in processes_lst:
        i.join()


def _single_combat_multiple_users_instances_lst(repetitions):
    """
    Creates multiple user instances and then a single combat instance for each.

    :param repetitions: (int)
    :return: (list) List of instances.
    """
    data = default_config.ALL_DATA
    combat_instances_lst = []

    for i in range(repetitions):
        user_instance = user_instance_settings.UserSession()
        combat_instance = user_instance.instance_after_combat(data)
        combat_instances_lst.append(combat_instance)

    return combat_instances_lst


def test_run_time(repetitions, sort_by='tottime', count_of_shown_functions=5):
    """
    Tests run duration of program in two ways:
        -Single user and multiple combat instances.
        -Multiple users and a single combat instance for each.

    :param repetitions: (int)
    :return:
    """

    print(fat_delimiter(80))

    function_dcts = {'multiple users': _single_combat_multiple_users_instances_lst.__name__,
                     'multiple combats': _single_user_multiple_combats_instances_lst.__name__,
                     'multiple combats (MULTIPROCESSING)': _multiprocessed_single_user_multiple_combats.__name__}

    for instances_type, func in sorted(function_dcts.items()):

        print(delimiter(40))
        print('Reps: {}'.format(repetitions))
        print('Instances type: {}\n'.format(instances_type))
        executed_str = '{}({})'.format(func, repetitions)

        cProfile.run(executed_str, 'cprof_results', sort=sort_by)

        results_run = pstats.Stats('cprof_results').sort_stats(sort_by)
        results_run.strip_dirs().sort_stats(sort_by).print_stats(count_of_shown_functions)


class AllFunctionalTests(object):

    def __init__(self):
        # Used to ensure storage and comparison are separate runs.
        self.prohibit_storage_comparison = False

    @property
    def __data_deepcopy(self):
        return default_config.all_data_deepcopy()

    def __data_dct(self, given_dct):
        """
        Returns given dict or sets it equal to deepcopy if None.

        :param given_dct: (dict) (None)
        :return: (dict) Dict with initial combat instance setup.
        """
        if given_dct:
            pass
        else:
            given_dct = self.__data_deepcopy

        return given_dct

    @staticmethod
    def __set_all_initial_lvls_to(initial_lvls_val, given_data_dct):
        """
        Modifies given dict by setting all lvls to chosen value.

        :param initial_lvls_val: (int) 1-18
        :param given_data_dct:
        :return: (None)
        """

        for i in given_data_dct['champion_lvls_dct']:
            given_data_dct['champion_lvls_dct'][i] = initial_lvls_val

    def run_combat_without_showing_results(self, data_dct=None):
        data_dct = self.__data_dct(given_dct=data_dct)

        user_instance = user_instance_settings.UserSession()
        post_combat_instance = user_instance.instance_after_combat(input_dct=data_dct)

        return post_combat_instance

    # # MEMORY
    # # TODO: Check if below method actually works.
    # @memory_profiler.profile
    # def test_memory_usage(self, data_dct=None):
    #     return self.run_combat_without_showing_results(data_dct=data_dct)

    def run_combat_and_show_results(self, data_dct=None):

        data_dct = self.__data_dct(given_dct=data_dct)

        user_instance = user_instance_settings.UserSession()
        post_combat_instance = user_instance.create_instance_and_represent_results(input_dct=data_dct)

        return post_combat_instance

    def naked_combat_and_results(self, rotation_lst, all_champs_lvls):

        data_dct = self.__data_deepcopy
        data_dct['rotation_lst'] = rotation_lst
        data_dct['selected_runes'] = None
        data_dct['selected_masteries_dct'] = None
        data_dct['chosen_items_dct'] = {}
        self.__set_all_initial_lvls_to(initial_lvls_val=all_champs_lvls, given_data_dct=data_dct)

        post_combat_instance = self.run_combat_and_show_results(data_dct=data_dct)

        return post_combat_instance

    # CONSISTENCY
    # TODO: Create tests that switch between champions and check their consistency.

    @staticmethod
    def __different_object_results_count(combat_instances_lst, compared_object_name):
        """
        Runs multiple combat tests for a single user instance, and returns the count of different results.

        :param compared_object_name: (str) Object of the combat instances that is being compared,
            eg. 'combat_results', 'combat_history'
        :return: (int)
        """

        enumerated_histories_dct = {}

        first_combat_instance_data = getattr(combat_instances_lst[0], compared_object_name)
        different_histories_dct = {0: first_combat_instance_data}

        for num, combat_instance in enumerate(combat_instances_lst):

            examined_history_dct = getattr(combat_instance, compared_object_name)
            enumerated_histories_dct.update({num: examined_history_dct})

            # Checks if history is different that existing histories.
            for stored_history in different_histories_dct.values():

                if stored_history == examined_history_dct:
                    break

            # If loop hasn't found a match.
            else:
                different_histories_dct.update({num: examined_history_dct})

        # Total different histories
        return len(different_histories_dct)

    def different_combat_results_count(self, combat_instances_lst):
        return self.__different_object_results_count(combat_instances_lst=combat_instances_lst,
                                                     compared_object_name='combat_results')

    def different_combat_history_count(self, combat_instances_lst):
        return self.__different_object_results_count(combat_instances_lst=combat_instances_lst,
                                                     compared_object_name='combat_history')

    @staticmethod
    def __compared_tar_pre_or_post_combat_stats(combat_instances_lst, tar_name, str_pre_or_post_combat_stats):
        """
        Compares pre or post combat stats for given instances.

        Prints only stats that differ in instances.

        :param combat_instances_lst: (list)
        :param str_pre_or_post_combat_stats: 'pre_combat_stats' or 'post_combat_stats'
        :return: (DataFrame) or (None)
        """

        all_stats_names = set()

        # Inserts all possible stats in dict, since some instances might not have that stat.
        for combat_instance in combat_instances_lst:
            combat_results_dct = combat_instance.combat_results
            tar_pre_combat_stats_dct = combat_results_dct[tar_name][str_pre_or_post_combat_stats]

            all_stats_names |= set(tar_pre_combat_stats_dct.keys())

        diff_pre_combat_stats = {i: [] for i in all_stats_names}

        # Inserts stats' values for each instance.
        # Instances without the stat are stored as NaN.
        for combat_instance in combat_instances_lst:
            combat_results_dct = combat_instance.combat_results

            tar_pre_combat_stats_dct = combat_results_dct[tar_name][str_pre_or_post_combat_stats]

            for stat_name in diff_pre_combat_stats:
                if stat_name in tar_pre_combat_stats_dct:
                    diff_pre_combat_stats[stat_name].append(tar_pre_combat_stats_dct[stat_name])
                else:
                    diff_pre_combat_stats[stat_name].append(None)

        # Filters out stats that remain the same.
        for stat_name in sorted(diff_pre_combat_stats):
            stat_vals_lst = diff_pre_combat_stats[stat_name]
            first_val = stat_vals_lst[0]

            for stat_val in stat_vals_lst:
                if stat_val != first_val:
                    break
            # (If loop doesn't break, then all values are equal and there is no point in displaying them.)
            else:
                del diff_pre_combat_stats[stat_name]

        # If no differences are found, dataframe is empty.
        stats_df = pandas.DataFrame(diff_pre_combat_stats)
        if stats_df.empty is True:
            return None
        else:
            return stats_df.transpose()

    def compared_tar_pre_combat_stats(self, combat_instances_lst, tar_name):
        return self.__compared_tar_pre_or_post_combat_stats(combat_instances_lst=combat_instances_lst,
                                                            tar_name=tar_name,
                                                            str_pre_or_post_combat_stats='pre_combat_stats')

    def compared_tar_post_combat_stats(self, combat_instances_lst, tar_name):
        return self.__compared_tar_pre_or_post_combat_stats(combat_instances_lst=combat_instances_lst,
                                                            tar_name=tar_name,
                                                            str_pre_or_post_combat_stats='post_combat_stats')

    def compare_pre_and_post_combat_stats(self, combat_instances_lst):
        """
        Compares and prints pre and post combat stats for all targets.

        :return: (None)
        """

        print(palette.fat_delimiter(40))
        print('PRE and POST COMBAT STATS COMPARISON.')

        data_dct = self.__data_deepcopy

        for tar in data_dct['selected_champions_dct']:
            pre_combat_comparison = self.compared_tar_pre_combat_stats(combat_instances_lst=combat_instances_lst,
                                                                       tar_name=tar)
            post_combat_comparison = self.compared_tar_post_combat_stats(combat_instances_lst=combat_instances_lst,
                                                                         tar_name=tar)

            print('\nTarget: {}'.format(tar))
            for comparison in (pre_combat_comparison, post_combat_comparison):

                if comparison:
                    print(comparison)

            else:
                print('No differences.')

    def _display_differences(self, combat_instances_lst, instances_type_msg):
        """
        Compares given instances searching for any differences and displays them.

        :param combat_instances_lst: (list) List of instances
        :return: (None)
        """

        total_instances = len(combat_instances_lst)

        print(palette.fat_delimiter(80))
        print('{}. Comparing {} combat instances.'.format(instances_type_msg, total_instances))

        diff_combat_results = self.different_combat_results_count(combat_instances_lst=combat_instances_lst)
        diff_combat_histories = self.different_combat_history_count(combat_instances_lst=combat_instances_lst)

        # If more than a single (different) instance is found, it displays all data.
        if diff_combat_results > 1 or diff_combat_histories > 1:
            print('Different combat results: {}'.format(diff_combat_results))
            print('Different combat histories: {}'.format(diff_combat_histories))
            print(self.compare_pre_and_post_combat_stats(combat_instances_lst=combat_instances_lst))

        else:
            print('-No differences.')

    def display_single_user_multi_combats_differences(self, repetitions):
        instances_type_msg = 'SINGLE USER'
        instances_lst = _single_user_multiple_combats_instances_lst(repetitions=repetitions)
        self._display_differences(combat_instances_lst=instances_lst, instances_type_msg=instances_type_msg)

    def display_multi_users_differences(self, repetitions):
        instances_type_msg = 'MULTIPLE USERS'
        instances_lst = _single_combat_multiple_users_instances_lst(repetitions=repetitions)
        self._display_differences(combat_instances_lst=instances_lst, instances_type_msg=instances_type_msg)

    @staticmethod
    def _process_history_and_results():
        """
        Creates a new process and returns history and results from a combat.

        :return: (dict) Keys: 'history', 'results'
        """

        output_as_bytes = subprocess.check_output([sys.executable, 'process_creation_helper.py'])
        output_as_str = output_as_bytes.decode("utf-8")
        output_as_dct = ast.literal_eval(output_as_str)

        return output_as_dct

    def multiple_runs_output_comparison(self, repetitions):
        """
        Creates multiple processes (so that PYTHONHASHSEED changes)
        and compares combat output.

        :return: (None)
        """

        # Creates first instance that will be compared to all other instances.
        first_process_output_dct = self._process_history_and_results()
        first_history = first_process_output_dct['history']
        first_results = first_process_output_dct['results']

        print(fat_delimiter(80))
        print('MULTIPLE DIFFERENT RUNS. Comparing {} combat instances.'.format(repetitions))

        # Creates multiple instances and compares them to the first instance.
        for i in range(repetitions):
            print(i)
            process_output_dct = self._process_history_and_results()
            fresh_history = process_output_dct['history']
            fresh_results = process_output_dct['results']

            history_different = palette.compare_complex_object(obj_1=first_history, obj_2=fresh_history)
            results_different = palette.compare_complex_object(obj_1=first_results, obj_2=fresh_results)

            if history_different:
                pprint.pprint(first_history['player']['heals'], width=10**6)
                pprint.pprint(fresh_history['player']['heals'], width=10**6)

            if results_different:
                print(first_results)
                print(fresh_results)

            if history_different or results_different:

                break

        # If loop didn't end prematurely.
        else:
            print('-No differences.')


if __name__ == '__main__':
    if 1:
        inst = AllFunctionalTests().run_combat_and_show_results()

    if 0:
        inst = AllFunctionalTests().naked_combat_and_results(rotation_lst=['AA'], all_champs_lvls=1)

    # RUN DURATION
    if 0:
        test_run_time(repetitions=50, sort_by='tottime', count_of_shown_functions=20)

    # CONSISTENCY
    # Different instances
    if 0:
        reps = 10
        AllFunctionalTests().display_single_user_multi_combats_differences(repetitions=reps)
        AllFunctionalTests().display_multi_users_differences(repetitions=reps)
    # Different runs:
    if 0:
        reps = 10
        AllFunctionalTests().multiple_runs_output_comparison(repetitions=reps)

    # MEMORY
    if 0:
        inst = AllFunctionalTests().test_memory_usage()
