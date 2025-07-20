from bs4 import BeautifulSoup
import requests

BBC = 'https://www.bbc.com/'

# Get HTML Content
r = requests.get(BBC)
soup = BeautifulSoup(r.content, 'html.parser')

# Find the Headlines
media_list = soup.find_all("h2", class_="sc-9d830f2a-3 jqQlce")

print(media_list)

headlines = media_list[0].text

# Optional ways to clean up the String
headlines = headlines.replace('  ', '')
headlines = headlines.replace('\n', '  ')

# Make a list of the Headlines
_headline_list = headlines.split('     ')

# Clean Up the List
previous = ""
for x in _headline_list:
    if x == '':
        _headline_list.remove(x)
z = 1
while z < len(_headline_list):
    if _headline_list[z] in _headline_list[z-1]:
        _headline_list.pop(z-1)
    z += 1

# Print the List with a line in between
print(len(_headline_list))
for x in _headline_list:
    print(x + "\n")
