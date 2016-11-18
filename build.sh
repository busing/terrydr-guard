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
	mkdir build
	cp * build

	#删除不需要的文件
	rm build/*.pyc
	rm -r build/log/
	rm build/build.sh
	rm build/conf/guard.xml

	#恢复配置文件
	mv build/conf/guard.xml.default build/conf/guard.xml
	tar -xzvf terrydr-guard.tar.gz build/* 
}

package