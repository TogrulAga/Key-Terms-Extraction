from lxml import etree


for child in etree.fromstring(input()):
    print(child.text)
