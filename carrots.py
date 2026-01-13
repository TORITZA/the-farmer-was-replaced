'''
Carrot harvester utilizing polyculture 
'''

p = Entities.Carrot

def poly_carrot(p):
    '''
    W.I.P: TO BE FURTHER OPTIMIZED
        --> replant carrots after harvest for more effectual yield 
    
    '''
    for i in range(get_world_size()):
        if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
            till()
            plant(p)
            companion, (x, y) = get_companion()
            while companion != Entities.Grass and (x + y) % 2 != 1:
                harvest()
                plant(p)
                #use_item(Items.Water)
                companion, (x, y) = get_companion()
        move(North)
        if can_harvest():
            harvest()
            plant(Entities.Grass)


def mega_carrot(p):
    '''
    Docstring for mega_carrot
    
    :param p: Description
    '''
    while True:
        for i in range(get_world_size()):
            if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
                if get_ground_type() == Grounds.Grassland:
                    till()
                    plant(Entities.Carrot)
                    companion, (x, y) = get_companion()
                    while companion != Entities.Grass and (x + y) % 2 != 1:
                        harvest()
                        plant(Entities.Carrot)
                        use_item(Items.Water)
                        companion, (x, y) = get_companion()
                move(North)
                if can_harvest():
                    harvest()


# CARROT MEGAFARMER:
"""
for i in range(get_world_size()):
	move(East)
	spawn_drone(mega_carrot)
mega_carrot()

"""