#!/usr/bin/env python

import argparse
import gettext

from lxml import etree, objectify

_ = gettext.gettext

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

tree = etree.parse(params.file)

recipe = objectify.fromstring(etree.tostring(tree))

name = recipe.stage.get('name')

print(_('During the {0} stage....'.format(name)))
