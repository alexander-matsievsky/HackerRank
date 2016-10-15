import re
import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if not re.match(r'^\s+$', data):
            if len(data.split('\n')) == 1:
                print('>>> Single-line Comment\n{}'.format(data))
            else:
                print('>>> Multi-line Comment\n{}'.format(data))

    def handle_data(self, data):
        if not re.match(r'^\s+$', data):
            print('>>> Data\n{}'.format(data))


MyHTMLParser().feed(''.join(list(sys.stdin)[1:]))
