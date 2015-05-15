ABILITIES_ATTRIBUTES = {
    'buffs': {'e_dmg_red': {'stats': {'aoe_dmg_reduction': {'percent': {'stat_values': 0.25,
                                                                        'stat_mods': {}}
                                                            },
                                      'aa_dmg_reduction': {'percent': {'stat_values': 1.0,
                                                                       'stat_mods': {}}
                                                           }},
                            'duration': 2,
                            'max_stacks': 1,
                            'on_hit': None,
                            'prohibit_cd_start': None,
                            'target_type': 'player',
                            'dot': False},
              'inn_buff_0': {'stats': {'aoe_dmg_reduction': {'percent': {'stat_values': (0.04, 0.06, 0.08, 0.10, 0.12),
                                                                         'stat_mods': {}}},
                                       },
                             'duration': 2.5,
                             'max_stacks': 6,
                             'on_hit': None,
                             'prohibit_cd_start': None,
                             'target_type': 'player',
                             'dot': False},
              'e_stun': {'stats': None,
                         'duration': 1,
                         'max_stacks': 1,
                         'on_hit': None,
                         'prohibit_cd_start': None,
                         'target_type': 'enemy',
                         'dot': False},
              'r_dmg_red': {'stats': {'armor': {'additive': {'stat_mods': None,
                                                             'stat_values': (20.0,
                                                                             35.0,
                                                                             50.0)}},
                                      'mr': {'additive': {'stat_mods': {'ap': (0.3,)},
                                                          'stat_values': (20.0,
                                                                          35.0,
                                                                          50.0)}, }},
                            'duration': 8,
                            'max_stacks': 1,
                            'on_hit': None,
                            'prohibit_cd_start': None,
                            'target_type': 'player',
                            'dot': False},
              'r_n_hit_initiator': {'stats': None,
                                    'duration': 'permanent',
                                    'max_stacks': 1,
                                    'on_hit': {'cause_dmg': [],
                                               'apply_buff': ['r_hit_counter'],
                                               'reduce_cd': {},
                                               'remove_buff': []},
                                    'prohibit_cd_start': None,
                                    'target_type': 'player',
                                    'dot': False},
              'r_hit_counter': {'stats': None,
                                'duration': 5,
                                'max_stacks': 3,
                                'on_hit': None,
                                'prohibit_cd_start': None,
                                'target_type': 'player',
                                'dot': False},
              'w_buff_0': {'stats': None,
                           'duration': 7,
                           'max_stacks': 1,
                           'on_hit': None,
                           'prohibit_cd_start': 'w',
                           'target_type': 'player',
                           'dot': False}},
    'dmgs': {'e_dmg_0': {'delay': None,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'e',
                         'dmg_type': 'physical',
                         'dmg_values': (1.0, 1.0, 1.0, 1.0, 1.0),
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 5,
                         'mods': {'enemy': {}, 'player': {'bonus_ad': 0.5}},
                         'radius': 150,
                         'target_type': 'enemy',
                         'usual_max_targets': 2,
                         'resource_type': 'hp'},
             'q_dmg_0': {'delay': None,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'q',
                         'dmg_type': 'physical',
                         'dmg_values': (70.0, 110.0, 150.0, 190.0, 230.0),
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {},
                                  'player': {'ap': 0.6, 'bonus_ad': 1.0}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1,
                         'resource_type': 'hp'},
             'r_dmg_0': {'delay': None,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'r',
                         'dmg_type': 'magic',
                         'dmg_values': (100.0, 160.0, 220.0),
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {}, 'player': {'ap': 0.7}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1,
                         'resource_type': 'hp'},
             'w_dmg_0': {'delay': None,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'w',
                         'dmg_type': 'magic',
                         'dmg_values': (40.0, 75.0, 110.0, 145.0, 180.0),
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {}, 'player': {'ap': 0.6}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1,
                         'resource_type': 'hp'}},
    'general_attributes': {'e': {'base_cd': (16.0, 14.0, 12.0, 10.0, 8.0),
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'cost_category': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (70,
                                                                       75,
                                                                       80,
                                                                       85,
                                                                       90)}},
                                 'dashed_distance': None,
                                 'independent_cast': False,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'reduces_ability_cd': None,
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'inn': {},
                           'q': {'base_cd': (10.0, 9.0, 8.0, 7.0, 6.0),
                                 'cast_time': 0.25,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'cost_category': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (65,
                                                                       65,
                                                                       65,
                                                                       65,
                                                                       65)}},
                                 'dashed_distance': 600,
                                 'independent_cast': False,
                                 'move_while_casting': False,
                                 'range': (700, 700, 700, 700, 700),
                                 'reduces_ability_cd': None,
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'r': {'base_cd': (80.0, 80.0, 80.0),
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'cost_category': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (100,
                                                                       100,
                                                                       100)}},
                                 'dashed_distance': None,
                                 'independent_cast': False,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'reduces_ability_cd': None,
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'w': {'base_cd': (7.0, 6.0, 5.0, 4.0, 3.0),
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'cost_category': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (30,
                                                                       30,
                                                                       30,
                                                                       30,
                                                                       30)}},
                                 'dashed_distance': None,
                                 'independent_cast': False,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'reduces_ability_cd': None,
                                 'resets_aa': True,
                                 'toggled': False,
                                 'travel_time': 0}}
}

