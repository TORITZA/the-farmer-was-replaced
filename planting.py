'''
Module containing functions that plant & harvest an 
assortment of the game's crops
'''

# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()

def search_key(d, target):
	for key, val in search_key.items():
		if val == target:
			return key
	return None

# move through row:
def traverse_row():
	for i in range(get_world_size()):
		move(North)

def grow(p): 
	# :param p: list of crop entities 
	# for 4 columns of the array, plant carrots; otherwise, plant bushes & trees
	# at alternating even/odd tiles 

	if get_entity_type() == Entities.Carrot and can_harvest():
		harvest() 
		till()
		plant(p[2])
	else:
		harvest()

	if get_pos_x() in range(1,7):
		if get_pos_x() in range(3,7):
			till() 
			plant(p[2])
		elif get_pos_y() % 2 == 0 and get_pos_x() % 2 == 0 or get_pos_y() % 2 != 0 and get_pos_x() % 2 != 0: 
			plant(p[1])
			#use_item(Items.Water)
		else: 
			plant(p[0])


# Basic power harvester: 
def pre_sun(p: dict) -> None:
	'''
	Pre-plants sunflowers across all available farmland before harvesting 
	
	:param p: dict of crop entities 
	'''
	for i in range(get_world_size()):
		till()
		plant(p['sunflwr'])
		# use_item(Items.Water)
		move(North)

def sunflwr(p: dict) -> None: 
	'''
	Harvests and re-plants sunflowers 
	
	:param p: dict of crop entities 
	:type p: dict
	'''
	for i in range(get_world_size()):
		harvest()
		till()
		plant(p['sunflwr'])
		use_item(Items.Water)
		move(North)

def weird_sub(p: dict) -> None:
	'''
	Harvests hay, power, and weird substance & re-plants sunflowers
	
	:param p: dict of crop entities 
	:type p: dict
	'''
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		elif get_ground_type() != Grounds.Soil:
			till()
		plant(p['sunflwr'])




	
		
		
		
	
	