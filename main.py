from planting import * 


# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()
P = {
	'bush': Entities.Bush, 
	'tree': Entities.Tree, 
	'carrot': Entities.Carrot, 
	'pumpkin': Entities.Pumpkin, 
	'sunflwr': Entities.Sunflower
	}
# change list to dict cuz indexes addle the human (MY) brain

clear()
change_hat(Hats.Tree_Hat)

while True:
	# for each tile in every array:
	for i in range(get_world_size()):
		pre_sun(P)
		sunflwr(P)
		move(East)


 
	



		
	
	