import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(sep='\n', *(
            ['Start : {}'.format(tag)] +
            ['-> {} > {}'.format(name, value) for name, value in attrs]
        ))

    def handle_endtag(self, tag):
        print('End   : {}'.format(tag))

    def handle_startendtag(self, tag, attrs):
        print(sep='\n', *(
            ['Empty : {}'.format(tag)] +
            ['-> {} > {}'.format(name, value) for name, value in attrs]
        ))


MyHTMLParser().feed(''.join(list(sys.stdin)[1:]))
