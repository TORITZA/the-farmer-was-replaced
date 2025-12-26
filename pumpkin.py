# Pumpkin harvester:

def pumpkin_planter(p):
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(p['pumpkin'])
		move(North)

def pumpkin_cleric(p):
	sz = list(range(get_world_size()))
	checked = set()
	i = 0
	while len(checked) < get_world_size():
		move(North)
		if i == get_world_size:
			i = 0
		else:
			i += 1
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(p['pumpkin'])
			use_item(Items.Water)
		elif can_harvest() and get_entity_type() != Entities.Dead_Pumpkin:
			checked.add(sz[i])
