from random import gauss, randint

import numpy as np

GOAL = (52, 152, 219)
MUTATION_CHANCE = 20
MUTATION_DEVIATION = 5
REPLACE_RATE = 1.1

def score_chromosome(self):
    r_err = abs(self[0] - GOAL[0])
    g_err = abs(self[1] - GOAL[1])
    b_err = abs(self[2] - GOAL[2])

    return r_err + g_err + b_err

def mate_chromosome(self, other):
    c_red = self[0]
    c_green = other[1]
    c_blue = self[2]

    child = np.array([c_red, c_green, c_blue])

    if randint(0, MUTATION_CHANCE) == 0:
        changes = [0, 0, 0]

        color_to_change = randint(0, 2)
        change = random_change()

        changes[color_to_change] = change

        mutate_chromosome(child, changes)

    return child

def random_change():
    change = gauss(0, MUTATION_DEVIATION)
    return change

def bound(value, lower_lim, upper_lim):
    if value > upper_lim:
        return upper_lim
    elif value < lower_lim:
        return lower_lim
    else:
        return value

def mutate_chromosome(self, changes):
    self[0] = bound(self[0] + changes[0], 0, 255)
    self[1] = bound(self[1] + changes[1], 0, 255)
    self[2] = bound(self[2] + changes[2], 0, 255)

def create_population(num):
    return np.array([create_individual() for x in range(num)])

def create_individual():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return np.array([red, green, blue])

def next_generation(population):
    scores = np.array([score_chromosome(c) for c in population])
    positions = np.argsort(scores)
    sorted_population = population[positions]

    midpoint = int(sorted_population.shape[0] / REPLACE_RATE)
    survivors = sorted_population[:midpoint]

    num_children = sorted_population.shape[0] - survivors.shape[0]
    children = create_children(survivors, num_children)

    new_population = np.concatenate([survivors, children])
    return new_population

def create_children(survivors, num_children):
    n_survivors = survivors.shape[0]
    parents = [(randint(0, n_survivors - 1), randint(0, n_survivors - 1)) for _ in range(num_children)]
    
    children = [mate(survivors, par) for par in parents]

    return np.array(children)

def mate(survivors, parents):
    p_1 = survivors[parents[0]]
    p_2 = survivors[parents[1]]
    child = mate_chromosome(p_1, p_2)

    return child
