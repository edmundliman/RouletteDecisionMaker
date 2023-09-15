import RouletteGame

# Global constants
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
DOZEN_BETS = [FIRST_DOZEN, SECOND_DOZEN, THIRD_DOZEN]
DOZEN_NAMES = ["P(First Dozen)", "P(Second Dozen)", "P(Third Dozen)"]

FIRST_COLUMN = ["1", "4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"]
SECOND_COLUMN = ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"]
THIRD_COLUMN = ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"]
COLUMN_BETS = [FIRST_COLUMN, SECOND_COLUMN, THIRD_COLUMN]
COLUMN_NAMES = ["P(First Column)", "P(Second Column)", "P(Third Column)"]

ODD = ["1", "3", "5", "7" , "9", "11", "13", "15", "17", "19", "21", "23", "25",
       "27", "29", "31", "33", "35"]
EVEN = ["2", "4", "6", "8" , "10", "12", "14", "16", "18", "20", "22", "24", "26",
       "28", "30", "32", "34", "36"]
ODD_EVEN_BETS = [ODD, EVEN]
ODD_EVEN_NAMES = ["P(Odd)", "P(Even)"]

RED = []
BLACK = []
COLOUR_BETS = [RED, BLACK]
COLOUR_NAMES = ["P(Red)", "P(Black)"]

FIRST_HALF = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
              "13", "14", "15", "16", "17", "18"]
SECOND_HALF = ["19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", 
                "30", "31", "32", "33", "34", "35", "36"]
HALVES_BETS = [FIRST_HALF, SECOND_HALF]
HALVES_NAMES = ["P(First Half)", "P(Second Half)"]

TITLE = ["Global Values", "Last Fourteen Values"]

# initialise current game state when arriving at a table
initial_game_state = []
print("Please input previous numbers starting from the oldest to newest roll")
print("*********************************************************************")
"""for i in range(14):
    roll = input("Input roll: ")
    while (roll not in ROULETTE_FACES):
        print("Invalid input")
        roll = input("Please enter a valid input: ")
    initial_game_state.append(roll)"""
initial_game_state = ['33', '26', '27', '9', '3', '1', '12', '30', '0', '21', '31', '11', '26', '32']

print("\n")
print("Please check if history is correct")
print("**********************************")
print(initial_game_state)

current_game = RouletteGame.RouletteGame(initial_game_state)

# We consider first by betting only in dozens
print("\n")
print("Initial Classification")
print("**********************")
classified_faces = current_game.classify(DOZEN_BETS)
print(classified_faces[0])

# Now we can start the game
print("\n")
print("Game has begun! Please enter rolls, enter \"esc\" to end game")
print("***********************************************************")
current_game.print_prob_table(current_game.naive_binomial(DOZEN_BETS, classified_faces, 
                                                     ROULETTE_FACES), TITLE, DOZEN_NAMES)

roll = input("Enter roll: ")
while(roll != "esc"):
    while (current_game.check_roll(roll, ROULETTE_FACES) == False):
        roll = input("Input invalid! Enter a valid roll: ")
    current_game.add_roll(roll)
    classified_faces = current_game.classify(DOZEN_BETS)
    current_game.print_prob_table(current_game.naive_binomial(DOZEN_BETS, classified_faces, 
                                                     ROULETTE_FACES), TITLE, DOZEN_NAMES)
    roll = input("Enter roll: ")

print("Game ended, see values below:")
print("*****************************")
print("Global Values")
print(current_game.get_global_history())
print("Last Fourteen Values")
print(current_game.get_last_fourteen_history())
