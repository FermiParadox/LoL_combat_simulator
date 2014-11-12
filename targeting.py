class Targeting(object):

    def __init__(self,
                 active_buffs,
                 current_target=None,
                 targets_already_hit=None):

        self.current_target = current_target
        self.targets_already_hit = targets_already_hit
        self.active_buffs = active_buffs

    def switch_to_first_alive_enemy(self):
        """Modifies current_target to first alive enemy.
        """
        for tar in sorted(self.active_buffs):
                if (tar != 'player') and ('dead_buff' not in self.active_buffs[tar]):
                    self.current_target = tar
                    break

    def switch_target(self, effect_name):
        """
        Modifies current_target based on the effect's target and available targets (non dead).
        """

        tar_type = getattr(self, effect_name)()['target']

        # If the effect targets the player..
        if tar_type == 'player':
            #.. it sets current_target to 'player'.
            self.current_target = 'player'
        # Otherwise it sets it to the first alive enemy.
        else:
            self.switch_to_first_alive_enemy()

    def next_target(self, selected_champs):
        """
        Modifies current_target and increases targets_already_hit by 1,
        if there are available (and alive) enemy targets.

        If there are no valid targets, sets current_target to None.
        """

        while True:
            # Creates next target's name.
            next_tar_name = 'enemy_%s' % (int(self.current_target[6:]) + 1)

            # Checks if target exists.
            if next_tar_name not in selected_champs:

                self.current_target = None
                break

            # Checks if target is alive.
            elif 'dead' not in self.active_buffs[next_tar_name]:
                # Adds 1 to target number and creates the next target name.
                self.current_target = next_tar_name

                self.targets_already_hit += 1

                break

    def target_type(self, tar_name=None):
        """
        Returns 'enemy' or 'player' based on the current_target.

        Optional argument:
            If given, it checks its type.
        """
        if tar_name:
            tar = tar_name
        else:
            tar = self.current_target

        if tar != 'player':
            return 'enemy'
        else:
            return 'player'