#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:29:33 2017

@author: henryzhang

Usage: python findPerson.py -d /home/xxx/project/Training_pic
"""

import xml.etree.ElementTree as ET
import os
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Check filename label in XML')

parser.add_argument( "-d", dest="directory", action="store", type=str, required=True, 
                  help="Directory containing resources" )

options = parser.parse_args()


if not os.path.isdir(options.directory):
    print("directory (%s) doesn't exist" % options.directory)
    sys.exit(1)
    
label_path = os.path.join(options.directory, 'label')
out_path = os.path.join(options.directory, 'out')

if not os.path.isdir(out_path):
    os.mkdir(out_path)

for xml_file in os.listdir(label_path):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(label_path, xml_file)
        if not os.path.isfile(xml_path):
            print("Could not find xml file %s, skipping" % (xml_path))
            continue
        
        try:
            xml_tree = ET.parse(xml_path)
        except OSError as error:
            print('Error occurs when opening XML file:', error)
            continue
        
        hasPerson = False
        
        for node in xml_tree.iterfind('object'):
            name = node.findtext('name')
            if name == 'person':
                hasPerson = True
                break
                
        if hasPerson:
            for node in xml_tree.findall('object'):
                name = node.findtext('name')
                if name != 'person':
                    xml_tree.getroot().remove(node)
            new_xml = os.path.join(out_path, xml_file)
            xml_tree.write(new_xml, encoding="utf-8")
            hasPerson = False
        