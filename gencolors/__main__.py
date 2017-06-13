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
    scores = [i.score() for i in population]

    return np.mean(scores)

# https://stackoverflow.com/questions/12062920/how-do-i-create-an-image-in-pil-using-a-list-of-rgb-tuples
def create_population_image(population, img_name):
    # Image size
    width = int((2 ** (FACTOR / 2)) * SCALING)
    height = int((2 ** (FACTOR / 2)) * SCALING)
    channels = 3

    # Create an empty image
    img = np.zeros((height, width, channels), dtype=np.uint8)

    # Set the RGB values
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            x_part = int(x / SCALING)
            y_part = int(int(y / SCALING) * (width / SCALING))
            index = x_part + y_part

            i = population[index]
            r, g, b = i.red, i.green, i.blue
            img[y][x][0] = r
            img[y][x][1] = g
            img[y][x][2] = b

    # Save the image
    scipy.misc.imsave(img_name, img)

if __name__ == "__main__":
    main()
