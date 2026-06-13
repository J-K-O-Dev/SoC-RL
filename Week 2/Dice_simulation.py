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

def Theoritical_probability(face,rolls):
    """
    Calculates the theoretical probability of rolling a specific face on a six-sided die.

    Parameters:
    face (int): The face for which to calculate the theoretical probability.
    rolls (list): A list containing the results of each die roll.

    Returns:
    float: The theoretical probability of rolling the specified face.
    """
    if 1 <= face <= 6:
        return math.comb(len(rolls),rolls.count(face))*1/6**len(rolls)
    else:
        return 0


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
                             "theoritical probability":Theoritical_probability(face,rolls)}} 
    print(f"trial {trial}: for {rolls_count} rolls probability of getting each face is {probability}")

#RESULTS
"""Results of rolling a die 10 times: [1, 2, 2, 5, 1, 1, 5, 4, 4, 2]
trial 0: for 80 rolls probability of getting each face is {6: {'np.random probability': 0.0875, 'theoritical probability': 1.7777816305500147e-53}}
trial 1: for 337 rolls probability of getting each face is {6: {'np.random probability': 0.18397626112759644, 'theoritical probability': 2.3866270059814968e-194}}
trial 2: for 705 rolls probability of getting each face is {6: {'np.random probability': 0.16312056737588654, 'theoritical probability': 0.0}}
trial 3: for 955 rolls probability of getting each face is {6: {'np.random probability': 0.1643979057591623, 'theoritical probability': 0.0}}
trial 4: for 525 rolls probability of getting each face is {6: {'np.random probability': 0.1580952380952381, 'theoritical probability': 4.7032024391826e-311}}
trial 5: for 503 rolls probability of getting each face is {6: {'np.random probability': 0.14512922465208747, 'theoritical probability': 5.853333522749436e-303}}
trial 6: for 329 rolls probability of getting each face is {6: {'np.random probability': 0.16109422492401215, 'theoritical probability': 6.988321565792203e-195}}
trial 7: for 211 rolls probability of getting each face is {6: {'np.random probability': 0.16113744075829384, 'theoritical probability': 1.394314516374227e-125}}
trial 8: for 969 rolls probability of getting each face is {6: {'np.random probability': 0.17234262125902994, 'theoritical probability': 0.0}}
trial 9: for 523 rolls probability of getting each face is {6: {'np.random probability': 0.17973231357552583, 'theoritical probability': 4.592518397620322e-302}}"""