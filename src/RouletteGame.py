class RouletteGame:
    """
    A class used to represent an game of roulette
    ...

    Attributes
    ----------
    global_history : list of str
        a list of string holding all rolls that have appeared so far
    last_fourteen_history : list of str
        a list of strings holding the last fourteen rolls, newest being last

    Methods
    -------
    get_global_history(self)
        getter function for global_history
    """

    def __init__(self, global_history):
        self.global_history = []
        self.last_fourteen_history = []

    def get_global_history(self):
        return self.global_history

    def __add_roll(self, roll):
        return 0
    
    def next_roll(roll: str):
        return 0