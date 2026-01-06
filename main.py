from planting import * 
from pumpkin import pumpkin_cleric, pumpkin_planter
from cacti import v_drone_sort_cacti, h_drone_sort_cacti, plant_cacti


# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()
P = {
	'bush': Entities.Bush, 
	'tree': Entities.Tree, 
	'carrot': Entities.Carrot, 
	'pumpkin': Entities.Pumpkin, 
	'sunflwr': Entities.Sunflower,
	'cactus': Entities.Cactus
	}

clear()
change_hat(Hats.Tree_Hat)

while True:
	# for each tile in every array:
	# CACTI MEGAFARM PROGRAM: 
	for i in range(get_world_size()-1):
		spawn_drone(v_drone_sort_cacti)
		move(North)
	v_drone_sort_cacti()
	for i in range(get_world_size() - 1):
		spawn_drone(h_drone_sort_cacti)
		move(East)
	h_drone_sort_cacti()
	harvest()
	clear()
	
	
	# --------- Pumpkin harvester:
	# for i in range(get_world_size()):
	# 	pumpkin_planter(P)
	# 	move(East)
	# for i in range(get_world_size()):
	# 	pumpkin_cleric(P)
	# 	move(East)
	# harvest()

# FOR DINO FARM:
# set_world_size(10)
# change_hat(Hats.Dinosaur_Hat)
# while True:
# 	snake()

# FOR CACTI FARM: 
	# while True:
	# 	for i in range(get_world_size()):
	# 		v_sort_cacti(P)
	# 	for i in range(get_world_size()):
	# 		h_sort_cacti(P)
	# 	harvest()

		

 
	



		
	
	