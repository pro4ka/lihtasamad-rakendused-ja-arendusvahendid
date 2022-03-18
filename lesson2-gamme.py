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

print("current current_position_y = ", current_position_y)
print("current current_position_x = ", current_position_x)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0
if can_move_right:
    print("should move right")
if can_move_bottom:
    print("Should move down")
#2. step 2 
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1
#3. step 3
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1
#4. step 4 
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1
#5. step 5 
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0
if can_move_right:
    print("should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1
#6. step 6
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

