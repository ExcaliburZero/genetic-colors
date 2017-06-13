from random import randint

GOAL = (52, 152, 219)
MUTATION_CHANCE = 100
MUTATION_RANGE = 15
REPLACE_RATE = 1.1

class Chromosome(object):
    red = None
    green = None
    blue = None

    def __init__(self, r, g,b):
        self.red = r
        self.green = g
        self.blue = b

    def score(self):
        r_err = abs(self.red - GOAL[0])
        g_err = abs(self.green - GOAL[1])
        b_err = abs(self.blue - GOAL[2])

        return r_err + g_err + b_err

    def mate(self, other):
        c_red = self.red
        c_green = other.green
        c_blue = self.blue

        child = Chromosome(c_red, c_green, c_blue)

        if randint(0, MUTATION_CHANCE) == 0:
            r_change = randint(-MUTATION_RANGE, MUTATION_RANGE)
            g_change = randint(-MUTATION_RANGE, MUTATION_RANGE)
            b_change = randint(-MUTATION_RANGE, MUTATION_RANGE)
            child.mutate(r_change, g_change, b_change)

        return child

    def mutate(self, r_change, g_change, b_change):
        self.red = self.red + r_change
        self.green = self.green + g_change
        self.blue = self.blue + b_change


def create_population(num):
    return [create_individual() for x in range(num)]

def create_individual():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    return Chromosome(red, green, blue)

def next_generation(population):
    scores = [(x.score(), x) for x in population]
    scores.sort(key=lambda tup: tup[0])

    midpoint = int(len(scores) / REPLACE_RATE)
    survivors = [x for (_,x) in scores[:midpoint]]

    num_children = len(scores) - midpoint
    children = create_children(survivors, num_children)

    new_population = survivors + children
    return new_population

def create_children(survivors, num_children):
    n_survivors = len(survivors)
    parents = [(randint(0, n_survivors - 1), randint(0, n_survivors - 1)) for _ in range(num_children)]
    
    children = [mate(survivors, par) for par in parents]

    return children

def mate(survivors, parents):
    p_1 = survivors[parents[0]]
    p_2 = survivors[parents[1]]
    child = p_1.mate(p_2)

    return child
