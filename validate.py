#!/usr/bin/env python

import argparse
from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

with open('recipe.xsd', 'r') as schema_file:
    schema_tree = etree.parse(schema_file)
    schema = etree.XMLSchema(schema_tree)

with open(params.file, 'r') as xml_file:
    xml_str = xml_file.read().replace('\n', '')

parser = etree.XMLParser(schema=schema)
etree.fromstring(xml_str, parser)

print('valid')
