import sys
from xml.etree import ElementTree

[_, *xml] = list(sys.stdin)
feed = ElementTree.fromstring(''.join(xml))
print(sum(len(node.attrib) for node in feed.iter()))
