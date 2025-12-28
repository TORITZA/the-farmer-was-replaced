'''
Carrot harvester utilizing polyculture 
'''

def poly_carrot(p):
    '''
    W.I.P: TO BE FURTHER OPTIMIZED
        --> replant carrots after harvest for more effectual yield 
    
    :param p: dict of crop entities 
    '''
    for i in range(get_world_size()):
        if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
            till()
            plant(p['carrots'])
            companion, (x, y) = get_companion()
            while companion != Entities.Grass and (x + y) % 2 != 1:
                harvest()
                plant(p['carrots'])
                #use_item(Items.Water)
                companion, (x, y) = get_companion()
        move(North)
        if can_harvest():
            harvest()
            plant(Entities.Grass)
