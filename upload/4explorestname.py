__author__ = 'elsieyao'

import xml.etree.ElementTree as ET
import pprint
import re
import collections
import pickle

osm_file = open('sacramento_california2.osm', 'r')

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
street_types = collections.defaultdict(set)

expected = ['Street', 'Avenue', 'Boulevard', 'Drive', 'Court', 'Place', 'Plaza', 'Parkway']

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key = lambda s: s.lower())
    for k in keys:
        v = d[k]
        print '%s: %d' % (k, v)


def is_street_name(elem):
    return (elem.attrib['k'] == 'addr:street')

def audit():
    for event, elem in ET.iterparse(osm_file, events=('start',)):
        if elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    pprint.pprint(dict(street_types))


if __name__ == '__main__':
    audit()
    with open('streetname2.txt', 'wb') as f:
        pickle.dump(street_types, f)