EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30
    

def bake_time_remaining(elapsed_bake_time) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """   
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers) -> int:
    """
    Function that takes the actual number of layers from _test.py as an argument
    and returns how much time you need to bake them. 
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) -> int:
    """
    Function that takes the actual number of layers from _test.py as an argument
    and the number of minutes the lasagna has been baking in the oven
    and returns the total number of minutes you've been cooking.
    """
    return  preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

