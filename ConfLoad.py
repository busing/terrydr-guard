#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
from GuardBean import *
from MailSender import *
import xml.dom.minidom
import sys

class ConfLoad:

	guardList = []
	mailList = []

	def __init__(self):
		self.loadXml()

	def loadXml(self):
		domTree=xml.dom.minidom.parse(sys.path[0]+"/conf/guard.xml")
		collection=domTree.documentElement
		elements=collection.getElementsByTagName("application")
		for e in elements:
			guard= Guard()
			guard.name=self.getNodeData(e,"name")
			guard.key=self.getNodeData(e,"key")
			guard.startup=self.getNodeData(e,"startup")
			guard.guard=True if self.getNodeData(e,"guard")=="yes" else False
			self.guardList.append(guard)
			pass

		elements=collection.getElementsByTagName("mailserver")[0]
		self.loadMail(elements)
		pass

		Mail.reciver=collection.getElementsByTagName("reciver")[0].childNodes[0].data

	def loadMail(self,e):
		Mail.sender=self.getNodeData(e,'sender')
		Mail.smtp=self.getNodeData(e,'smtp')
		Mail.port=self.getNodeData(e,'port')
		Mail.password=self.getNodeData(e,'password')
		Mail.mailapi=self.getNodeData(e,'mailapi')
		Mail.apisend=True if self.getNodeData(e,"apisend")=="yes" else False
		
		pass


	def getNodeData(self,e,key):
		return e.getElementsByTagName(key)[0].childNodes[0].data
		pass
