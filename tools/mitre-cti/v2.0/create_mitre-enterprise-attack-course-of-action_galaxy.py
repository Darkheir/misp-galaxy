#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s courses-of-action.\nMust be in the mitre/cti/entreprise-attack/course-of-action folder')
parser.add_argument("-v", "--version", type=int, required=True, help="Version of the galaxy. Please increment the previous one")
args = parser.parse_args()

values = []

for element in os.listdir('.'):
    if element.endswith('.json'):
        with open(element) as json_data:
            d = json.load(json_data)
            json_data.close()

            temp = d['objects'][0]

            value = {}
            value['description'] = temp['description']
            value['value'] = temp['name']
            value['uuid'] = re.search('--(.*)$', temp['id']).group(0)[2:]
            values.append(value)

galaxy = {}
galaxy['name'] = "Entreprise Attack - Course of Action"
galaxy['type'] = "mitre-entreprise-attack-course-of-action"
galaxy['description'] = "ATT&CK Mitigation"
galaxy['uuid' ] = "fb5a36c0-1707-11e8-81f5-d732b22a4982"
galaxy['version'] = args.version
galaxy['icon'] = "chain"

cluster = {} 
cluster['name'] = "Entreprise Attack - Course of Action"
cluster['type'] = "mitre-entreprise-attack-course-of-action"
cluster['description'] = "ATT&CK Mitigation"
cluster['version'] = args.version
cluster['source'] = "https://github.com/mitre/cti"
cluster['uuid' ] = "fb870a6a-1707-11e8-b548-17523e4d0670"
cluster['authors'] = ["MITRE"]
cluster['values'] = values

with open('generate/galaxies/mitre-entreprise-attack-course-of-action.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre-entreprise-attack-course-of-action.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
