import palette


ITEMS_ATTRIBUTES = {
    'abyssal_scepter': {'buffs': {'abyssal_scepter_buff_0': {'buff_source': 'abyssal_scepter',
                                                             'dot': False,
                                                             'duration': 'permanent',
                                                             'max_stacks': 1,
                                                             'on_hit': {},
                                                             'stats': {'flat_magic_penetration': {'additive': {'stat_mods': {},
                                                                                                               'stat_values': 20}}},
                                                             'target_type': 'enemy'}},
                        'dmgs': {},
                        'general_attributes': {'castable': False},
                        'non_unique_stats': {'additive': {'ap': 70,
                                                          'mr': 50}},
                        'secondary_data': {'build_from': {'blasting_wand': 1,
                                                          'negatron_cloak': 1},
                                           'builds_into': set(),
                                           'id': 3001,
                                           'leafs': set(),
                                           'recipe_price': 730,
                                           'roots': {'blasting_wand',
                                                     'negatron_cloak',
                                                     'null_magic_mantle'},
                                           'sell_price': 1708,
                                           'total_price': 2440},
                        'unique_stats': {'ap': {'additive': {'stat_mods': {},
                                                             'stat_values': 70}},
                                         'mr': {'additive': {'stat_mods': {},
                                                             'stat_values': 50}}}},
    'aegis_of_the_legion': {'buffs': {'aegis_of_the_legion_buff_0': {'buff_source': 'aegis_of_the_legion',
                                                                     'dot': False,
                                                                     'duration': 'permanent',
                                                                     'max_stacks': 1,
                                                                     'mr': {'additive': {'stat_mods': {},
                                                                                         'stat_values': 15}},
                                                                     'on_hit': {},
                                                                     'stats': {},
                                                                     'target_type': 'player'}},
                            'dmgs': {},
                            'general_attributes': {'castable': False},
                            'non_unique_stats': {'additive': {'hp': 200,
                                                              'mr': 20},
                                                 'percent': {'hp': 1.0,
                                                             'hp5': 1.0}},
                            'secondary_data': {'build_from': {'crystalline_bracer': 1,
                                                              'null_magic_mantle': 1},
                                               'builds_into': {'banner_of_command',
                                                               'locket_of_the_iron_solari'},
                                               'id': 3105,
                                               'leafs': {'banner_of_command',
                                                         'locket_of_the_iron_solari'},
                                               'recipe_price': 550,
                                               'roots': {'crystalline_bracer',
                                                         'null_magic_mantle',
                                                         'rejuvenation_bead',
                                                         'ruby_crystal'},
                                               'sell_price': 1120,
                                               'total_price': 1600},
                            'unique_stats': {'additive': {'mr': 15}}},
    'aether_wisp': {'buffs': {},
                    'dmgs': {},
                    'general_attributes': {'castable': False},
                    'non_unique_stats': {'additive': {'ap': 30}},
                    'secondary_data': {'build_from': {'amplifying_tome': 1},
                                       'builds_into': {'ardent_censer',
                                                       'lich_bane',
                                                       'ludens_echo',
                                                       'twin_shadows'},
                                       'id': 3113,
                                       'leafs': {None,
                                                 'ardent_censer',
                                                 'lich_bane',
                                                 'ludens_echo',
                                                 'twin_shadows'},
                                       'recipe_price': 415,
                                       'roots': {'amplifying_tome'},
                                       'sell_price': 595,
                                       'total_price': 850},
                    'unique_stats': {'percent': {'move_speed': 0.05}}},
    'amplifying_tome': {'buffs': {},
                        'dmgs': {},
                        'general_attributes': {'castable': False},
                        'non_unique_stats': {'additive': {'ap': 20}},
                        'secondary_data': {'build_from': {},
                                           'builds_into': {'aether_wisp',
                                                           'athenes_unholy_grail',
                                                           'fiendish_codex',
                                                           'haunting_guise',
                                                           'hextech_revolver',
                                                           'mejais_soulstealer',
                                                           'morellonomicon',
                                                           'netherstride_grimoire',
                                                           'pox_arcana',
                                                           'rabadons_deathcap',
                                                           'rite_of_ruin',
                                                           'rylais_crystal_scepter',
                                                           'seekers_armguard',
                                                           'sheen',
                                                           'staff_of_flowing_water',
                                                           'void_staff',
                                                           'wooglets_witchcap',
                                                           'zekes_harbinger'},
                                           'id': 1052,
                                           'leafs': {None,
                                                     'aether_wisp',
                                                     'ardent_censer',
                                                     'athenes_unholy_grail',
                                                     'banner_of_command',
                                                     'enchantment_runeglaive',
                                                     'fiendish_codex',
                                                     'frost_queens_claim',
                                                     'haunting_guise',
                                                     'hextech_gunblade',
                                                     'hextech_revolver',
                                                     'iceborn_gauntlet',
                                                     'liandrys_torment',
                                                     'lich_bane',
                                                     'lost_chapter',
                                                     'ludens_echo',
                                                     'mejais_soulstealer',
                                                     'moonflair_spellblade',
                                                     'morellonomicon',
                                                     'nashors_tooth',
                                                     'netherstride_grimoire',
                                                     'pox_arcana',
                                                     'rabadons_deathcap',
                                                     'rite_of_ruin',
                                                     'rylais_crystal_scepter',
                                                     'seekers_armguard',
                                                     'sheen',
                                                     'staff_of_flowing_water',
                                                     'tricksters_glass',
                                                     'trinity_force',
                                                     'twin_shadows',
                                                     'void_staff',
                                                     'will_of_the_ancients',
                                                     'wooglets_witchcap',
                                                     'zekes_harbinger',
                                                     'zhonyas_hourglass'},
                                           'recipe_price': 435,
                                           'roots': set(),
                                           'sell_price': 305,
                                           'total_price': 435},
                        'unique_stats': {}},
    'ancient_coin': {'buffs': {},
                     'dmgs': {},
                     'general_attributes': {'castable': False},
                     'non_unique_stats': {'percent': {'mp': 0.25,
                                                      'mp5': 0.25}},
                     'secondary_data': {'build_from': {},
                                        'builds_into': {'nomads_medallion'},
                                        'id': 3301,
                                        'leafs': {'nomads_medallion',
                                                  'talisman_of_ascension'},
                                        'recipe_price': 365,
                                        'roots': set(),
                                        'sell_price': 146,
                                        'total_price': 365},
                     'unique_stats': {'additive': {'hp': 3}}},
    'hextech_gunblade': {'buffs': {'hextech_gunblade_cd_modifier_buff': {'on_hit': {}},
                                   'hextech_gunblade_slow_buff': {'buff_source': 'hextech_gunblade',
                                                                  'dot': False,
                                                                  'duration': 2,
                                                                  'max_stacks': 1,
                                                                  'move_speed_reduction': {'multiplicative': {'stat_mods': {},
                                                                                                              'stat_values': 0.4}},
                                                                  'on_hit': {},
                                                                  'stats': {},
                                                                  'target_type': 'enemy'}},
                         'dmgs': {'hextech_gunblade_dmg_0': {'crit_type': None,
                                                             'delay': None,
                                                             'dmg_category': 'standard_dmg',
                                                             'dmg_source': 'hextech_gunblade',
                                                             'dmg_type': 'magic',
                                                             'dmg_values': 150,
                                                             'dot': False,
                                                             'life_conversion_type': 'spellvamp',
                                                             'max_targets': 1,
                                                             'mods': {'enemy': {},
                                                                      'player': {'ap': 0.4}},
                                                             'radius': None,
                                                             'resource_type': 'hp',
                                                             'target_type': 'enemy',
                                                             'usual_max_targets': 1}},
                         'general_attributes': {'base_cd': 60,
                                                'cast_time': 0,
                                                'castable': True,
                                                'channel_time': None,
                                                'dashed_distance': None,
                                                'independent_cast': True,
                                                'move_while_casting': True,
                                                'range': 500,
                                                'resets_aa': False,
                                                'toggled': False,
                                                'travel_time': 0.25},
                         'non_unique_stats': {'additive': {'ad': 40,
                                                           'ap': 80,
                                                           'lifesteal': 0.1}},
                         'secondary_data': {'build_from': {'bilgewater_cutlass': 1,
                                                           'hextech_revolver': 1},
                                            'builds_into': set(),
                                            'id': 3146,
                                            'leafs': set(),
                                            'recipe_price': 800,
                                            'roots': {'amplifying_tome',
                                                      'bilgewater_cutlass',
                                                      'hextech_revolver',
                                                      'long_sword',
                                                      'vampiric_scepter'},
                                            'sell_price': 2380,
                                            'total_price': 3400},
                         'unique_stats': {'additive': {'ap': 150,
                                                       'move_speed': 150,
                                                       'spellvamp': 0.2}}},
    'will_of_the_ancients': {'buffs': {},
                             'dmgs': {},
                             'general_attributes': {'castable': False},
                             'non_unique_stats': {'additive': {'ap': 80},
                                                  'percent': {'cdr': 0.1}},
                             'secondary_data': {'build_from': {'fiendish_codex': 1,
                                                               'hextech_revolver': 1},
                                                'builds_into': set(),
                                                'id': 3152,
                                                'leafs': set(),
                                                'recipe_price': 480,
                                                'roots': {'amplifying_tome',
                                                          'fiendish_codex',
                                                          'hextech_revolver'},
                                                'sell_price': 1750,
                                                'total_price': 2500},
                             'unique_stats': {'additive': {'spellvamp': 0.2}}}}

