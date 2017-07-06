#!/usr/bin/env python
"""
    Converts XML recipes to written word
"""

import argparse
import gettext

from lxml import etree, objectify

_ = gettext.gettext

def get_day_range(elem: objectify.ObjectifiedElement) -> str:
    """uses the objects min and max values and converts to a day range."""
    return '{0} to {1} days'.format(int(elem.get('min')) /60/60/24,
                                    int(elem.get('max')) /60/60/24)


def main():
    """Entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    params = parser.parse_args()

    tree = etree.parse(params.file)

    recipe = objectify.fromstring(etree.tostring(tree))

    name = recipe.stage.get('name')

    for stage in recipe.stage:
        if 'min' in stage.keys() and 'max' in stage.keys():
            print(_('The {0} stage lasts {1}'.format(name,
                                                     get_day_range(stage))))


if __name__ == '__main__':
    main()
