import RouletteGame

ROULETTE_FACES = ["0", "00", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                  "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                  "31", "32", "33", "34", "35", "36"]

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

print("Please check if history is correct")
print("**********************************")
print(initial_game_state)

current_game = RouletteGame.RouletteGame(initial_game_state)