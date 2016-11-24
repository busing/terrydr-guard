#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
import commands,time,socket,os,signal,sys,logging
from logging.handlers import TimedRotatingFileHandler,RotatingFileHandler

scriptSelfName="GuardServer"
workdir=sys.path[0]

#日志打印格式
log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
formatter = logging.Formatter(log_fmt)
#创建TimedRotatingFileHandler对象
log_file_handler = TimedRotatingFileHandler(filename=workdir+"/log/"+scriptSelfName+".log", when="D", interval=1, backupCount=7)
#log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
#log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
log_file_handler.setFormatter(formatter)    
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
log.addHandler(log_file_handler)

# logging.basicConfig(
#     level    = logging.INFO,
#     format   = 'LINE %(lineno)-4d  %(levelname)-8s %(message)s',
#     datefmt  = '%m-%d %H:%M',
#     filename = workdir+"/log/"+scriptSelfName + ".log",
#     filemode = 'w');


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
		log.error('guard server is already running')
		log.error(e)
		return True

#服务启动
def startUp():
	
	# if checkAlive():
		# os._exit(0)
	log.info('GuardServer startup')
	print "GuardServer startup"
	while (True):
		if is_sigint_up:
			print "exit"
			break
		log.info("【exec TerrydrGuard】")
		s=commands.getoutput("python %s/TerrydrGuard.pyc" % sys.path[0])
		log.info(s)
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





	
