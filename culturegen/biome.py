import food
import buildmat
import collections


class Biome(object):

    def __init__(self, token, template):
        self.token = token
        self.template = template
        self.food = template['foodsources']
        self.build = template['buildmats']


SWAMP_WIDTH = .5 / 6
RAINFOREST_WIDTH = 1 / 6
FOREST_WIDTH = 1.5 / 6
MARSH_WIDTH = .5 / 6
GRASS_WIDTH = 1.5 / 6
DESERT_WIDTH = 1 / 6

temporary_food_list = collections.Counter({
    food.barley: 5,
    food.rice: 4,
    food.yams: 3,
    food.apple: 2,
    food.blackberries: 1
})

temporary_building_materials = collections.Counter({
    buildmat.adobe: 5,
    buildmat.stoneblock: 4,
    buildmat.wattledaub: 3,
    buildmat.timber: 2,
    buildmat.sod: 1
})

tmpl = {
    'TUNDRA': {
        'chart_height': .2,
        'chart_width': 1,
        'rainfall': 6,
        'temperature': 1,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'BOREAL_SWAMP': {
        'chart_height': .4,
        'chart_width': SWAMP_WIDTH,
        'rainfall': 6,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'CYPRUS_SWAMP': {
        'chart_height': .2,
        'chart_width': SWAMP_WIDTH,
        'rainfall': 6,
        'temperature': 4,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'MERANTI_SWAMP': {
        'chart_height': .2,
        'chart_width': SWAMP_WIDTH,
        'rainfall': 6,
        'temperature': 5,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'BOREAL_FOREST': {
        'chart_height': .2,
        'chart_width': RAINFOREST_WIDTH + FOREST_WIDTH,
        'rainfall': 4,
        'temperature': 2,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'TEMPERATE_RAINFOREST': {
        'chart_height': .2,
        'chart_width': RAINFOREST_WIDTH,
        'rainfall': 5,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'TROPICAL_RAINFOREST': {
        'chart_height': .4,
        'chart_width': RAINFOREST_WIDTH,
        'rainfall': 5,
        'temperature': 5,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'TEMPERATE_DECIDUOUS': {
        'chart_height': .4,
        'chart_width': FOREST_WIDTH,
        'rainfall': 4,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'TROPICAL_SEASONAL': {
        'chart_height': .2,
        'chart_width': FOREST_WIDTH,
        'rainfall': 4,
        'temperature': 5,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'BOREAL_MARSH': {
        'chart_height': .2,
        'chart_width': MARSH_WIDTH,
        'rainfall': 3,
        'temperature': 2,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'SALT_MARSH': {
        'chart_height': .2,
        'chart_width': MARSH_WIDTH,
        'rainfall': 3,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'MANGROVE': {
        'chart_height': .4,
        'chart_width': MARSH_WIDTH,
        'rainfall': 3,
        'temperature': 4,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'STEPPE': {
        'chart_height': .25,
        'chart_width': GRASS_WIDTH,
        'rainfall': 2,
        'temperature': 2,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'CHAPPERAL': {
        'chart_height': .3,
        'chart_width': GRASS_WIDTH,
        'rainfall': 2,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'SAVANNA': {
        'chart_height': .25,
        'chart_width': GRASS_WIDTH,
        'rainfall': 2,
        'temperature': 4,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'COLD_DESERT': {
        'chart_height': .4,
        'chart_width': DESERT_WIDTH,
        'rainfall': 1,
        'temperature': 3,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    },
    'HOT_DESERT': {
        'chart_height': .4,
        'chart_width': DESERT_WIDTH,
        'rainfall': 1,
        'temperature': 5,
        'buildmats': temporary_building_materials,
        'foodsources': temporary_food_list
    }
}


# Load the templates into Biome instances
bdict = {}

for i in tmpl:
    bdict[i] = Biome(i, tmpl[i])
