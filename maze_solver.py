
def treasure_hunter(p):
    plant(p['bush'])
    use_item(Items.Fertilizer)
    use_item(Items.Weird_Substance, 1)
    harvest()

    # x, y = measure()
    # if get_pos_x() == x and get_pos_y() == y:
    #     harvest()
    # elif get_pos_x() != x:
    #     if can_move(East) is False or can_move(West) is False:
    #         move(North)
        # elif
    
