# Pumpkin Harvester:
	# Refactor; all drones finished function

p = Entities.Pumpkin

def pumpkin_planter():
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(p)
		move(North)
	return 

def pumpkin_cleric():
	sz = list(range(get_world_size()))
	checked = set()
	i = 0
	while len(checked) < get_world_size():
		move(North)
		i += 1
		
		if i >= get_world_size():
			i = 0
		
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(p)
			use_item(Items.Water)
		elif can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
			checked.add(sz[i])
	return

def mega_kin():
	pumpkin_planter()
	pumpkin_cleric()