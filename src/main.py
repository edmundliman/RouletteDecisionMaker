import RouletteGame

ROULETTE_FACES = ["0", "00", "1", "2", ""]

# initialise current game state when arriving at a table
initial_game_state = []
print("Please input previous numbers starting from the oldest to newest roll")
print("*********************************************************************")
for i in range(14):
    roll = input("Input roll: ")
    initial_game_state.append(roll)

current_game = RouletteGame.RouletteGame(initial_game_state)