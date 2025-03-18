import random
import time

def random_chance(range):
    return random.randint(0,range)

ability_percentages = {
    'dodge':20,
    'double damage':10,
    'rebound':10,
    'rizz':10,
}

ability_description = {
    'dodge':f"This ability gives you a {ability_percentages['dodge']} percent chance every turn to dodge an opponent's attack.",
    'extra healing':f"This ability lets you heal 5 health more than your base stat.",
    'double damage':f"This ability gives you a {ability_percentages['double damage']} percent chance every turn of dealing double damage.",
    'rebound':f"This ability gives you a {ability_percentages['rebound']} percent chance every turn of rebounding an enemy's attack back at them.",
    'rizz':f'This ability gives you a {ability_percentages['rizz']} percent chance every turn of rizzing up your enemy and winning the battle.',
    'Your species does not have an ability.':''
}

player_stats = {
    'Name':'none',
    'Species':'none',
    'Health':10,
    'Damage':10,
    'Healing':10,
    'Gold':0, 
    'Ability':'dodge',
}
ability_upgrades_cost = {
    'dodge':80,
    'extra healing':200,
    'double damage':100,
    'rebound':80,
    'rizz':110,
    'Your species does not have an ability.':350
}
ability_upgrades = {
    'dodge':'Increase your chance of dodging an attack by 3 percent.',
    'extra healing':'Double your healing stat.',
    'double damage':'Increase the multiplier that double damage does by 0.5.',
    'rebound':'Increase your chance of rebounding an attack by 2 percent.',
    'rizz':'Increase your chance of rizzing up your enemy by 2 percent.',
    'Your species does not have an ability.':'Purchase a random ability.'
}
shop_item_costs = {
    '1':70,
    '2':50,
    '3':50,
    '4':ability_upgrades_cost[player_stats['Ability']],
}
ability_list = ['dodge','extra healing','double damage','rebound', 'rizz']

enemy_names_list = ['Mushroom Ma','The GG Master','Grubular','Fish','The Walking Stick','Timothy']

enemy_health_list = [100,125,150,175,200,280]

enemy_damage_list = [20,30,40,50,70,90]

enemy_reward_list = [50,70,100,150,200,250]

enemy_level = 0

enemy_stats = {
    'Name':enemy_names_list[random_chance(len(enemy_names_list)-1)],
    'Health':enemy_health_list[enemy_level],
    'Damage':enemy_damage_list[enemy_level],
    'Gold reward':enemy_reward_list[enemy_level],
}

del enemy_names_list[enemy_names_list.index(enemy_stats['Name'])]

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
stats_chosen = False

double_damage_multiplier = 2

# Intro
print('Welcome adventurer! Before you lies the entrance to the dungeons.')
time.sleep(0.2)
print('They say an amulet that gives the wearer max aura is hidden in the depths of the dungeons.')
time.sleep(2)
print('But it is protected by many powerful and beastly guardians.')
time.sleep(2)
player_stats['Name'] = input('If it is the amulet you seek, you are brave for coming here! What may your name be? ')
time.sleep(0.5)
print(f'Welcome to the dungeons {player_stats['Name'].title()}!')
time.sleep(0.2)

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

player_stats['Species'] = input('What species would you like to be? (human/dwarf/wizard/sigma) ')
time.sleep(0.2)

choose_stats(player_stats['Species'])

print('\nHere are your stats:\n')
print('\n'.join("{}: {}".format(k, v) for k, v in player_stats.items()))
print(ability_description[player_stats['Ability']])

time.sleep(0.2)

input('\nNow you are ready for your journey into the dungeons!\nGood luck! (Press enter to begin) ')

time.sleep(0.2)

