import RouletteGame

ROULETTE_FACES = ["0", "00", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                  "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                  "31", "32", "33", "34", "35", "36"]

# Roulette Faces Classification
FIRST_DOZEN = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
SECOND_DOZEN = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
                "23", "24"]
THIRD_DOZEN = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", 
               "36"]

FIRST_COLUMN = []
SECOND_COLUMN = []
THIRD_COLUMN = []

ODD = []
EVEN = []

RED = []
BLACK = []

FIRST_HALF = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
              "13", "14", "15", "16", "17", "18"]
SECOND_HALF = ["19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
                "30", "31", "32", "33", "34", "35", "36"]

# initialise current game state when arriving at a table
initial_game_state = []
print("Please input previous numbers starting from the oldest to newest roll")
print("*********************************************************************")
for i in range(14):
    roll = input("Input roll: ")
    while (roll not in ROULETTE_FACES):
        print("Invalid input")
        roll = input("Please enter a valid input: ")
    initial_game_state.append(roll)

print("\n")
print("Please check if history is correct")
print("**********************************")
print(initial_game_state)

current_game = RouletteGame.RouletteGame(initial_game_state)

print("\n")
print("Initial Classification")
print("**********************")
classified_faces = current_game.classify([FIRST_DOZEN, SECOND_DOZEN, THIRD_DOZEN])
print(classified_faces)

# Now we can start the game
print("\n")
print("Game has begun! Please enter rolls, enter \"esc\" to end game")
print("***********************************************************")

# We consider first by betting only in dozens
roll = input("Enter roll: ")
while(roll != "esc"):
    current_game.add_roll(roll)
    classified_faces = current_game.classify([FIRST_DOZEN, SECOND_DOZEN, THIRD_DOZEN])
    roll = input("Enter roll: ")

print("Game ended, see values below:")
print("*****************************")
print(current_game.get_global_history())
print(current_game.get_last_fourteen_history())
