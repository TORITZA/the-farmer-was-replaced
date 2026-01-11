'''
Docstring for sunflower
'''

def plant_sunflowers_first():
    for i in range(get_world_size()):
        if get_ground_type() == Grounds.Grassland:
            till()
        plant(Entities.Sunflower)
        use_item(Items.Water)
        move(East)

def power_plant():
    flowers = get_world_size()
    while flowers > 0:
        for petals in range(15, 6, -1):
            for i in range(get_world_size()):
                if measure() == petals:
                    harvest()
                    flowers -= 1
                move(East)

# SUN-POWER MEGAFARMER:
"""
while True:
    for i in range(get_world_size()):
        move(North)
        spawn_drone(plant_sunflowers_first)
    plant_sunflowers_first()
    for i in range(get_world_size()):
        move(North)
        spawn_drone(power_plant)
    power_plant()
"""