def ability(player_ability):
    if player_ability == 'dodge':
        if random_chance(100) <= ability_percentages['dodge']:
            player_stats['Health'] = player_stats['Health'] + enemy_stats['Damage']
            print('But you dodged the attack! You lost no health.')
            time.sleep(2)
    if player_ability == 'double damage':
        if random_chance(100) <= ability_percentages['double damage']:
            enemy_stats['Health'] = (enemy_stats['Health'] + player_stats['Damage']) - player_stats['Damage'] * double_damage_multiplier
            print(f'Your ability activated and you did an extra {player_stats['Damage']} damage!')
            time.sleep(2)
    if player_ability == 'rebound':
        if random_chance(100) <= ability_percentages['rebound']:
            enemy_stats['Health'] = enemy_stats['Health'] - enemy_stats['Damage']
            player_stats['Health'] = player_stats['Health'] + enemy_stats['Damage']
            print(f'But your ability rebounded the attack!\n{enemy_stats['Name']} took {enemy_stats['Damage']} damage and has {enemy_stats['Health']} health!')
            time.sleep(2)
    if player_ability == 'rizz':
        if random_chance(100) <= ability_percentages['rizz']:
            enemy_stats['Health'] = 0
            print('Your ability activated and you rizzed up your enemy, winning the battle!')
            time.sleep(2)


def attack(attacker, attacked):
    if attacker['Name'] == player_stats['Name']:
        time.sleep(1)
        print('\nYou attack!')
    else:
        time.sleep(1)
        print(f'\n{attacker['Name']} attacks!')
    # There is a two thirds chance that the number will be below 2, so therefore a two thirds chance of an attack being successful.
    if random_chance(2) < 2:
        # Changing health stats and then there is a lot of narration.
        attacked['Health'] = attacked['Health'] - attacker['Damage']
        if attacker['Name'] == player_stats['Name']:
            time.sleep(1)
            print(f"Your attack was a success! You did {str(attacker['Damage'])} damage.")
            time.sleep(1)
            if player_stats['Ability'] == 'double damage' or player_stats['Ability'] == 'rizz':
                ability(player_stats['Ability'])
            print(f'{attacked['Name']} now has {attacked['Health']} health.')
            time.sleep(1)
            print(f'You also healed {str(player_stats['Healing'])} health points.')
            time.sleep(1)
            player_stats['Health'] = player_stats['Health'] + player_stats['Healing']
            if enemy_stats['Health'] <= 0:
                print(f'You vanquished {enemy_stats['Name']}!')
        else:
            # Changing health stats and then there is a lot of narration.
            time.sleep(1)
            print(f"{attacker['Name']}'s attack was a success! He did {str(attacker['Damage'])} damage.")
            time.sleep(1)
            if player_stats['Ability'] == 'rebound' or player_stats['Ability'] == 'dodge':
                ability(player_stats['Ability'])
            print(f'You now have {attacked['Health']} health.')
            if attacked['Health'] <= 0:
                print(f'You were vanquished by {enemy_stats['Name']}!')
    else:
        # Same as earlier but if the attack fails.
        if attacker['Name'] == player_stats['Name']:
            time.sleep(1)
            print('Your attack failed!')
            time.sleep(1)
            if player_stats['Ability'] == 'rizz':
                ability(player_stats['Ability'])
            print(f'{enemy_stats['Name']} still has {enemy_stats['Health']} health.')
            time.sleep(1)
            print(f'You healed {str(player_stats['Healing'])} health points.')
            time.sleep(1)
            player_stats['Health'] = player_stats['Health'] + player_stats['Healing']
        else:
            time.sleep(1)
            print(f"{enemy_stats['Name']}'s attack failed!")
            time.sleep(1)
            print(f'You still have {player_stats['Health']} health.')

