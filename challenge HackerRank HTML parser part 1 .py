
from html.parser import HTMLParser
class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

MyParser = MyHtmlParser()
MyParser.feed(''.join([input() for _ in range(int(input()))]))
        