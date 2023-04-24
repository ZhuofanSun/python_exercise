import random


def random_pick(some_list, prob_list):
    x = random.random()
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, prob_list):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


print(random_pick([1, 2, 3, 4], [0.3, 0.1, 0.2, 0.4]))
