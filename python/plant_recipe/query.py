from lxml import etree, objectify

from plant_recipe import validate

ROOT_NODE = 'recipe'
DEFAULT_STAGE = 'default'

class Metric:

    def __init__(self, min=None, max=None):
        self.min = min
        if self.min:
            self.min = float(self.min)

        self.max = max
        if self.max:
            self.max = float(self.max)

def find_metric_value(xml, stage, metric_type, metric_name):
    """
    Finds the specified metric in the given stage. If the metric is not
    present in the given stage, the metric is taken from the default stage
    """

    if validate.valid(xml):
        # go back to the beginning
        xml.seek(0)

        tree = etree.parse(xml)

        metric = tree.xpath('/{root}/{stage}/{metric_type}/{metric_name}'.format(
            root=ROOT_NODE, stage=stage, metric_type=metric_type,
            metric_name=metric_name))

        if not metric:
            metric = tree.xpath('/{root}/{stage}/{metric_type}/{metric_name}'.format(
                root=ROOT_NODE, stage=DEFAULT_STAGE, metric_type=metric_type,
                metric_name=metric_name))

        if not metric:
            return None

        # there should only be definition if the metric is present
        assert len(metric) == 1

        return Metric(metric[0].attrib.get('min'),
                      metric[0].attrib.get('max'))
