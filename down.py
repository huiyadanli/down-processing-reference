# -*- coding: utf-8 -*-
# Download all the html in reference

import urllib2
from bs4 import BeautifulSoup

# down reference index page
ref_html = urllib2.urlopen("https://www.processing.org/reference/").read()
soup = BeautifulSoup(ref_html, "html.parser")
links = []
# extract ref links
urls = soup.find_all('a', attrs={'class':'ref-link'})
# save links name as txt
f = open('ref-link.txt', 'w')
for url in urls:
    links.append(url["href"])
    f.writelines(url["href"] + '\n')
f.close()

# down ever page
for i in range(len(links)):
    print str(i) + '/' + str(len(links)) + ' ' + links[i]
    base_url = "https://www.processing.org/reference/" + links[i]
    html = urllib2.urlopen(base_url).read()
    # print html
    f = open('ref/' + links[i], 'w')
    f.write(html)
    f.close()
