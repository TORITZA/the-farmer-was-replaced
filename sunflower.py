'''
Docstring for sunflower
'''

def plant_sunflowers_first():
    for i in range(get_world_size()):
        till()
        plant(Entities.Sunflower)
        use_item(Items.Water)
        move(East)

def power_plant():
    flowers = get_world_size()
    while flowers > 0:
        for i in range(get_world_size()):
            for petals in range(15, 6, -1):
                if measure() == petals:
                    harvest()
                    flowers -= 1
            move(East)

