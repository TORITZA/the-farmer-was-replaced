'''
Module to maximize cacti harvest
'''

# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()

def plant_cacti(p: dict) -> None:
    '''
    Coats the farm in cacti crops as a primer for harvest 
    
    :param p: dict of crop entities 
    '''
    for i in (get_world_size()):
        plant(p['cacti'])
        move(North)
    move(East)
    
def sort_cacti(p: dict) -> None: 
    '''
    Reconfigures the arrangement of the cacti to be in sorted order  
    
    :param p: dict of crop entities
    '''
    for i in (get_world_size()):
        if can_move(East) and measure() < measure(East):
            swap(East)
        if can_move(North) and measure() > measure(North):
            swap(North)
        move(North)
    move(East)

def harvest_cacti(p: dict) -> None:
    '''
    Harvests all cacti 
    
    :param p: dict of crop entities 
    '''
    for i in (get_world_size()):
        harvest()
        move(North)
    move(East)