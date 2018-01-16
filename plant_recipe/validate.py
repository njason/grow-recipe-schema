#!/usr/bin/env python
import os

import argparse
from lxml import etree

DEFAULT_SCHEMA = os.path.join(os.path.dirname(__file__), 'recipe.xsd')

def valid(xml_file, schema=None):

    if not schema:
        with open(DEFAULT_SCHEMA, 'r') as schema_file:
            schema_tree = etree.parse(schema_file)
            schema = etree.XMLSchema(schema_tree)

    xml_str = xml_file.read().replace('\n', '').encode('utf-8')
    parser = etree.XMLParser(schema=schema)

    etree.fromstring(xml_str, parser)

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    params = parser.parse_args()

    with open(params.file) as xml_file:
        is_valid = valid(xml_file)

    if is_valid:
        print('valid')
