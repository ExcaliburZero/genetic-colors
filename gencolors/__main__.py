import genetics
import numpy as np
import scipy.misc

FACTOR = 8
POPULATION_SIZE = 2 ** FACTOR
GENERATIONS = 100

SCALING = 16

def main():
    population = genetics.create_population(POPULATION_SIZE)

    for g in range(GENERATIONS):
        print(get_average_score(population))

        img_name = "generation_%04d.png" % g
        create_population_image(population, img_name)

        population = genetics.next_generation(population)

def get_average_score(population):
    scores = [genetics.score_chromosome(i) for i in population]

    return np.mean(scores)

def create_population_image(population, img_name):
    # Create the image from the population
    dim = int(2 ** (FACTOR / 2))
    img = np.reshape(population, (dim, dim, 3))
    img = img.repeat(SCALING, axis=0) \
             .repeat(SCALING, axis=1)

    # Save the image
    scipy.misc.imsave(img_name, img)

if __name__ == "__main__":
    main()
