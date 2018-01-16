from lxml import etree

from plant_recipe import constants, validate


class Metric:

    def __init__(self, min_value=None, max_value=None):
        self.min = min_value
        if self.min:
            self.min = float(self.min)

        self.max = max_value
        if self.max:
            self.max = float(self.max)


def find_metric_value(xml, stage, topic, metric):
    """
    Finds the specified metric in the given stage. If the metric is not
    present in the given stage, the metric is taken from the default stage
    """

    if validate.valid(xml):
        # go back to the beginning
        xml.seek(0)

        tree = etree.parse(xml)

        value = tree.xpath('/{root}/{stage}/{topic}/{metric}'
                           .format(root=constants.ROOT_NODE, stage=stage,
                                   topic=topic, metric=metric))

        if not value:
            value = tree.xpath('/{root}/{stage}/{topic}/{metric}'.format(
                root=constants.ROOT_NODE,
                stage=constants.Stages.DEFAULT.value, topic=topic,
                metric=metric))

        if not value:
            return None

        # there should only be definition if the metric is present
        assert len(value) == 1

        return Metric(value[0].attrib.get('min'),
                      value[0].attrib.get('max'))
