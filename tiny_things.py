#!/usr/bin/env python3
# A program to check the status of the ever unreliable Arran-Broddick ferry
# I made it because I was sick of having to navigate the website several times a day

import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.calmac.co.uk/service-status?route=05')
soup = BeautifulSoup(req.content, 'html.parser')

useful = soup.find('h3', class_='heading')

print((useful.contents)[0])

############################################

#!/usr/bin/env python3
# For faster yotube searches from command line
# use ./yt.py <search_term> from terminal window
# or ./yt to search using current clipboard

import sys, pyperclip, webbrowser

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyperclip.paste()

webbrowser.open('https://youtube.com/results?search_query=' + search)
