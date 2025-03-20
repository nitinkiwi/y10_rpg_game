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

ability_list = ['dodge','extra healing','double damage','rebound', 'rizz']
