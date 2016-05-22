# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup

# ! please run down.py and generate ref-link.txt before run this py

# get reference name
f = open('ref-link.txt', 'r')
links = []
for line in f.readlines():
    links.append(line.replace('\n', ''))
f.close()

# process every html doc
for i in range(len(links)):
    print str(i) + '/' + str(len(links)) + ' ' + links[i]
    f = open('ref/' + links[i], 'r')
    html = f.read()
    f.close()
    # get table
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table').prettify()
    table = str(table).replace("<kbd>","")
    table = table.replace("</kbd>","")
    # save
    f = open('ref_table/' + links[i], 'w')
    f.write(table)
    f.close()