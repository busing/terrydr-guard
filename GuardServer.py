#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import commands,time,socket,os,signal,sys,logging

scriptSelfName="GuardServer"
workdir=sys.path[0]

logging.basicConfig(
    level    = logging.INFO,
    format   = 'LINE %(lineno)-4d  %(levelname)-8s %(message)s',
    datefmt  = '%m-%d %H:%M',
    filename = workdir+"/log/"+scriptSelfName + ".log",
    filemode = 'w');


#检查是否已经启动
def checkAlive():
	try:
		# 全局属性，否则变量会在方法退出后被销毁
		global s
		s = socket.socket()
		host = socket.gethostname()
		s.bind((host, 65500))
		return False
	except BaseException , e:
		logging.error('guard server is already running')
		logging.error(e)
		return True

#服务启动
def startUp():
	
	if checkAlive():
		os._exit(0)
	logging.info('GuardServer startup')
	print "GuardServer startup"
	while (True):
		if is_sigint_up:
			print "exit"
			break
		logging.info("【exec TerrydrGuard】")
		s=commands.getoutput("python %s/TerrydrGuard.py" % sys.path[0])
		logging.info(s)
		time.sleep(10)


#ctrl+c处理
def sigint_handler(signum, frame):
	global is_sigint_up
	is_sigint_up = True


is_sigint_up = False
#注册ctrl+c
signal.signal(signal.SIGINT, sigint_handler)
#启动服务
startUp()





	
