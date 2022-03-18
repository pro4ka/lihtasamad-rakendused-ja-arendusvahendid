map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24],

]
map2 = [
    [12, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 24],

]
map = map2 
# 1. step
start_position_x = 0
start_positioin_y = 0
current_position_x = start_position_x
current_position_y = start_positioin_y
def move(step, current_position_x, current_position_y):
    print("current step is: ", step)
    print("current_position_y =", current_position_y)
    print("current_position_x = ", current_position_x)
    can_move_right = current_position_x <= 2 and map [current_position_y][current_position_x+1]
    can_move_bottom = current_position_y <= 2 and map [current_position_y+1][current_position_x]
    if can_move_right:
        print("Should move right")
        current_position_x = current_position_x + 1
    if can_move_bottom:
        print("shoyld move down")
        current_position_y = current_position_y + 1
    return[current_position_x, current_position_y]

new_position = move (1, start_position_x, start_positioin_y)
new_position = move (2, new_position[0], new_position[1])
new_position = move (3, new_position[0], new_position[1])
