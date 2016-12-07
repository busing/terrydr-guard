#!/usr/bin/python
# -*- coding=utf-8 -*-
import xml.etree.ElementTree as et
import xml.dom.minidom as minidom
import sys

xmlFile=sys.path[0]+"/conf/guard.xml"
tree=et.parse(xmlFile)
root=tree.getroot()

#添加守护程序
def addApplication(application,key ,startup,guard,execuser):
	appEl=getAppNodeByAppName(application)
	if appEl == None:
		eApplication=et.SubElement(root,"application")

		eName=et.SubElement(eApplication,"name")
		eName.text=application

		eKey=et.SubElement(eApplication,"key")
		eKey.text=key

		eStartup=et.SubElement(eApplication,"startup")
		eStartup.text=startup

		eGuard=et.SubElement(eApplication,"guard")
		eGuard.text=guard

		eExecuser=et.SubElement(eApplication,"execuser")
		eExecuser.text=execuser
		saveFile()
	else:
		print "application \"%s\" is already exists,del it first" % application



#删除守护程序
def delApplication(name):
	appEl=getAppNodeByAppName(name)
	if appEl ==None:
		print "can not find application \"%s\",please check application name and try again" % name
	else:
		root.remove(appEl)
		saveFile()


#修改是否守护
def changeGuard(name,guard):
	appEl=getAppNodeByAppName(name)
	appEl.find("guard").text=guard
	saveFile()


#根据名称获xml节点
def getAppNodeByAppName(appName):
	for app in root.findall("application"):
		name=app.find("name").text
		if name==appName:
			return app


def saveFile():
	indent(root)
	tree=et.ElementTree(root)
	tree.write(xmlFile, encoding="utf-8",xml_declaration=True,method="xml")

def indent(elem, level=0):
	i = "\n" + level*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			indent(elem, level+1)
			if not elem.tail or not elem.tail.strip():
				elem.tail = i
			else:
				if level and (not elem.tail or not elem.tail.strip()):
					elem.tail = i



