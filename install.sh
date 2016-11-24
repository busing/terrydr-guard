#jdk安装目录
install_path="/usr/local/guard"
profile="/etc/rc.local"


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


##检测是否安装
check()
{
	log "check terrydr guard ……"
	if [ -d $install_path ] 
	then
		return 0
	else
		return 1
	fi
}

##安装
instal()
{
	check
	checkFlag=$?
	if [ $checkFlag -eq 1 ]
	then
		logWarn "terrydr guard is not installed"
		log "start install……"
		log "extract files"
		mkdir -p $install_path
		log "copy files "
		cp -r * $install_path
		rm $install_path/install.sh
		reconf
		logSucc "terrydr guard has bean installed to $install_path"
		logSucc "'python ${install_path}/GuardServer.pyc &' to start up guard"
		# logSucc "start up GuardServer"
	else
		logError "terrydr guard is installed ,uninstall first"
	fi
}

##卸载
uninstall()
{
	check
	checkFlag=$?
	if [ $checkFlag -eq 1 ]
	then
		logError "terrydr guard is not installed"
	else
		logWarn "uninstall……"
		clearconf
		rm -rf $install_path
		logSucc "uninstalled"
	fi
}

##清除配置
clearconf()
{
	#清理已有配置
	sed -i '/. \/etc\/profile/'d $profile
	sed -i '/python \/usr\/local\/guard\/GuardServer.pyc/'d $profile
	sed -i '/exit 0/'d $profile

}


##重新配置文件
reconf()
{
	log "config file"
	#清理已有配置
	clearconf
	#添加新配置 追加配置
	echo '. /etc/profile' >> $profile
	echo 'python /usr/local/guard/GuardServer.pyc &' >> $profile
	echo 'exit 0' >> $profile
}

##命令入口
init()
{
	option=$1
	# log $option
	if [ "$option" == 'install' ]
	then
		instal
	elif [ "$option" == 'uninstall' ]
	then
		uninstall
	elif [ "$option" == 'reconf' ]
	then
		reconf
	else
		logError "unknow options"
		logWarn "install.sh install to install terrydr guard"
		logWarn "install.sh uninstall to uninstall terrydr guard"
		logWarn "install.sh reconf to reconf terrydr guard"
	fi
}

init $1
