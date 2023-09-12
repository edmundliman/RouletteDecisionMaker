class RouletteGame:
    """
    A class used to represent an game of roulette
    ...

    Attributes
    ----------
    __global_history : list of str
        a list of string holding all rolls that have appeared so far
    __last_fourteen_history : list of str
        a list of strings holding the last fourteen rolls, newest being last

    Methods
    -------
    add_roll(self, roll)
        adds the latest roll to both __global_history and __last_fourteen_history
        removes the oldest roll from __last_fourteen_history
    """

    def __init__(self, initial_game_state):
        self.__global_history = initial_game_state.copy()
        self.__last_fourteen_history = initial_game_state.copy()

    def get_global_history(self):
        return self.__global_history

    def get_last_fourteen_history(self):
        return self.__last_fourteen_history
    
    def add_roll(self, roll):
        self.__global_history.append(roll)
        self.__last_fourteen_history.append(roll)
        self.__last_fourteen_history.pop(0)