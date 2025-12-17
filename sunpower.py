# defunt; TFWR does not support key= argument/lambda sorting 

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
