#!/usr/bin/env python

from os import path
from random import randint
import argparse
from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

tree = etree.parse(params.file)

# use XPath to query all nodes with a min attribute
for node in tree.findall('.//*[@min]'):
    node.attrib['min'] = str(randint(0, 100))

for node in tree.findall('.//*[@max]'):
    num = randint(0, 100)
    if 'min' in node.attrib:
        node.attrib['max'] = str(int(node.attrib['min']) + num)
    else:
        node.attrib['max'] = str(num)

filename, file_extension = path.splitext(params.file)
redacted_file = filename + '_REDACTED' + file_extension

tree.write(redacted_file, pretty_print=True)
