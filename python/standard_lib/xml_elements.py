"""Parse podcasts.opml."""

# need testing and keep other .xml file

#1 make parse

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

print(tree)


#2 check all nodes of tree

from xml.etree import ElementTree
import pprint

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for noe in tree.iter():
    print(node.tag)

#3 show feed urls

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    name = node.attrib.get('text')
    url = node.attrib.get('xmlUrl')
    if name and url:
        print('  %s' % name)
        print('    %s' % url)
    else:
        print(name)

#4 find feeds by tag

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.findall('.//outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print(url)

#5 find feeds by structure

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print(url)

#6 for data.xml node attributes

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('./with_attributes')
print(node.tag)
for name, value in sorted(node.attrib.items()):
    print('  %-4s = "%s"' % (name, value))

#7 tail text

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for path in ['./child', './child_with_tail']:
    node = tree.find(path)
    print(node.tag)
    print('  child node text:', node.text)
    print('  and tail text  :', node.tail)

#8 entity references

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('entity_expansion')
print(node.tag)
print('  in attribute:', node.attrib['attribute'])
print('  in text     :', node.text.strip())

#9 show all events

from xml.etree.ElementTree import iterparse

depth = 0
prefix_width = 8
prifix_dots = '.' * prefix_width
line_template = ''.join([
    '{prifix:<0.{prefix_len}}',
    '{event:<8}',
    '{suffix:<{suffix_len}}',
    '{node.tag:<12}',
    '{node_id}',
])

EVENT_NAMES = ['start', 'end', 'start-ns','end-ns']

for (event, node) in iterparse('podcasts.opml', EVENT_NAMES):
    if event == 'end':
        depth -= 1

    prefix_len = depth * 2

    print(line_template.format(
        prefix=prefix_dots,
        prefix_len=prefix_len,
        suffix='',
        suffix_len=(prefix_width - prefix_len),
        node=node,
        node_id=id(node),
        event=event,
    ))

    if event == 'start':
        depth += 1

#10 for csv

import csv
from xml.etree.ElementTree import iterparse
import sys

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

group_name = ''

parsing = iterparse('podcasts.opml', events=['start'])

for (event, node) in parsing:
    if node.tag != 'outline':
        continue
    if not node.attrib.get('xmlUrl'):
        group_name = node.attrib['text']
    else:
        writer.writerow(
                (group_name, node.attrib['text'],
                    node.attrib['xmlUrl'],
                    node.attrib.get('htmlUrl', ''))
    )

#11 scv truebuilder

import csv
import io
from xml.etree.ElementTree import XMLParser
import sys


class PodcastListToCSV(object):

    def __init__(self, outputFile):
        self.writer = csv.writer(
                outputFile,
                quoting=csv.QUOTE_NONNUMERIC,
        )
        self.group_name = ''

    def start(self, tag, attrib):
        if tag != 'outline':
            return
        if not attrib.get('xmlUrl'):
            self.group_name = attrib['text']
        else:
            self.writer.writerow(
                    (self.group_name,
                     attrib['text'],
                     attrib['xmlUrl'],
                     attrib.get('htmlUrl', ''))
            )

    def end(self, tag):
        "Ignore closing tags"

    def data(self, data):
        "Ignore data inside nodes"

    def close(self):
        "Nothing special to do here"


target = PodcastListToCSV(sys.stdout)
parser = XMLParser(target=target)
with open('podcasts.opml', 'rt') as f:
    for line in f:
        parser.feed(line)
parser.close()

#12 xml

from xml.etree.ElementTree import XML

def show_node(node):
    print(node.tag)
    if node.text is not None and node.text.strip():
        print('  text: "%s"' % node.text)
    if node.tail is not None and node.tail.strip():
        print('  tail: "%s"' % node.tail)
    for name, value in sorted(node.attrib.items()):
        print('  %-4s = "%s"' % (name, value))
    for child in node:
        show_node(child)

parsed = XML('''
        <root>
            <group>
              <child id="a">This is child "a".</child>
              <child id="b">This is child "b".</child>
            </group>
            <group>
              <child id="c">This is child "c".</child>
            </group>
        </root>
''')

print('parsed =', parsed)

for elem in parsed:
    show_node(elem)

#13 xmlid

from xml.etree.ElementTree import XMLID

tree, id_map = XMLID('''
<root>
  <group>
    <child id="a">This is child "a".</child>
    <child id="b">This is child "b".</child>
  </group>
  <group>
    <child id="c">This is child "c".</child>
  </group>
</root>
''')

for key, value in sorted(id_map.items()):
    print('%s = %s' % (key, value))

#14 create document

from xml.etree.ElementTree import (
        Element, SubElement, Comment, tostring,
)

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print(tostring(top))

#15 put it code on the file ElementTree_pretty.py

from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return pretty xml-string for Element obj."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

#16 ElementTree_create_pretty.py

from xml.etree.ElementTree import Element, SubElement, Comment

from ElementTree_pretty import prettify

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')

child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

print(prettify(top))

#17 ElementTree_csv_to_xml.py

import csv
from xml.etree.ElementTree import (
        Element, SubElement, Comment, tostring,
)
import datetime
from ElementTree_pretty import prettify

generated_on = str(datetime.datetime.now())

# Configurate one athribute with set() method
root = Element('opml')
root.set('version', '1.0')

root.append(
        Comment('Generated by ElementTree_csv_to_xml.py for PyMOTW')
)

head = SubElement(root, 'head')
title = SubElement(head, 'title')
title.text = 'My Podcasts'
dc = SubElement(head, 'dateCreated')
dc.text = generated_on
dm = SubElement(head, 'dateModified')
dm.text = generated_on

body = SubElement(root, 'body')

with open('podcasts.csv', 'rt') as f:
    current_group = None
    reader = csv.reader(f)
    for row in reader:
        group_name, podcast_name, xml_url, html_url = row
        if (current_group is None or
                group_name != current_group.text):
            # Start new group
            current_group = SubElement(
                    body, 'outline',
                    {'text': group_name},
            )
        # Add podcast into group and set attributes
        podcast = SubElement(
                current_group, 'outline',
                {'text': podcast_name,
                 'xmlUrl': xml_url,
                 'htmlUrl': html_url},
        )

print(prettify(root))

#18 ElementTree_extend.py

from xml.etree.ElementTree import Element,tostring
from ElementTree_pretty import prettify

top = Element('top')

children = [
        Element('child', num=str(i))
        for i in range(3)
]

top.extend(children)

print(prettyfy(top))

#19 ElementTree_extend_node.py

from xml.etree.ElementTree import (
        Element, SubElement, tostring, XML,
)
from ElementTree_pretty import prettify

top = Element('top')

parent = SubElement(top, 'parent')

children = XML(
        '<root><child num="0" /><child num="1" />'
        '<child num="2" /></root>'
)
parent.extend(children)

print(prettify(top))

#20 ElementTree_extend_node_copy.py

from xml.etree.ElementTree import (
        Element, SubElement, tostring, XML,
)
from ElementTree_pretty import prettify

top = Element('top')

parent_a = SubElement(top, 'parent', id='A')
parent_b = SubElement(top, 'parent', id='B')

# make a doughters nodes
children = XML(
        '<root><child num="0" /><child num="1" />'
        '<child num="2" /></root>'
)

# check dublicates
for c in children:
    c.set('id', str(id(c)))


# add node into first parent node
parent_a.extend(children)

print('A:')
print(prettify(top))
print()

#21 ElementTree_write.py

import io
import sys
from xml.etree.ElementTree import (
        Element, SubElement, Comment, ElementTree,
)

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'

child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

empty_child = SubElement(top, 'empty_child')

ElementTree(top).write(sys.stdout.buffer)

#22 ElementTree_write_method.py

import io
import sys
from xml.etree.ElementTree import (
        Element, SubElement, ElementTree,
)

top = Element('top')

child = SubElement(top, 'child')
child.text = 'Contains text.'

empty_child = SubElement(top,'empty_child')

for method in ['xml', 'html', 'text']:
    print(method)
    sys.stdout.flush()
    ElementTree(top).write(sys.stdout.buffer, method=method)
    print('\n')
