# start 0,0 -> traverse entire farm; loop -> collect apples 
# "direction" dict (turn left, turn right)

# directions = ("North", "East", "South", "West")
# position = 0

def turn_left():
    move(South)
    for i in range(get_world_size() - 1):
        move(East)

def turn_right():
    move(South)
    for i in range(get_world_size() - 1):
        move(West)

def snake():
    x, y = get_pos_x(), get_pos_y()
    
    if move() is False:
        print("ERROR")
    
    if x == 0 and y == 0:
        for i in range(get_world_size()):
            move(North)
        for i in range(get_world_size()):
            move(East)
    elif x == get_world_size() - 1:
        turn_right()
    elif x == 1:
        turn_left() 
        