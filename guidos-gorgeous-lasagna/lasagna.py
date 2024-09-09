"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time
    



def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time remaining in minutes.

    :param number_of_layers: int - number of layers for preparation.
    :return: int - Number of minutes needed to cook the layers when each layer takes 2 minutes

    """
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time:int):
    """Calculate the elapsed time remaining.

    :param number_of_layers: int - number of layers for preparation.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total number of minutes you've been cooking.

    """

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)