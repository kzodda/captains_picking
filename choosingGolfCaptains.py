"""
author: Karl Zodda
date: 2025-03-06
Title: Choosing Golf Captains
Purpose: A script to choose golf Captains
"""

# Import the random module
import numpy as np

golfers = ["Ken", "Bauer", "Pumba", "Zods", "Rothe", "Deeno", "Murph", "Johnsy"]

def choose_captains(list_of_golfers: list):
    """
    This function will choose the captains for the golf teams with even odds for everyone
    list_of_golfers: a list of all the golfers
    returns: None, but prints the two captains
    """
    even_odds = len(list_of_golfers)
    print(list_of_golfers)
    vals = np.random.choice(len(list_of_golfers), 2, replace=False)
    print(vals)
    print(list_of_golfers[vals[0]], list_of_golfers[vals[1]])


choose_captains(golfers)