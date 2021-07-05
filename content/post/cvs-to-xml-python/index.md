---
title: "csv to xml via python"
date: "2008-04-15"
categories: 
  - "professional"
  - "python"
tags: 
  - "python"
---

Today at work our [main Flash developer](http://arpitonline.com) asked me about expanding his skills and learning either Ruby or Python. My personal preference is towards python but ruby has its place. Flash is really doing well in the Java/Enterprise space lately so I went that way.

Most of the Flash backend in our work is xml based so XML was on my mind anyway. Recently we needed to mock up a xml data data file for a project while the real APIs are being completed. We had the data in a csv file so we asked some developers to whip up a xml file.

As I started writing up the ticket I started thinking it would be easier to just do it myself.

Given the speed of python development I was right!.

#!/usr/bin/env python
"""
cvs2xml.py

Created by Aaron Held on 2008-04-11.
Make the xml from the csv using dom and other three letter acronyms
"""import sys,os
import unittes
import csv

from pprint import pprint
import xml.etree.ElementTree as ET

class Cvs2xml:
    def loadCSV(self):
        """Load the data and return a list of maps"""
reader = csv.DictReader(open(r"input.csv",'r'))
        rows = \[\]
for row in reader:
            rows.append(row)
return rows

def mappings(self):
        """
        Map csv file to xml field names
        """
mapping = { 'id':"store\_number"
        return mapping

def createXML(self,listofrows):
"""Turn lists into xml
"""
root = ET.Element("stores")
for row in listofrows:
store = ET.SubElement(root, "store")
for xml\_field in row.keys():
csv\_field = self.mappings().get(xml\_field,xml\_field)
ET.SubElement(store, xml\_field).text = row.get(csv\_field,"")
print(ET.tostring(root))
#tree = ET.ElementTree(root)
#tree.write("output.xml")

class Cvs2xmlTests(unittest.TestCase):
def setUp(self):
pass

def testRun(self):
'''Lazy way of main()'''
cvs2xml = Cvs2xml()
rows = cvs2xml.loadCSV()
cvs2xml.createXML(rows)

if \_\_name\_\_ == '\_\_main\_\_':
unittest.main()
