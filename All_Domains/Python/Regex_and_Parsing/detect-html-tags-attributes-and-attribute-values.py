import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(sep='\n', *(
            [tag] +
            ['-> {} > {}'.format(name, value) for name, value in attrs]
        ))

    def handle_startendtag(self, tag, attrs):
        print(sep='\n', *(
            [tag] +
            ['-> {} > {}'.format(name, value) for name, value in attrs]
        ))


MyHTMLParser().feed(''.join(list(sys.stdin)[1:]))
