import Binomial

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
    classify(self, list_of_classification)
        classifies the current board state based on the list of classification
        returns a list of list of the classification
    naive_binomial(self)
        please find below the explanation of this method
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

    def classify(self, list_of_classification):
        return_list_global = []
        return_list_last = []

        for i in range(len(list_of_classification)):
            current_list_global = []
            current_list_last = []

            for global_rolls in self.__global_history:
                if (global_rolls in list_of_classification[i]):
                    current_list_global.append(global_rolls)
            for last_rolls in self.__last_fourteen_history:
                if (last_rolls in list_of_classification[i]):
                    current_list_last.append(last_rolls)

            return_list_global.append(current_list_global)
            return_list_last.append(current_list_last)

        return [return_list_global, return_list_last]
    
    """
    The naive_binomial method just considers pure binomial probabilities
    on deciding how to place the bets. Considers next roll to be independent of
    the previous roll. 

    Uses n = len(__global_history) + 1 for __global_history and n = 15 for
    __last_fourteen_history, assuming we know outcome for the first n - 1 trials.

    Then, finds the pmf by considering P(X = len(classification) + 1) where
    x ~ Bi(n, P(classification)). The probability of the next roll being in the
    classification by considering number of successes in sample size n.

    This method does not consider the drift factor based on the hand of the dealer.

    Logical explanation:
    In a n sample size, what is the probability of hitting x + 1 successes
    Naivety: It will average out to equal probabilities.
    """
    def naive_binomial(self, list_of_classification, list_of_classified, faces):
        probability_list = []
        no_choices = len(list_of_classification)
        next_prob_global = []
        next_prob_fourteen = []

        for i in range(no_choices):
            probability_list.append(len(list_of_classification[i]) / len(faces))

        for i in range(no_choices):
            # Using global
            x = len(list_of_classified[0][i]) + 1
            n = len(self.__global_history) + 1
            p = probability_list[i]
            next_prob_global.append(Binomial.dbinom(x, n, p))

            # Using last fourteen
            x = len(list_of_classified[1][i]) + 1
            n = len(self.__last_fourteen_history) + 1
            p = probability_list[i]
            next_prob_fourteen.append(Binomial.dbinom(x, n, p))

        return [next_prob_global, next_prob_fourteen]
    
    """
    This method finds p, the probaility of the next roll hitting the classification
    with sample size n* = n - 1. This method may consider the drift factor created 
    by the hand of the dealer although not yet tested. Each classification is
    treated as a different binomial distribution. To find p, we use maximum 
    likelihood estimation based on existing data.
    """
    def mle_binomial(self, list_of_classified):
        return 0