from planting import * 


# GLOBALS: 
X, Y = get_pos_x(), get_pos_y()
P = [Entities.Bush, Entities.Tree, Entities.Carrot, Entities.Pumpkin, Entities.Sunflower]
# change list to dict cuz indexes addle the human (MY) brain

clear()
change_hat(Hats.Tree_Hat)

while True:
	# for each tile in every array:
	for i in range(get_world_size()):
		grow(P)
		pookin(P)
		sunflwr(P, petals())
		move(North)
	move(East)


 
	



		
	
	