import biomegraph
import random


class Civilization(object):
    BIOME_COUNT = 3
    RESOURCE_COUNT = 2

    def __init__(self):
        self.biome_list = biomegraph.random_biome_set(self.BIOME_COUNT)
        self.food = self.rand_res(
            biomegraph.food_list(self.biome_list), self.RESOURCE_COUNT)
        self.build = self.rand_res(
            biomegraph.build_list(self.biome_list), self.RESOURCE_COUNT)

    def rand_res(self, res_list, how_many):
        result = list()
        for i in range(how_many):
            result.append(random.choice(res_list.elements()))
        return result

    def print_civ(self):

        print("Biomes:", self.biome_list)
        print("Food:", self.food)
        print("Building Materials:", self.build)


the_civ = Civilization()
the_civ.print_civ()