for i in range(0,len(enemy_names_list)):
    print(f'\nYou now enter the next room of the dungeons.\n\nInside is an enemy: {enemy_stats['Name']}!')
    time.sleep(1)
    print(f"\nHere are {enemy_stats['Name']}'s stats:\n")
    print('\n'.join("{}: {}".format(k, v) for k, v in enemy_stats.items()))
    input('\n(Press enter to continue) ')
    print('\nYou fight!')

    while player_stats['Health'] > 0 and enemy_stats['Health'] > 0:
        # The fighting sequence with the 'attack' function.
        time.sleep(1)
        attack(player_stats,enemy_stats)        
        if enemy_stats['Health'] < 1:
            break
        attack(enemy_stats,player_stats)
        if player_stats['Health'] < 1:
            break
    if player_stats['Health'] < 1:
        break
    # Getting your gold reward if you won the battle and then entering the shop.
    time.sleep(1)
    print(f'\nYou earned {str(enemy_stats['Gold reward'])} gold!')
    time.sleep(2)
    player_stats['Gold'] = player_stats['Gold'] + enemy_stats['Gold reward']
    print(f'You have in total {player_stats['Gold']} gold.')
    time.sleep(1)
    print("\nYou go into the next room of the dungeons. To your suprise, there is an adventurer's shop there!")
    time.sleep(2)
    shop_item = input(f"\nWhich upgrade do you want?\n1. Add 10 to your damage stat. (70 gold)\n2. Add 5 to your healing stat. (50 gold)\n3. Gain 30 health. (50 gold)\n4. Ability upgrade: {ability_upgrades[player_stats['Ability']]} ({ability_upgrades_cost[player_stats['Ability']]} gold)\n\nEnter the number of the upgrade you want or 'q' if you do not want an upgrade: ")
    time.sleep(1)
    if shop_item == '1' and player_stats['Gold'] >= shop_item_costs[shop_item]:
        # These conditionals are checking firstly which item you have chosen and then if the amount of gold you have 'player_stats['Gold]' is more or equal to the cost of the item you have selected 'shop_item_costs[shop_item]'
        player_stats['Damage'] = player_stats['Damage'] + 10
        print('\nYour damage has been upgraded.')
        player_stats['Gold'] = player_stats['Gold'] - 70
    elif shop_item == '2' and player_stats['Gold'] >= shop_item_costs[shop_item]:
        player_stats['Healing'] = player_stats['Healing'] + 5
        print('\nYour healing has been upgraded.')
        player_stats['Gold'] = player_stats['Gold'] - 50
    elif shop_item == '3' and player_stats['Gold'] >= shop_item_costs[shop_item]:
        player_stats['Health'] = player_stats['Health'] + 30
        print('\nYour health has been upgraded.')
        player_stats['Gold'] = player_stats['Gold'] - 50
    elif shop_item == '4' and player_stats['Gold'] >= shop_item_costs[shop_item]:
        print('Your ability has been upgraded.')
        player_stats['Gold'] = player_stats['Gold'] - ability_upgrades_cost[player_stats['Ability']]
        if player_stats['Ability'] == 'dodge':
            ability_percentages['dodge'] = ability_percentages['dodge'] + 3
        elif player_stats['Ability'] == 'extra healing':
            player_stats['Healing'] = player_stats['Healing'] * 2
        elif player_stats['Ability'] == 'double damage':
            double_damage_multiplier = double_damage_multiplier + 0.5
        elif player_stats['Ability'] == 'rebound':
            ability_percentages['rebound'] = ability_percentages['rebound'] + 2
        elif player_stats['Ability'] == 'rizz':
            ability_percentages['rizz'] = ability_percentages['rizz'] + 2
        elif player_stats['Ability'] == 'Your species does not have an ability.':
            # The extra 240 gold take away is because it cost 350 gold to get an ability and only 110 to upgrade an ability.
            player_stats['Gold'] = player_stats['Gold'] - 240
            player_stats['Ability'] = ability_list[random_chance(3)]
            if player_stats['Ability'] == 'extra healing':
                player_stats['Healing'] = player_stats['Healing'] + 5
            print(f'Your new ability is {player_stats['Ability']}.')
            time.sleep(2)
            print(ability_description[player_stats['Ability']])
            time.sleep(2)
        else:
            print('Your species does not have an ability so for you this upgrade is not valid.')
    elif shop_item == 'q':
        print('\nYou move past the shop.')
    elif player_stats['Gold'] < shop_item_costs[shop_item]:
        print("\nAre you dumb? You didn't have enough gold to purchase that item. You missed your chance to buy an upgrade.")
    else:
        print('That is not a valid item to purchase.')

    ability_description = {
        'dodge':f"This ability gives you a {ability_percentages['dodge']} percent chance every turn to dodge an opponent's attack.",
        'extra healing':f"This ability lets you heal 5 health more than your base stat.",
        'double damage':f"This ability gives you a {ability_percentages['double damage']} percent chance every turn of dealing double damage.",
        'rebound':f"This ability gives you a {ability_percentages['rebound']} percent chance every turn of rebounding an enemy's attack back at them.",
        'rizz':f'This ability gives you a {ability_percentages['rizz']} percent chance every turn of rizzing up your enemy and winning the battle.',
        'Your species does not have an ability.':''
    }
    # Representing stats after upgrades and the battle.
    time.sleep(1)
    print('\nHere are your stats after your battle:\n')
    time.sleep(1)
    print('\n'.join("{}: {}".format(k, v) for k, v in player_stats.items()))
    print(ability_description[player_stats['Ability']])
    input('(Press enter to continue) ')

    enemy_level = enemy_level + 1

    if enemy_level < 6:
        enemy_stats = {
            'Name':enemy_names_list[random_chance(len(enemy_names_list)-1)],
            'Health':enemy_health_list[enemy_level],
            'Damage':enemy_damage_list[enemy_level],
            'Gold reward':enemy_reward_list[enemy_level] 
        }

    del enemy_names_list[enemy_names_list.index(enemy_stats['Name'])]

