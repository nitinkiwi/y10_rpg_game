import random

def random_chance(range):
    return random.randint(0,range)
enemy_names_list = ['Mushroom Ma','The GG Master','Grubular','Fish','The Walking Stick','Timothy']

enemy_health_list = [100,125,150,175,200,280]

enemy_damage_list = [20,30,40,50,70,80]

enemy_reward_list = [50,70,100,150,200,250]

enemy_level = 0

enemy_stats = {
    'Name':enemy_names_list[random_chance(len(enemy_names_list)-1)],
    'Health':enemy_health_list[enemy_level],
    'Damage':enemy_damage_list[enemy_level],
    'Gold reward':enemy_reward_list[enemy_level],
}