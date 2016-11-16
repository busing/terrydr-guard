#!/usr/bin/python
# -*- coding: UTF-8 -*-

import commands
import XmlUtil

class Guard:
	name = ""
	key = ""
	startup = ""
	guard=""

	#检查是否存活
	def checkAlive(self):
		# print "check",self.name,"is alive"
		output= commands.getoutput("ps -ef|grep %s|grep -v grep|awk \'{print $2}\'" % (self.key))
		if output.strip():
			return True
		else:
			return False

	#执行启动脚本
	def startUp(self):
		(status,output)= commands.getstatusoutput(self.startup)
		print (status,output)
		print "startup",self.name

	#获取程序状态
	def status(self):
		output= commands.getoutput("ps -ef|grep %s|grep -v grep|awk \'{print $2}\'" % (self.key))
		print "["+output+"]\t"+ self.name +"\t"+("monitor" if self.guard else "stopmonitor")

