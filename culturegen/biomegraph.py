import networkx as nx
import random
import biome
import collections


class BiomeGraph(nx.Graph):
    BIOME_DICT = biome.bdict

    edge_pairs = (
        ('TUNDRA', 'BOREAL_SWAMP'),
        ('TUNDRA', 'BOREAL_FOREST'),
        ('TUNDRA', 'STEPPE'),
        ('TUNDRA', 'COLD_DESERT'),
        ('BOREAL_FOREST', 'TEMPERATE_RAINFOREST'),
        ('BOREAL_FOREST', 'TEMPERATE_DECIDUOUS'),
        ('TEMPERATE_RAINFOREST', 'TROPICAL_RAINFOREST'),
        ('TEMPERATE_DECIDUOUS', 'TROPICAL_SEASONAL'),
        ('STEPPE', 'CHAPPERAL'),
        ('CHAPPERAL', 'SAVANNA'),
        ('COLD_DESERT', 'HOT_DESERT'),
        ('BOREAL_SWAMP', 'BOREAL_FOREST'),
        ('BOREAL_SWAMP', 'STEPPE'),
        ('BOREAL_FOREST', 'STEPPE'),
        ('BOREAL_FOREST', 'BOREAL_MARSH'),
        ('BOREAL_MARSH', 'STEPPE'),
        ('STEPPE', 'COLD_DESERT'),
        ('BOREAL_SWAMP', 'TEMPERATE_RAINFOREST'),
        ('BOREAL_SWAMP', 'TEMPERATE_DECIDUOUS'),
        ('TEMPERATE_RAINFOREST', 'TEMPERATE_DECIDUOUS'),
        ('TEMPERATE_RAINFOREST', 'SALT_MARSH'),
        ('TEMPERATE_DECIDUOUS', 'STEPPE'),
        ('TEMPERATE_DECIDUOUS', 'CHAPPERAL'),
        ('TEMPERATE_DECIDUOUS', 'SALT_MARSH'),
        ('SALT_MARSH', 'STEPPE'),
        ('SALT_MARSH', 'CHAPPERAL'),
        ('CHAPPERAL', 'COLD_DESERT'),
        ('CHAPPERAL', 'HOT_DESERT'),
        ('CYPRUS_SWAMP', 'TROPICAL_RAINFOREST'),
        ('CYPRUS_SWAMP', 'TROPICAL_SEASONAL'),
        ('CYPRUS_SWAMP', 'TEMPERATE_DECIDUOUS'),
        ('TROPICAL_RAINFOREST', 'TEMPERATE_DECIDUOUS'),
        ('TROPICAL_RAINFOREST', 'MANGROVE'),
        ('TEMPERATE_DECIDUOUS', 'MANGROVE'),
        ('MANGROVE', 'CHAPPERAL'),
        ('MANGROVE', 'SAVANNA'),
        ('SAVANNA', 'HOT_DESERT'),
        ('MERANTI_SWAMP', 'TROPICAL_RAINFOREST'),
        ('MERANTI_SWAMP', 'TROPICAL_SEASONAL'),
        ('TROPICAL_SEASONAL', 'MANGROVE'),
        ('TROPICAL_SEASONAL', 'SAVANNA'))

    def __init__(self):
        super().__init__()

        for the_biome in self.BIOME_DICT:
            self.add_node(the_biome)

        for a, b in self.edge_pairs:
            self.add_edge(self.BIOME_DICT[a], self.BIOME_DICT[b])

    def neighbors_subgraph(self, node_list):
        '''subgraph including node_list and ANY neighbors

        this function returns a subgraph of itself, consisting
        of the nodes in node_list AND any node that is a neighbor
        of ANY of them.'''

        neighbors = list()
        for node in node_list:
            neighbors.append(nx.all_neighbors(self, node))

        return nx.subgraph(self, neighbors)

    def select_random_biome(self, adj_list=list()):
        if adj_list:
            the_graph = self.neighbors_subgraph(adj_list)
        else:
            the_graph = self

        return random.choice(nx.nodes(the_graph))


bgraph = BiomeGraph()

# =============================================
# PUBLIC INTERFACE FUNCTIONS
# =============================================


def random_biome(seed_nodes=list()):
    global bgraph
    return bgraph.select_random_biome(seed_nodes)


def random_biome_set(count):

    biome_list = list()
    next_biome = None

    for i in range(count):
        next_biome = random_biome(list((biome_list)))
        biome_list.append(next_biome)

    return biome_list


def multibiome_res_list(biome_list, var_name, exc_list=None):
    print('biome_list', biome_list)
    res_list = collections.Counter()
    for i in biome_list:
        res_list += biome_list[i].var_name

    if exc_list:
        for i in exc_list:
            if i in res_list:
                res_list.remove(i)

    return res_list


def food_list(biome_list, exc_list=None):
    return multibiome_res_list(biome_list, 'food', exc_list)


def build_list(biome_list, exc_list=None):
    return multibiome_res_list(biome_list, 'build', exc_list)