ABILITIES_EFFECTS = {
    'inn': {'enemy': {'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}},
            'player': {'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}}},
    'e': {'enemy': {'actives': {'buffs': [], 'dmg': [], 'remove_buff': []},
                    'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}},
          'player': {'actives': {'buffs': [],
                                 'cds_modified': {},
                                 'dmg': [],
                                 'remove_buff': []},
                     'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}}},
    'q': {'enemy': {'actives': {'buffs': [], 'dmg': [], 'remove_buff': []},
                    'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}},
          'player': {'actives': {'buffs': [],
                                 'cds_modified': {},
                                 'dmg': [],
                                 'remove_buff': []},
                     'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}}},
    'r': {'enemy': {'actives': {'buffs': [], 'dmg': [], 'remove_buff': []},
                    'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}},
          'player': {'actives': {'buffs': ['r_dmg_red'],
                                 'cds_modified': {},
                                 'dmg': [],
                                 'remove_buff': []},
                     'passives': {'buffs': ['r_n_hit_initiator'],
                                  'dmg': [],
                                  'remove_buff': []}}},
    'w': {'enemy': {'actives': {'buffs': [], 'dmg': [], 'remove_buff': []},
                    'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}},
          'player': {'actives': {'buffs': [],
                                 'cds_modified': {},
                                 'dmg': [],
                                 'remove_buff': []},
                     'passives': {'buffs': [], 'dmg': [], 'remove_buff': []}}}
}

ABILITIES_CONDITIONALS = {
    'q_apply_w_conditional': {'effects': {'apply_w_dmg': {'obj_name': 'q',
                                                          'lst_category': 'dmg',
                                                          'effect_type': 'ability_effect',
                                                          'mod_operation': 'append',
                                                          'names_lst': ['w_dmg_0'],
                                                          'tar_type': 'enemy'},
                                          'remove_w_buff': {'obj_name': 'q',
                                                            'lst_category': 'remove_buff',
                                                            'effect_type': 'ability_effect',
                                                            'mod_operation': 'append',
                                                            'names_lst': ['w_buff_0'],
                                                            'tar_type': 'player'}},
                              'triggers': {}},
    'r_nth_hit': {'effects': {'apply_r_dmg': {'obj_name': 'r_n_hit_initiator',
                                              'lst_category': 'apply_dmg',
                                              'effect_type': 'buff_on_hit',
                                              'mod_operation': 'append',
                                              'names_lst': ['r_dmg_0']},
                              'remove_r_counter_stacks': {'obj_name': 'r_n_hit_initiator',
                                                          'lst_category': 'remove_buff',
                                                          'effect_type': 'buff_on_hit',
                                                          'mod_operation': 'append',
                                                          'names_lst': ['r_hit_counter']}},
                  'triggers': {'nth_hit_trig': {'buff_name': 'r_hit_counter',
                                                'operator': '>=',
                                                'owner_type': 'player',
                                                'stacks': 2,
                                                'trigger_type': 'buff'}}}}

CHAMPION_EXTERNAL_VARIABLES = {
    'hits_dodged_during_e': 5}

DEFAULT_ACTIONS_PRIORITY = ('AA', 'r', 'e', 'w', 'q')


class ChampionAttributes(object):

    ABILITIES_ATTRIBUTES = ABILITIES_ATTRIBUTES
    ABILITIES_EFFECTS = ABILITIES_EFFECTS
    ABILITIES_CONDITIONALS = ABILITIES_CONDITIONALS
    DEFAULT_ACTIONS_PRIORITY = DEFAULT_ACTIONS_PRIORITY

    def __init__(self, external_vars_dct=CHAMPION_EXTERNAL_VARIABLES):
        for i in external_vars_dct:
            setattr(ChampionAttributes, i, external_vars_dct[i])