ITEMS_EFFECTS = {
    'abyssal_scepter': {'enemy': {'actives': {'buffs': [],
                                              'dmg': [],
                                              'remove_buff': []},
                                  'passives': {'buffs': ['abyssal_scepter_buff_0'],
                                               'dmg': [],
                                               'remove_buff': []}},
                        'player': {'actives': {'buffs': [],
                                               'dmg': [],
                                               'remove_buff': []},
                                   'passives': {'buffs': [],
                                                'dmg': [],
                                                'remove_buff': []}}},
    'aegis_of_the_legion': {'enemy': {'actives': {'buffs': [],
                                                  'dmg': [],
                                                  'remove_buff': []},
                                      'passives': {'buffs': [],
                                                   'dmg': [],
                                                   'remove_buff': []}},
                            'player': {'actives': {'buffs': [],
                                                   'dmg': [],
                                                   'remove_buff': []},
                                       'passives': {'buffs': ['aegis_of_the_legion_buff_0'],
                                                    'dmg': [],
                                                    'remove_buff': []}}},
    'aether_wisp': {},
    'amplifying_tome': {},
    'ancient_coin': {},
    'hextech_gunblade': {'enemy': {'actives': {'buffs': ['hextech_gunblade_slow_buff'],
                                               'dmg': ['hextech_gunblade_dmg_0'],
                                               'remove_buff': []},
                                   'passives': {'buffs': [],
                                                'dmg': [],
                                                'remove_buff': []}},
                         'player': {'actives': {'buffs': [],
                                                'dmg': [],
                                                'remove_buff': []},
                                    'passives': {'buffs': ['hextech_gunblade_cd_modifier_buff'],
                                                 'dmg': [],
                                                 'remove_buff': []}}},
    'will_of_the_ancients': {}}

