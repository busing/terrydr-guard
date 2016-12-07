#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ConfLoad import *
from MailSender import *
import sys
import time


options=sys.argv[1] if len(sys.argv)>1 else ""
application=sys.argv[2] if len(sys.argv)>2 else ""
key=sys.argv[3] if len(sys.argv)>3 else ""
startup=sys.argv[4] if len(sys.argv)>4 else ""
execuser=sys.argv[5] if len(sys.argv)>5 else "root"



conf = ConfLoad()

def guard():
	try:
		if len(conf.guardList)>0:
			crashList=[]
			for g in conf.guardList:
				if g.guard:
					if not g.checkAlive():
						print g.name,"is not running ,startup"
						g.startUp()
						crashList.append(g.name)
						pass
					else:
						print g.name,"is running\n"
						pass
				else:
					print "skip "+g.name

			if len(crashList) >0:
				content=""
				for name in crashList:
					content+='\napplication \"'+name+'\" is breakdown,  terrydrGuard has startup it'
				content+="\ncheck at: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
				Mail.send(content)
		else:
			print "error: no application for guard"
	except BaseException:
		content="terrydr guard occur a excetion"
		print content
		Mail.send(content)


def status():
	for g in conf.guardList:
		g.status()

def printHelp():
	print 'unknow options'
	print 'run \"python TerrydrGuard.py\" to check application at once'
	print 'run \"python TerrydrGuard.py add [name] [key] [startup_shell]\" to add application for monitor'
	print 'run \"python TerrydrGuard.py del [name]\" to delete application from monitor'
	print 'run \"python TerrydrGuard.py stopmonitor [name]\" to stop monitor application'
	print 'run \"python TerrydrGuard.py startmonitor [name]\" to start monitor application'
	print 'run \"python TerrydrGuard.py status\" to view application status'

def stopMonitor():
	if application =="":
		printHelp()
	else:
		XmlUtil.changeGuard(application,"no")

def startMonitor():
	if application =="":
		printHelp()
	else:
		XmlUtil.changeGuard(application,"yes")

def addApplication():
	if application =="" or key=="" or startup=="":
		printHelp()
	else:
		XmlUtil.addApplication(application,key,startup,"yes",execuser)

def delApplication():
	if application =="":
		printHelp()
	else:
		XmlUtil.delApplication(application)


if options=='add':
	addApplication()
elif options=='del':
	delApplication()
elif options=='status':
	status()
elif options=='stopmonitor':
	stopMonitor()
elif options=='startmonitor':
	startMonitor()
elif options=="":
	guard()
else:
	printHelp()
