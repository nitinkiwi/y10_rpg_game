import random

def random_chance(start, range):
    return random.randint(start,range)
enemy_names_list = ['Mushroom Ma','The GG Master','Grubular','Fish','The Walking Stick','Timothy']

enemy_health_list = [100,125,150,175,200,280]

enemy_damage_list = [20,30,40,50,70,80]

enemy_reward_list = [50,70,100,150,200,250]

enemy_level = 0

adjectives = ['pretty', 'slimy', 'ugly', 'small', 'large', 'excellent', 'master', 'crazy', 'undead', 'young', 'old', 'splendid', 'stupid', 'bloated']

nouns = ['baiter', 'slime', 'avocado', 'zombie', 'panda', 'snake', 'mushroom', 'chicken', 'baby', 'bird', 'sandworm', 'nit', 'mosquito', 'alien']

def enemy_name_generator():
    enemy_name = f'{adjectives[random_chance(0, len(adjectives)-1)]} {nouns[random_chance(0, len(nouns)-1)]}'
    return enemy_name

enemy_stats = {
    'Name':enemy_name_generator(),
    'Health':enemy_health_list[enemy_level],
    'Damage':enemy_damage_list[enemy_level],
    'Gold reward':enemy_reward_list[enemy_level],
}