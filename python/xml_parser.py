"""Little bit xml-parser about."""

'''
import xml.sax

handler = xml.sax.ContentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("jill.xml")
'''
#2 Xml with DOM

import xml.dom.minidom

domtree = xml.dom.minidom.parse("jill.xml")
group = domtree.documentElement
persons = group.getElementsByTagName("person")
for person in persons:
    print("--- Person ---")
    if person.hasAttribute("id"):
        print("ID: %s" % person.getAttribute("id"))
        name = person.getElementsByTagName("name")[0]
        age = person.getElementsByTagName("weight")[0]
        weight = person.getElementsByTagName("weight")[0]
        height = person.getElementsByTagName("height")[0]
