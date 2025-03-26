from abilities import ability_upgrades_cost

from character_creation import player_stats

shop_item = 'not chosen'

shop_item_costs = {
    '1':70,
    '2':50,
    '3':50,
    '4':ability_upgrades_cost[player_stats['Ability']],
}