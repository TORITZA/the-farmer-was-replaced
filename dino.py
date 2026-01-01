# start 0,0 -> traverse entire farm; loop -> collect apples 
# "direction" dict (turn left, turn right)

# directions = ("North", "East", "South", "West")
# if any(move(directions) for coor in directions) is not True:
# built-in any function 

def turn_left():
    move(South)
    for i in range(get_world_size() - 2):
        move(East)

def turn_right():
    move(South)
    for i in range(get_world_size() - 2):
        move(West)

def any_tfwr(iterable):
	falsy = []
	for item in iterable:
		if can_move(item) == False:
			falsy.append(False)
	if len(falsy) == len(iterable):
		return False
	else:
		return True 


def snake():
	directions = (North, East, South, West)

# if cactus cost enough, then permiss the function's execution: 
	cactus_cost = get_cost(Entities.Apple)
	for cactus in cactus_cost:
		if num_items(Items.Cactus) < cactus_cost[cactus]:
			print("MISSING CACTI")

	x, y = get_pos_x(), get_pos_y()

	if any_tfwr(directions) == False:
		print("POOF")
		change_hat(Hats.Wizard_Hat)
		clear()
		change_hat(Hats.Dinosaur_Hat)
		return
		
	if x == 0 and y == 0:
		for i in range(get_world_size()):
			move(North)
		for i in range(get_world_size()):
			move(East)
	elif x == 1 and y == 0:
		move(West)
	elif x == get_world_size() - 1:
		turn_right()
	elif x == 1:
		turn_left()
        