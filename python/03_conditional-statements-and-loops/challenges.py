
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
        print(" ".join(line))

def navigation(map, x_pos, y_pos, direction):
    # Add code to navigate map
    return map # Doesnt have to return map, could be a dictionary with map and other values *wink wink*

def play_game():
    print("[Enter Epic Backstory to Game here]")
    print("Navigate your character:\n \
        [w] for up\n \
        [s] for down\n \
        [a] for left\n \
        [d] for right")

    x_pos = player_x_init
    y_pos = player_y_init
    map = starting_map

    while(True):
        direction = input("Direction: ")
        navigation(map, x_pos, y_pos, direction)
        print_map(map)


play_game()