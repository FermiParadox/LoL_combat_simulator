ABILITIES_ATTRIBUTES = {
    'buffs': {'e_dmg_red': {'affected_stats': {'placeholder_stat_1': 'placeholder'},
                            'duration': 2,
                            'max_stacks': 1,
                            'on_hit': {'add_dmg': ['placeholder'],
                                       'apply_buff': ['placeholder'],
                                       'reduce_cd': {},
                                       'remove_buff': ['placeholder']},
                            'prohibit_cd_start': None,
                            'target_type': 'player'},
              'e_stun': {'affected_stats': None,
                         'duration': 1,
                         'max_stacks': 1,
                         'on_hit': {'add_dmg': ['placeholder'],
                                    'apply_buff': ['placeholder'],
                                    'reduce_cd': {},
                                    'remove_buff': ['placeholder']},
                         'prohibit_cd_start': None,
                         'target_type': 'enemy'},
              'r_dmg_red': {'affected_stats': {'armor': {'bonus_type': 'additive',
                                                         'stat_mods': None,
                                                         'stat_values': [20.0,
                                                                         35.0,
                                                                         50.0]},
                                               'mr': {'bonus_type': 'additive',
                                                      'stat_mods': {'ap': [0.3]},
                                                      'stat_values': [20.0,
                                                                      35.0,
                                                                      50.0]}},
                            'duration': 8,
                            'max_stacks': 'placeholder',
                            'on_hit': {'add_dmg': ['placeholder'],
                                       'apply_buff': ['placeholder'],
                                       'reduce_cd': {},
                                       'remove_buff': ['placeholder']},
                            'prohibit_cd_start': None,
                            'target_type': 'player'},
              'r_n_hit_initiator': {'affected_stats': None,
                                    'duration': 'permanent',
                                    'max_stacks': 1,
                                    'on_hit': {'add_dmg': ['placeholder'],
                                               'apply_buff': ['placeholder'],
                                               'reduce_cd': {},
                                               'remove_buff': ['placeholder']},
                                    'prohibit_cd_start': None,
                                    'target_type': 'player'},
              'w_buff_0': {'affected_stats': None,
                           'duration': 7,
                           'max_stacks': 1,
                           'on_hit': {'add_dmg': ['placeholder'],
                                      'apply_buff': ['placeholder'],
                                      'reduce_cd': {},
                                      'remove_buff': ['placeholder']},
                           'prohibit_cd_start': 'w',
                           'target_type': 'player'}},
    'dmgs': {'e_dmg_0': {'delay': 0,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'e',
                         'dmg_type': 'physical',
                         'dmg_values': [1.0, 1.0, 1.0, 1.0, 1.0],
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 5,
                         'mods': {'enemy': {}, 'player': {'bonus_ad': 0.5}},
                         'radius': 150,
                         'target_type': 'enemy',
                         'usual_max_targets': 2},
             'q_dmg_0': {'delay': 0,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'q',
                         'dmg_type': 'physical',
                         'dmg_values': [70.0, 110.0, 150.0, 190.0, 230.0],
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {},
                                  'player': {'ap': 0.6, 'bonus_ad': 1.0}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1},
             'r_dmg_0': {'delay': 0,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'r',
                         'dmg_type': 'magic',
                         'dmg_values': [100.0, 160.0, 220.0],
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {}, 'player': {'ap': 0.7}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1},
             'w_dmg_0': {'delay': 0,
                         'dmg_category': 'standard_dmg',
                         'dmg_source': 'w',
                         'dmg_type': 'magic',
                         'dmg_values': [40.0, 75.0, 110.0, 145.0, 180.0],
                         'dot': False,
                         'life_conversion_type': 'spellvamp',
                         'max_targets': 1,
                         'mods': {'enemy': {}, 'player': {'ap': 0.6}},
                         'radius': None,
                         'target_type': 'enemy',
                         'usual_max_targets': 1}},
    'general_attributes': {'e': {'base_cd': [16.0, 14.0, 12.0, 10.0, 8.0],
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'COST CATEGORY': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (70,
                                                                       75,
                                                                       80,
                                                                       85,
                                                                       90)}},
                                 'dashed_distance': None,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'inn': {},
                           'q': {'base_cd': [10.0, 9.0, 8.0, 7.0, 6.0],
                                 'cast_time': 0.25,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'COST CATEGORY': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (65,
                                                                       65,
                                                                       65,
                                                                       65,
                                                                       65)}},
                                 'dashed_distance': 600,
                                 'move_while_casting': False,
                                 'range': [700, 700, 700, 700, 700],
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'r': {'base_cd': [80.0, 80.0, 80.0],
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'COST CATEGORY': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (100,
                                                                       100,
                                                                       100)}},
                                 'dashed_distance': None,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'resets_aa': False,
                                 'toggled': False,
                                 'travel_time': 0},
                           'w': {'base_cd': [7.0, 6.0, 5.0, 4.0, 3.0],
                                 'cast_time': 0,
                                 'castable': True,
                                 'channel_time': None,
                                 'cost': {'stack_cost': None,
                                          'standard_cost': {'COST CATEGORY': 'normal',
                                                            'resource_type': 'mp',
                                                            'values': (30,
                                                                       30,
                                                                       30,
                                                                       30,
                                                                       30)}},
                                 'dashed_distance': None,
                                 'move_while_casting': True,
                                 'range': 0,
                                 'resets_aa': True,
                                 'toggled': False,
                                 'travel_time': 0}}
}

