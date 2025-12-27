# Tree harvester utilizing polyculture:

def poly_tree(p):
	'''
    W.I.P: TO BE FURTHER OPTIMIZED 
    
    :param p: dict of crop entities 
    '''
	for i in range(get_world_size()):
		if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 or get_pos_x() % 2 != 0 and get_pos_y() % 2 != 0:
			till()
			plant(p['tree'])
			companion, (x, y) = get_companion()
			while companion != Entities.Grass and (x + y) % 2 != 1:
				harvest()
				plant(p['tree'])
				use_item(Items.Water)
				companion, (x, y) = get_companion()
		move(North)
		if can_harvest():
			harvest()
			plant(Entities.Grass)
