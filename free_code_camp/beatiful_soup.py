
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page1.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag) -> <a href="http://www.dr-chuck.com/page2.htm">
    # Second Page</a>
    print(tag.get('href', None))







