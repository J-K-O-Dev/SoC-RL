"""Dice rolling simulation and probability calculation of each roll 
using the np.random.randint"""

import numpy as np
import math

def roll_die(num_rolls):
    """
    Simulates rolling a six-sided die a specified number of times.

    Parameters:
    num_rolls (int): The number of times to roll the die.

    Returns:
    list: A list containing the results of each die roll.
    """
    # Generate random integers between 1 and 6 (inclusive) for the specified 
    # number of rolls
    rolls = np.random.randint(1, 7, size=num_rolls)
    
    return rolls.tolist()
# Example usage:
num_rolls = 10
results = roll_die(num_rolls)
print(f"Results of rolling a die {num_rolls} times: {results}")

# def Theoritical_probability(face,rolls):
#     """
#     Calculates the theoretical probability of rolling a specific face on a six-sided die.

#     Parameters:
#     face (int): The face for which to calculate the theoretical probability.
#     rolls (list): A list containing the results of each die roll.

#     Returns:
#     float: The theoretical probability of rolling the specified face.
#     """
#     if 1 <= face <= 6:
#         return math.comb(len(rolls),rolls.count(face))*1/6**len(rolls)*(5/6)**len(rolls)
#     else:
#         return 0
# this was different from what we do in the calculate_probability_of_face so taking out 


def calculate_probability_of_face(rolls, face):
    """
    Calculates the empirical probability of rolling a specific face.

    Parameters:
    rolls (list): A list containing the results of each die roll.
    face (int): The face for which to calculate the probability.

    Returns:
    float: The empirical probability (observed frequency).
    """
    if not rolls:
        return 0
    count = rolls.count(face)
    total_rolls = len(rolls)
    return count / total_rolls



probability={}
for trial in range(10):
    rolls_count = np.random.randint(1, 1000)  # randomly choose number of rolls between 1 and 1000
    rolls = roll_die(rolls_count)
    for face in range(1, 7):
       probability = {face: {"np.random probability":calculate_probability_of_face(rolls, face),
                             "theoritical probability":1/6}} 
    print(f"trial {trial}: for {rolls_count} rolls probability of getting each face is {probability}")

#RESULTS
"""Results of rolling a die 10 times: [5, 3, 2, 3, 2, 4, 3, 4, 2, 6]
trial 0: for 448 rolls probability of getting each face is {6: {'np.random probability': 0.16071428571428573, 'theoritical probability': 0.16666666666666666}}
trial 1: for 424 rolls probability of getting each face is {6: {'np.random probability': 0.18160377358490565, 'theoritical probability': 0.16666666666666666}}
trial 2: for 852 rolls probability of getting each face is {6: {'np.random probability': 0.1607981220657277, 'theoritical probability': 0.16666666666666666}}
trial 3: for 85 rolls probability of getting each face is {6: {'np.random probability': 0.25882352941176473, 'theoritical probability': 0.16666666666666666}}
trial 4: for 978 rolls probability of getting each face is {6: {'np.random probability': 0.18098159509202455, 'theoritical probability': 0.16666666666666666}}
trial 5: for 710 rolls probability of getting each face is {6: {'np.random probability': 0.17746478873239438, 'theoritical probability': 0.16666666666666666}}
trial 6: for 195 rolls probability of getting each face is {6: {'np.random probability': 0.17435897435897435, 'theoritical probability': 0.16666666666666666}}
trial 7: for 556 rolls probability of getting each face is {6: {'np.random probability': 0.1672661870503597, 'theoritical probability': 0.16666666666666666}}
trial 8: for 862 rolls probability of getting each face is {6: {'np.random probability': 0.17633410672853828, 'theoritical probability': 0.16666666666666666}}
trial 9: for 894 rolls probability of getting each face is {6: {'np.random probability': 0.17114093959731544, 'theoritical probability': 0.16666666666666666}}"""