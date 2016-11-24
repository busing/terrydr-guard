#正常日志打印
log(){
	echo "$1"
}

#错误日志打印
logError(){
	echo -e "\033[31m$1\033[0m" 
}

#警告日志打印
logWarn(){
	echo -e "\033[33m$1\033[0m" 
}

#成功日志打印
logSucc(){
	echo -e "\033[32m$1\033[0m"
}


package()
{
	#检查目录
	if [ -d terrydr-guard ]
	then
		rm -r terrydr-guard
	fi
	#创建目录
	mkdir terrydr-guard
	python -m compileall .
	
	#copy 文件到build目录
	rsync -av --exclude  terrydr-guard *  terrydr-guard

	rm terrydr-guard/*.py
	#删除不需要的文件
	#编译代码
	rm terrydr-guard/*.tar.gz


	if [ -d terrydr-guard/log ]
	then
		rm -r terrydr-guard/log/*
	fi
	rm terrydr-guard/build.sh
	rm terrydr-guard/conf/guard.xml

	#恢复配置文件
	mv terrydr-guard/conf/guard.xml.default terrydr-guard/conf/guard.xml

	#打包
	tar -czvf terrydr-guard.tar.gz terrydr-guard/

	#清除目录
	rm -r terrydr-guard
}

package