if player_stats['Health'] > 0:
    print('\nYou beat the final enemy in the dungeons!')
    time.sleep(1)
    print('\nThere is golden light coming from the door ahead of you.')
    time.sleep(1)
    print('\nYou go through to door into what seems to be the final room of the dungeons.')
    time.sleep(1)
    print('\nOn a pedestal in front of you is the amulet.')
    time.sleep(1)
    print('\nYou take it and become a hero!')
    time.sleep(1)
    print('\nThanks for playing!')
    time.sleep(5)
    print('\n\nCredits:')
    print('\nCreated and programed by Nitin Keswani.')
    easter_egg = input('\nAll rights reserved. Copyright 2025 to Nitin Keswani\n ')
    if easter_egg.lower() == 'easter egg':
        print("\nBefore you left the amulet's chamber you noticed an engraved stone on the ground.")
        time.sleep(3)
        print('\nIt said...')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.\n')
        time.sleep(1)
        print('''
    ░░░:=░»____,░░Ü░░░░░░░░,:.:,╔╦╔╓▒╥╥╔╦╠▒▒▒░;__░`»_░`░»░»»Ü▒▒▒▒╠▒▒▒Ü░░»»_``░=░░░░░
    `²»»░░░░░░░░░░:░░░░░░╔╔╔╦▒▒▒▒▒▒▒▒▒▒╠╠╠ÄÜ╠Ü▒▄▄▒Ü▒Ü░▒░░░:=░╚▒▒▒░▄▒▒▒░░=»░,░░░╓░░░░
    ______;_'░░░░░░░░░░░░░░Ü░ÜÜ▒▒░╠▒▒▒╩░╢▓▓▓▓▓▓▓▓▓▓▓▄▒▒▒▒▒▒╠╠╠É▄▓█▓ÑÄ▓▓▒▓Ñ█╬▓X│░²²`░
    __░___________»░»░»░░░`:░░░╚Ü▒▒╚Ü╩▒╬╣▓█████▓███▓▓▓▒╚╚╙╚╚╩╠ÑÑÄÑÉÑÖÑÜ╠Ü╙│▒"░¬    ░
     ,.. `  ____:░»░░░»»░░___'=`╚ÜÜ░Ü╔▒╬╬╬╬╬╬▓╬╬╬╬▓▓██▓Ü░░░░¼▒▒▒▒▒▒▒░»».▌▄█▌p▓/_  `:
     `_ . _»░░░░»`]░░░░`░░░░░░░░Ü░▒▒▒╫▓╬╬╬╬╬╠╠╠╠╠╠╠╠╫▓▓╦╦╦╠╦╠▒╚▒▒▒▒▒▒▒╔4Ñ»╚.L,.    =
    `:░░░░»░░░░`--=░░░░≈░░░░ÜÜ░░░░▒▒╠╫╬╩╣╣╣╬╬╠╠▒╩▒▒╠╣▓▌╠╠▒╠╠╠░░╠╠▒╠▒╚▒Ü▒▒▒░░..`_```
    ░»»»░»»»»»    »»»»»░»░░` ______░▒Ü╠╣╬╬╬╬╬▒╠╣╬╬╠╠╫▓Ü`]░╚▒▒▒▒▒▒▒▒▒░»╙Ü▒Ü▒▒▒▒░░....
    »»-`  ``»`_   »┌»»»»`. . . ,___[╠H░╬╬╬╬╬╬▒▒▒╠▒▒╠╣▄»ⁿ¡ⁿ¡╙╚╠▒▒▒▒▒▒░░»[ÜÜ▒▒ÜÜÜ░▒░╔_
    » _  ___:»:░__::░»»»»_    _,___,╠▒░╬╬╬╬╬╬╩Ñ╠▒▒╠╠╬Ü░`⌠^^░^░╠▒▒▒▒▒░░░▒▒ÜÜÜ░░░▒Ü▒▒▒
    »░░```░»»```░»»»»»»░. __________░ [╬╬╬╬╬╬▒Ä╠▒╠╠╚Ü░░^⌠^^Ü!╚▒▒▒▒▒▒▒▒▒╠▒Ü░░░»░░╚▒▒▒
    »░░░░░░²` ` `░»»»»»░_________--_░╓φ╠╬╬╬╬╠╠╠╠╠╠░░░░░ⁿ⌠∩^░∩░╠▒▒▒▒▒▒▒░Ü╚ÜÜ░░^|▒▒▒╩╙
    ░_»'²░░_  _  ]»»░░░░░░░_   »-,╦▒▒▒╠╬╬╣╣╣╣╬╬╬╠╠▒▒░░░^^∩░¼@╠▒▒▒▒▒▒Ü░░░=╙ÜÜ▒ÜÜ░ÜÜ░░
    _ ` ``░░ ``  ░»░░░__`░░░░╔╔╓╓▒▒▒▒▒▐╬╬╬╬╬╠╠╠╠╠Ü▓▓▒░░:░░╦╠▒╠╚▒▒▒▒▒Ü░░░░»[Ü╙^░░░▒▒╦
    ░__-  |░_ `` ░░░░░░=░░░░ÜÜ▒▒▒╩Ü╙[╟▒╬╬╬╬╬╬╠▒╩░¢████▓▓▓╬▒▒▒░░░▒▒▒▒╠░»»»»▒Ü``»::╚▒▒
    ░░__. '░∩ '_ ░░░░░░░░Ü`,╔▒▒╬╬╬╠[Ü╟╬╬╬╢╬╬╣╬Ü░░╫████████████▓▓▓╣▄▒╠░░░»░▒░`»._¼╠▒▒
    Ü░░_.._░░░░_»Ü░▒Ü▒ÜÜ╦▒╬╣▓████▓H▒▒╫▓╣╬╬╬ÑÜ░░░▓███████████████████▓▒░Ü░╠Ü"»░_╔▒╠╚╠
    ,[░░,|░░░╚╩░▒░Ü▒▒▒╟▓▓█████████▒▄▌╫▓▓▓▒▒▄░░)██████████████████████▌░▒▒╠╠░░░╔▒▒Ü░░
    ░░░Ü░░Ü.. `'╚░Ü▒▒▒╫█████████████▓▓▓▓▓▒╫▄╬╬████████████████████████▒ÜÜ╚╠╠▒▒▒▒▒░Ü░
    ╠▒Ü▒▒Ü░``»' |░░░▒▒▓█████████████▓╬╣▓╣▀▀▓▓▓█████████████████████████▒░░░▒╠╠▒╠▒▒▒▒
    ╠▒▒▒▒▒Ü∩^:^¬╚░▒▒▒╠▓█████████████▓▓╬╬╬╬▀▀▀██████████████████████████▒░░░▒▒▒▒▒▒╙╙╙
    ▒▒░╙╠▒▒▒░=»»╚▒▒▒╠╠▓█████████████▓▓▒╠╠▓╬▓▓███████████████████████████▌░░▒▒╠╠╠▒░²░
    ▒Ü░≡Ü▒ÜÜÜ»░,░▒▒▒╠║██████████████▓▓▒▒▓▓╬▓█████████████████████████████▓▄▒▒Ü░╚▒Ü--
    ╩=░░░▒▒░▒░--░░▒▒▒║███████████████▓╣╣▓▓▓▓██████╬╬╠╠▓▓▓▓██████████████████▓▒░░╚Ü░
    U░╔╦▒▒Ü░ÜÜ░ ░Ü▒▒▒▒███████████████▓╬╣▓▓▓███████╬╣╬╬╬╬╬╬╬▓███████████████████▓▄░▒░
    ░░▒╠▒▒▒_░ÜÜ░Ü▒▒▒▒░███████████████▓╬╣▓▓▓████████▓▓╬╬╬╬╬╬╬╬████████████████████▒▒▒
    ╠╠╠╩░░╚▒▒▒░ÜÜ▒╠▒╠▒███████████████▓╬╣▓███████████▓╬╬╬╬╬╬╬╬╫███████████████████▒╠╠
    ╠╠░░;__,Ü░░░░Ü▒▒▒▒███████████████▓╬╣▓▓███████████████▓╬╬╬╣███████████████████▌▒▒
    ░░░░░░»_░^▒░Ü▒▒▒▒╢█▓███████▓▓╬╬╬██▓╣██████████████████████████████████████████╠╠
    ▒ÄÜ≡HHHHH░≡╠▒╠╠╠╠╠▓███╬╬╣▓▓▓▓▓▓███▓╣████████████████████████████████████████▓Ñ╠╬
    ▒▒░ûÜ░░░░╔╠╠▒╠╠╠╠╠▓██▓█▓╣▓╬╬╬▓▓███▓╣██████████████████████████▓▓▓██████▀▀▀ÑÜ▒╩╠╬
    ╬╠▒░░░░╠╠╠╠╠╠╠╠╠╠╬╬▓████▓▓▓▓▓▓▓████▓███████████████████████████╬╠╠╠╠╠╢╠╠╠╠▒▒╠╬╬╬
    ╬╬╬▒▒╠╠╠╠╠╠╠╠╬╬╬╬╬╠╬╬╬╫███▓▓▓██████▓███████████████████████████╬╬╠╬╠╬╬╬╠╠╠╠╠╬╬╬╬
    ╬╬╬╬╬╬╬╬Ü▒╠╠╬╬╬╬╬╬▒╠╬╬╬╬▓██████████▓███████████████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    ╠╠╬╬╬╬▒▒▒▒╠╠╬╬╬╬╬▒▒▒╠╠╬╬╬╬╬▓███████▓████████████████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    ╬╬╬╬╬╬▒▒▒▒╠╬╬╬╬╬╬╠╠╠╠╟╬╬╬╬╣█████▓▓▓▓████████████████████████████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬
    

''')
    print('\nNever gonna give you up!\nNever gonna let you down!\nNever gonna run around and desert you!')