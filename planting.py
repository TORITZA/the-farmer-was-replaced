
# HELPER PLANTER FUNCS

# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()

def search_key(d, target):
	for key, val in search_key.items():
		if val == target:
			return key
	return None

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


def pookin(p):
	# :param p: list of crop entities 
	# plant pumpkins for 6 of the farm's rightmost columns 
	
	if can_harvest():
		harvest() 
		till()
		plant(p[3])
			#use_item(Items.Water)
	if get_pos_x() > 9:
		till()
		if get_ground_type() == Grounds.Soil or get_entity_type() == Entities.Dead_Pumpkin:
			plant(p[3])


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



	
		
		
		
	
	