
# HELPER PLANTER FUNCS

# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()


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


# power harvester: 
def petals() -> list:
	# return: list of tuples containing a sunflower's number of petals and its position on the grid; 
	# sorted in ascending order based on the former 
	sun_max = []
	for i in range(get_world_size):
		sun_max.append((Y, measure()))
		move(North)
	return sun_max.sort(key=lambda x: x[1], reverse=True)
	
def sunflwr(p: dict) -> None: 
	# :param p: dict of crop entities 
	# for one column of farm land, plants sunflowers and harvests the current sunflower w/ 
	# highest num of petals until there are 10 left
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
			plant(p['sunflwr'])
			move(North)
		else:
			move(North)
	pt_sz = petals()
	while len(pt_sz) > 10:
		for tile in range(pt_sz[0][0]):
			move(North)
		harvest()
		for tile in range(pt_sz[0][0]):
			move(South)
		pt_sz.pop()


	
		
		
		
	
	