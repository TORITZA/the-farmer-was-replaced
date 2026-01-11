from planting import * 
from pumpkin import pumpkin_cleric, pumpkin_planter
from cacti import v_drone_sort_cacti, h_drone_sort_cacti, plant_cacti
from carrots import poly_carrot


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
	for i in range(get_world_size()):
		move(North)
		spawn_drone(poly_carrot)
	poly_carrot()
	



	# -- CACTI MEGAFARM PROGRAM: 
	# for i in range(get_world_size()-1):
	# 	spawn_drone(v_drone_sort_cacti)
	# 	move(North)
	# v_drone_sort_cacti()
	# for i in range(get_world_size() - 1):
	# 	spawn_drone(h_drone_sort_cacti)
	# 	move(East)
	# h_drone_sort_cacti()
	# harvest()
	# clear()

# --- MegaFarm Pumpkin harvester: (WIP - TIMED PUMPKIN ACHIEVEMENT)
	# change_hat(Hats.Pumpkin_Hat)
	# while True:
	# 	for i in range(get_world_size()):
	# 		spawn_drone(pumpkin_planter)
	# 		move(East)
	# 	move(West)
	# 	pumpkin_planter()
	# 	move(East)
	# 	for i in range(get_world_size()):
	# 		spawn_drone(pumpkin_cleric)
	# 		move(East)
	# 	move(West)
	# 	while num_drones() > 1:
	# 		pumpkin_cleric()
	# 	harvest()
	# 	clear()



	# Debug attempt for MegaFarm cacti.py harvester:
	# deployed_drones = []
#	for i in range(get_world_size()-1):
#		v_drone = spawn_drone(v_sort_cacti)
#		deployed_drones.append(v_drone)
#		move(North)
#	v_sort_cacti()
#	for drone in deployed_drones:
#		while has_finished(drone) != True:
#			wait_for(drone)
#	move(North)
#	deployed_drones = []
#	for i in range(get_world_size() - 1):
#		h_drone = spawn_drone(h_sort_cacti)
#		deployed_drones.append(h_drone)
#		move(East)
#	h_sort_cacti()
#	harvest()
#	clear()
	
	# --- Lousy MegaFarm 1x1 Maze Harvester:
	# while True:
	# for i in range(get_world_size()):
	# 	move(North)
	# 	spawn_drone(drone_treasure_hunter)
	# move(East)
	
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

		

 
	



		
	
	