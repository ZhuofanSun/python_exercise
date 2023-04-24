# -------------------------------------------------------------------
# Name : Zhuofan Sun
# ID : 1740983
#
# Weekly Exercise #2: Unfair Dice
# -------------------------------------------------------------------


import random


def biased_rolls(prob_list, s, n):
    random.seed(s)
    """Initialize the pseudo-random number generator"""

    rolls = []
    """Initialize the list for putting output of dice"""

    for w in range(n):
        dice_list = []
        """Initialize a list for putting numbers on Dice"""

        for i in range(0, len(prob_list), 1):
            dice_list.append(i + 1)
            """dice_list give the possible outcomes when rolling a dice"""

        def random_pick(lst, probabilities):
            """ Define a new function to set up the probability for each number on dice"""

            x = random.random()
            """"Set up a random float number between 0 and 1"""
            cumulative_probability = 0.0
            for item, item_probability in zip(lst, probabilities):
                cumulative_probability += item_probability
                """item has corresponding probabilities to be set with the range of numbers on the dice"""
                if x < cumulative_probability:
                    break
            return item

        rolls.append(random_pick(dice_list, prob_list))
        """each item returned is added to the list: rolls"""

    return rolls


pass


def draw_histogram(m, rolls, width):
    row = 1
    """Initialize the row starting from 1"""
    lst_a = []
    """Initialize the list for putting the number of times that each row occurs"""
    while row <= m:
        print("%d." % row, end='')
        """print the title of each row:1.
                                       2.
                                       3.
                                       4."""
        col = 1
        """Initialize the column for each row starting from 1"""
        a = rolls.count(row)
        """a is the number of times that each row occurs"""
        lst_a.append(a)
        """ 'a' for each row is added into the list """
        max_item = lst_a[0]
        """suppose the list max_item contains any one value in lst_a, index0, for example"""
        for item in lst_a:
            if max_item < item:
                max_item = item
                """compare all item in lst_a with the selected value, if the item is greater than the selected value
                this item is the max_item."""
        a = round((width / max_item) * a)
        """Change the size of 'a' by scaling"""
        while col <= width:
            print("#" * a, end=''"-" * (width - a))
            """in each row, there are 'a' number of '#', and the rest is '-'"""
            col += 1
            break
        print('')
        row += 1

    pass


#rolls = biased_rolls([1 / 4, 1 / 6, 1 / 12, 1 / 12, 1 / 4, 1 / 6], 42, 200)
#draw_histogram(6, rolls, 10)
'''test of the two functions'''
