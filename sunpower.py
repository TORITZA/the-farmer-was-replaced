# defunt; TFWR does not support key= argument/lambda sorting 
from planting import *


# Power harvester(s): 
def pre_sun(p):
	'''
	Pre-plants sunflowers across 10 squares of farmland before harvesting 
	
	:param p: dict of crop entities 
	'''
	for i in range(10):
		till()
		plant(p['sunflwr'])
		# use_item(Items.Water)
		move(North)
	for i in range(10):
		move(South)

def petals_srt() -> list:
	'''
    Aggregates each sunflower's number of petals & y-coor position on one column of farmland into 
	a list of tuples 
    
    :return: list of tuples containing a sunflower's number of petals and its position on the grid; 
	sorted in ascending order based on the former
    :rtype: list
    '''
	sun_max = []
	for i in range(get_world_size):
		sun_max.append((Y, measure()))
		move(North)
	return sun_max.sort(key=lambda x: x[1], reverse=True)
	
def sunflwr_srt(p: dict) -> None: 
	'''
    For one column of farm land, plants sunflowers and harvests the current sunflower w/ 
	highest num of petals until there are 10 left
    
    :param p: dict of crop entities
    :type p: dict
    '''
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
			plant(p['sunflwr'])
			move(North)
		else:
			move(North)
	pt_sz = petals_srt()
	while len(pt_sz) > 10:
		for tile in range(pt_sz[0][0]):
			move(North)
		harvest()
		for tile in range(pt_sz[0][0]):
			move(South)
		pt_sz.pop()
		
def petals_y() -> dict:
	'''
    :return: dict containing a key-value pairs of a sunflower's position on the grid & its
    number of petals
    :rtype: dict
    '''
	sun_max = {}
	for i in range(10):
		sun_max[Y] = measure()
		move(North)
	for i in range(10):
		move(South)
	return sun_max

def sunflwr_y(p: dict) -> None: 
	'''
    identify the sunflower with the largest number of petals and harvest it at the 
	corresponding y-coordinate 
    
    :param p: dict of crop entities 
    :type p: dict
    '''
	y_val = search_key(petals_y(), max(petals_y().values))
	for tile in range(y_val):
		move(North)
	harvest()
	till()
	plant(p['sunflwr'])
	use_item(Items.Water) # optional 
	for i in range(y_val):
		move(South)
