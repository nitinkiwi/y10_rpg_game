from abilities import ability_list
import random

def random_chance(range):
    return random.randint(0,range)

player_stats = {
    'Name':'none',
    'Species':'none',
    'Health':10,
    'Damage':10,
    'Healing':10,
    'Gold':0, 
    'Ability':'dodge',
}

species = ['human', 'dwarf','wizard', 'sigma']

health_multipliers = {
    'human':12,
    'dwarf':8,
    'wizard':12.1,
    'sigma':13
}

damage_multipliers = {
    'human':5,
    'dwarf':8,
    'wizard':6,
    'sigma':6
}

def choose_stats(species):
    # The next two lines multiply your original health and damage stat by your species multiplier.
    player_stats['Health'] = player_stats['Health'] * health_multipliers[species]
    player_stats['Damage'] = player_stats['Damage'] * damage_multipliers[species]
    if species == 'human' or species == 'wizard':
        # Selecting a random ability if your species can have an ability at the start of the game.
        player_stats['Ability'] = ability_list[random_chance(3)]
        if player_stats['Ability'] == ability_list[1]:
            # Adding the 5 healing bonus for the extra healing ability.
            player_stats['Healing'] = player_stats['Healing'] + 5
    elif species == 'dwarf':
        player_stats['Ability'] = 'Your species does not have an ability.'
    else:
        # Sigmas always get the 'rizz' ability.
        player_stats['Ability'] = 'rizz'

stats_chosen = False

double_damage_multiplier = 2