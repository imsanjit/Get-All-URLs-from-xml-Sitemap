from lxml import etree
import requests

url_in = input("Kindly Enter sitemap url: ")

r = requests.get(url_in)
root = etree.fromstring(r.content)
print ("The number of urls are {0}".format(len(root)))
for sitemap in root:
    xmlDict = []
    children = sitemap.getchildren()
    xmlDict.append(children[0].text)
    print (xmlDict)
