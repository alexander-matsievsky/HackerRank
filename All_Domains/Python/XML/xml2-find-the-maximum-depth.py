import sys
from xml.etree import ElementTree


def walk(parent, level=0):
    yield (parent, level)
    for child in parent:
        for pair in walk(child, level + 1):
            yield pair


[_, *xml] = list(sys.stdin)
feed = ElementTree.fromstring(''.join(xml))
print(max(map(lambda node: node[1], walk(feed))))
