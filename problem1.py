#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:16:10 2024

@author: stephenson
"""

# Functions used in preparing Guido's gorgeous lasagna.
# Learn about Guido, the creator of the Python language:
# https://en.wikipedia.org/wiki/Guido_van_Rossum
#
# This is a module docstring, used to describe the functionality
# of a module and its functions and/or classes.

# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40  # We assume it takes 40 minutes for the lasagna to bake

# Define the 'bake_time_remaining()' function.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function calculates the remaining bake time based on the elapsed time
    the lasagna has been in the oven. It subtracts the elapsed time from the
    expected bake time.
    """
    # Calculate the remaining bake time by subtracting the elapsed time from the expected bake time
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Define the 'preparation_time_in_minutes()' function.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers to prepare.
    :return: int - preparation time (in minutes).

    This function calculates the time needed to prepare the lasagna based on
    the number of layers to be added. It assumes each layer takes 2 minutes
    to prepare.
    """
    # Assuming each layer takes 2 minutes to prepare
    return number_of_layers * 2

# Define the 'elapsed_time_in_minutes()' function.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    This function calculates the total elapsed time in minutes for preparing
    and baking the lasagna. It takes into account the number of layers added
    and the baking time already elapsed.
    """
    # Calculate the total elapsed time by summing the preparation time and elapsed baking time
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
