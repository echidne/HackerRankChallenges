"""
Detect HTML Tags, Attributes and Attribute Values
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
MyParser = MyHTMLParser()
MyParser.feed(''.join([input() for _ in range(int(input()))]))
