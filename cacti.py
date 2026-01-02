'''
Module to maximize cacti harvest
'''

# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()

def plant_cacti(p):
    for i in range(get_world_size()):
        till()
        plant(p['cactus'])


def sort_cacti(p: dict) -> None: 
    '''
    Reconfigures the arrangement of the cacti to be in sorted order
    (Bubble sort)  
    
    :param p: dict of crop entities
    '''
    plant_cacti(p)
    is_sorted = False

# Continue looping as long as the list is not marked as sorted:
    while not is_sorted:
        # Assume the list is sorted at the start of the pass (loop condition changes): 
        is_sorted = True
        for i in range(get_world_size() - 1):
            if measure() > measure(East):
                swap(East)
                is_sorted = False
            move(North)
    
    
