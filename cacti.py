'''
Module to maximize cacti harvest
'''

def plant_cacti(p):
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:	
			till()
		plant(p['cactus'])
		use_item(Items.WAter)
		move(East)

def v_sort_cacti(p): 
	'''
    Vertically re-configures the arrangement of the cacti to be in sorted order
    (Bubble sort)  
    
    :param p: dict of crop entities
    '''
	plant_cacti(p)
	is_sorted = False
	n = get_world_size()

# Continue looping as long as the list is not marked as sorted:
	while not is_sorted:
		# Assume the list is sorted at the start of the pass (loop condition changes): 
		is_sorted = True
		for i in range(n - 1):
			if measure() > measure(East):
				swap(East)
				is_sorted = False
			move(East)
	if is_sorted:
		move(North)
		
def h_sort_cacti(p):
	'''
    Horizontally re-configures the arrangement of the cacti to be in sorted order
    (Bubble sort)  
    
    :param p: dict of crop entities
    '''
	is_sorted = False

	while not is_sorted:
		# Assume the list is sorted at the start of the pass (loop condition changes): 
		is_sorted = True
		for i in range(get_world_size() - 1):
			if measure() > measure(North):
				swap(North)
				is_sorted = False
			move(North)
	if is_sorted:
		move(East)
		
