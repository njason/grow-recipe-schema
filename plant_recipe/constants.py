from enum import Enum


# the root node in the XML structure
ROOT_NODE = 'recipe'


class Stages(Enum):
    DEFAULT = 'default'
    GERMINATION = 'germination'
    VEGETATIVE = 'vegetative'
    FLOWERING = 'flowering'
    FRUITING = 'fruiting'


class Topics(Enum):
    AIR = 'air'
    WATER = 'water'
    LIGHT = 'light'


class Metrics(Enum):
    TEMPERATURE = 'temperature'
    HUMIDITY = 'relative-humidity'
    EC = 'electro-conductivity'
    OXYGEN = 'dissolved-oxygen'
    OXIDIZING_REDUCTION_POTENTIAL = 'oxidizing-reduction-potential'
    HARDNESS = 'hardness'
    PH = 'ph'
    VPD = 'vpd'
    BICARBONATE = 'bicarbonate'
    NITROGEN = 'nitrogen'
    POTASSIUM = 'potassium'
    CALCIUM = 'calcium'
    MAGNESIUM = 'magnesium'
    SULFER = 'sulfer'
    IRON = 'iron'
    COPPER = 'copper'
    ZINC = 'zinc'
    MANGANESE = 'manganese'
    SODIUM = 'sodium'
    BORON = 'boron'
    CHLORINE = 'chlorine'
    SILICON = 'silicon'
    IRON_CHELATES = 'iron-chelates'
    SODIUM_CHLORIDE = 'sodium-chloride'