ITEMS_CONDITIONALS = {
    'abyssal_scepter': {},
    'aegis_of_the_legion': {},
    'aether_wisp': {},
    'amplifying_tome': {},
    'ancient_coin': {},
    'hextech_gunblade': {},
    'will_of_the_ancients': {}}


ITEMS_BUFFS_NAMES = palette.items_or_masteries_buffs_or_dmgs_names_dct(str_buffs_or_dmgs='buffs', attrs_dct=ITEMS_ATTRIBUTES)
ITEMS_DMGS_NAMES = palette.items_or_masteries_buffs_or_dmgs_names_dct(str_buffs_or_dmgs='dmgs', attrs_dct=ITEMS_ATTRIBUTES)

CASTABLE_ITEMS = [item_name for item_name in ITEMS_ATTRIBUTES if ITEMS_ATTRIBUTES[item_name]['general_attributes']['castable']]
CASTABLE_ITEMS = tuple(sorted(CASTABLE_ITEMS))


if __name__ == '__main__':

    # All buffs and dmgs names of all items.
    print("Item buffs' names: {}".format(ITEMS_BUFFS_NAMES))
    print("Item buffs' names: {}".format(ITEMS_DMGS_NAMES))
    print("Castable items: {}".format(CASTABLE_ITEMS))
