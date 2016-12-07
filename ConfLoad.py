#!/usr/bin/python
# -*- coding: UTF-8 -*-

from GuardBean import *
from MailSender import *
import xml.etree.cElementTree as ET
import sys

class ConfLoad:

	guardList = []
	mailList = []

	def __init__(self):
		self.loadXml()

	def loadXml(self):
		domTree=ET.ElementTree(file=sys.path[0]+"/conf/guard.xml")
		root=domTree.getroot()

		for e in root.iterfind("application"):
			guard= Guard()
			guard.name=self.getNodeData(e,"name")
			guard.key=self.getNodeData(e,"key")
			guard.startup=self.getNodeData(e,"startup")
			guard.execuser=self.getNodeData(e,"execuser")
			guard.guard=True if self.getNodeData(e,"guard")=="yes" else False
			self.guardList.append(guard)
			pass

		e=self.getNode(root,"mailserver")
		self.loadMail(e)
		pass

	def loadMail(self,e):
		Mail.sender=self.getNodeData(e,'sender')
		Mail.smtp=self.getNodeData(e,'smtp')
		Mail.port=self.getNodeData(e,'port')
		Mail.password=self.getNodeData(e,'password')
		Mail.mailapi=self.getNodeData(e,'mailapi')
		Mail.apisend=True if self.getNodeData(e,"apisend")=="yes" else False
		Mail.reciver=self.getNodeData(e,'reciver')
		
		pass


	def getNodeData(self,e,key):
		for elem in e.iterfind(key):
			return elem.text
		pass

	def getNode(self,e,key):
		for elem in e.iterfind(key):
			return elem
		pass
