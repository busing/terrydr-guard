#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import time
import os
import socket
import traceback
import urllib2
import urllib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


class Mail:

	sender = ""
	smtp = ""
	port = ""
	password = ""
	reciver = ""
	mailapi=""
	apisend=False
	sendTimePath="log/sendTime"

	@classmethod
	def send(self,content):
		try:
			subject="【Warning】some application is breakdown"
			if Mail.timeToSendMail():
				content+="\n\n[from terrydrGuard , hostname:"+socket.gethostname()+"]"
				if Mail.apisend:
					data={}
					data['toAddress']=Mail.reciver
					data['type']=0
					data['content']=content
					data['subject']=subject
					data['personal']="TerrydrGuard"
					post_data = urllib.urlencode(data)
					req=urllib2.Request(Mail.mailapi,post_data)
					response=urllib2.urlopen(req)
					s=response.read()
					print "response: %s" % s
				else:
					reciverArr=Mail.reciver.split(",")
					msg=MIMEText(content,'plain','utf-8')
					formatReciv="";
					for to in reciverArr:
						formatReciv+=","+Mail.formatAddr(to)
					msg['To']=formatReciv
					msg['From']=Mail.formatAddr(u'TerrydrGuard <%s>' % Mail.sender)
					msg['Subject']=Header(subject,"utf-8")

					server=smtplib.SMTP(Mail.smtp , int(Mail.port)) #发件人邮箱中的SMTP服务器，端口是25
					server.login(Mail.sender , Mail.password)  #括号中对应的是发件人邮箱账号、邮箱密码
					server.sendmail(Mail.sender,reciverArr,msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
					# server.quit()  #这句是关闭连接的意思

				print "send mail to",Mail.reciver
				Mail.saveSendTime()

		except Exception,e:  #如果try中的语句没有执行，则会执行下面的ret=False
			print "Error: send mail exception"
			print traceback.format_exc()


	@classmethod
	def formatAddr(self,s):
		name, addr = parseaddr(s)
		return formataddr(( \
			Header(name, 'utf-8').encode(), \
			addr.encode('utf-8') if isinstance(addr, unicode) else addr))

	@classmethod
	def saveSendTime(self):
		fo = open(Mail.sendTimePath, "wb")
		fo.write(str(time.time()))
		fo.close()

	@classmethod
	def readSendTime(self):
		if not os.path.exists(Mail.sendTimePath):
			if not os.path.exists('log'):
				os.mkdir("log")
			return 0
		else:
			fo = open(Mail.sendTimePath, "r+")
			str= fo.read()
			fo.close()
			return str

	@classmethod
	def timeToSendMail(self):
		lasttime=float(Mail.readSendTime())
		currenttime=time.time()
		if currenttime-lasttime>60*15 :#15分钟间隔
			return True
		else:
			return False

	
