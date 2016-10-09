#!/usr/bin/env python

import os
import json
import argparse

import dicttoxml

parser = argparse.ArgumentParser()
parser.add_argument('file')

params = parser.parse_args()

with open(params.file) as file:
    dict = json.load(file)

xml = dicttoxml.dicttoxml(dict, custom_root='recipe')

print xml
