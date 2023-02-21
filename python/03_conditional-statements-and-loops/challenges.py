
# 2D Arrays
# https://www.tutorialspoint.com/python_data_structure/python_2darray.htm
#
# You are building a game where your player is moving accross a 10 x 10 array map. The game will have 
# have the player start from the location (1,2) where x = 1 (second position in the horizontal) and
# y = 2 (third position in the vertical). Your code should allow the user to navigate around obstacles,
# prevent the player from going out of bounds, and confirm if the user has made it to the goal.

# Note: 
#  1) The player will be marked as 'P' on the map and every time the user moves the player the map
#     should be printed to with the new players location
#  2) Conditional statements should be used to prevent the player from going out of bounds or into the 
#     obsstacle areas marked as 'X'
#  3) Player should be given a win statement when the reach the goal marked with '?'

# Legend:
# 'P' -> Player
# '-' -> Empty space for player to move
# 'X' -> Obstacle (player cant move on those spaces)
# '?' -> Goal

# The game will run in an infinite loop until the player wins. To escape the game use 'ctrl - c'

from IPython.display import clear_output
starting_map = [
    ["P","-","X","X","X","X","-","-","X","X"],
    ["-","-","-","-","-","-","-","-","X","X"],
    ["-","X","X","-","-","X","X","-","X","X"],
    ["-","X","-","-","X","X","X","-","-","X"],
    ["-","X","-","-","-","X","X","X","-","-"],
    ["-","-","X","-","-","X","-","-","-","-"],
    ["X","-","X","X","-","-","-","-","X","-"],
    ["X","-","-","X","X","-","-","X","-","-"],
    ["-","-","-","-","-","-","-","-","?","X"],
    ["X","X","-","-","-","X","X","X","-","X"]
]
player_x_init = 0
player_y_init = 0

def print_map(map):
    for line in map:
        print(f'\t{" ".join(line)}')

def game_on(map):
    mark = []
    for row in map:
        mark.append('?' in row)
    return (True in mark)

def print_partial_map(map, x_pos, y_pos):
    clear_output()
    rows = [y_pos - 1, y_pos, y_pos + 1]
    for row in rows:
        if row > -1 and row < 10:
            if x_pos == 0:
                print(f"\t{' '.join(map[row][x_pos :x_pos + 2])}")
            elif x_pos == 9:
                print(f"\t{' '.join(map[row][x_pos - 1:x_pos + 1])}")
            else:
                print(f"\t{' '.join(map[row][x_pos - 1:x_pos + 2])}")
                
def print_instructions():
    print("Navigate your character:\n \
        [w] for up\n \
        [s] for down\n \
        [a] for left\n \
        [d] for right")

def moves_allowed(map, x_pos, y_pos):
    allowed = ['w','a','s','d']
    if y_pos == 0 or map[y_pos-1][x_pos] == 'X':
        allowed.remove('w')
    if y_pos == 9 or map[y_pos+1][x_pos] == 'X':
        allowed.remove('s')
    if x_pos == 0 or map[y_pos][x_pos-1] == 'X':
        allowed.remove('a')
    if x_pos == 9 or map[y_pos][x_pos+1] == 'X':
        allowed.remove('d')
    return allowed

def input_direction(map, x_pos, y_pos):
    move = input("Where do you want to go ").lower()
    while move not in moves_allowed(map, x_pos, y_pos):
        move = input("You can't do that! Where do you want to go? ").lower()
    return move


def play_game():
    x_pos = player_x_init
    y_pos = player_y_init
    map = starting_map


    print("You know Pokemon Red? Yea, the cave, you're looking for a rare item located at the '?'")
    print("You see this map at the entrance.\n")
    print_map(map)
    print('')
    print("Oh, and you forgot your HM05\n")
    print_instructions()

    
    
    while game_on(map):
        direction = input_direction(map, x_pos, y_pos)

        map[y_pos][x_pos] = '-'
        if direction == 'w':
            y_pos -= 1
        elif direction.lower() == 's':
            y_pos += 1
        elif direction.lower() == 'a':
            x_pos -= 1
        else:
            x_pos += 1
        map[y_pos][x_pos] = 'P'

        print('')
        print_partial_map(map, x_pos, y_pos)
        print('')
        print_instructions()

    print('')
    print_partial_map(map, x_pos, y_pos)
    print('\nYou found an escape rope!')

play_game()