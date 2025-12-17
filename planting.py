
# HELPER PLANTER FUNCS

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
def petals():
	# :param n: max num of petals out of all planted sunflowers 
	# return: coordinates of current sunflower w/ greatest amount of petals 
	n = 0 	
	if get_entity_type() == Entities.Sunflower:
		if measure() > n: 
			n = measure() 
			move(North)
	return n 
	
def sunflwr(p, n): 
	# :param p: list of crop entities 
	# :param x: x-coor of drone
	# :param y: y-coor of drone 
	# for two columns of farm land, plants sunflowers and harvests the sunflower w/ 
	# highest num of petals
	if get_pos_x() == 0 or get_pos_x() == 7:
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Sunflower:
			plant(p[4])
		elif can_harvest():
			harvest() 
			till()
			plant(p[4])
		else:
			pass

	# x, y = get_pos_x(), get_pos_y()
	# sun_coors = {}
	# if x == 0:
	# 	sun_coors[(x,y)] = measure()
	# if len(sun_coors) == get_world_size():	
	# 	max_p = list(sun_coors.items).sort(key=lambda x: x[1], reverse=True) 
			
		
	
		
		
		
	
	