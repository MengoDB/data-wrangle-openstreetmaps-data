"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET

OSMFILE = "sacramento_california3.osm"

amenity_types = set()
# UPDATE THIS VARIABLE



def is_amenity(elem):
    return (elem.attrib['k'] == "amenity")


    return name


if __name__ == '__main__':

    osm_file = ET.parse(OSMFILE)
    root = osm_file.getroot()
    for elem in root:

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_amenity(tag):
                    amenity_types.add(tag.attrib['v'])
    print amenity_types

                    
# write osm

#    osm_file.write('sacramento_california3.osm')




