from lxml import etree
import requests
import csv


def xml_sitemap_urls(url):
    r = requests.get(url)
    if r.status_code ==200:
        root = etree.fromstring(r.content)
        print (f"The number of urls are {len(root)}\n")
        for sitemap in root:
            children = sitemap.getchildren()
            urls = children[0].text
            with open('names.csv', 'a+') as f:
                f.write(f'{urls}\n')
        return "File created"
    else:
        return "Not A valid url."
    
    
   
xml_sitemap_urls('https://www.abcd.com/sitemap.xml')
