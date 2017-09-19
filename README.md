# terrydr-guard （泰立瑞进程守护服务）
##1.获取安装包

```
git clone https://github.com/busing/terrydr-guard.git
```
```shell
cd terrydr-guard
chmod +x build.sh
./build.sh
```
  当前目录会生成一个terrydr-guard.tar.gz的安装包

##2.安装和卸载(root 用户安装)
```shell
tar -xzvf terrydr-guard.tar.gz
cd terrydr-guard
chmod +x install.sh
./install.sh install #执行安装
./install.sh uninstall #执行卸载
```
  安装目录在:/usr/local/guard
  安装之后会自动注册到/etc/rc.local 服务器重启自动启动GuardServer服务
    
##3.GuardServer（进程守护服务）
    守护服务，每10秒钟检测一下所有配置服务，如果有没有运行的服务，执行对应的启动命令，并发送邮件通知对应的用户。
    具体的邮件配置在conf/guard.xml
   
  服务启动命令：    
```shell
guardserver > /dev/null 2>&1 &
```
    
##4.TerrydrGuard（工具，命令）
```shell
guard add tomcat tomcat "sh /usr/local/tomcat/bin/startup.sh" root #添加守护配置 [name] [key] [startup shell][exec user,default root]
guard stopmonitor tomcat #停止监控某个服务
guard startmonitor tomcat #启动监控某个服务
guard del tomcat #删除某个服务
guard status #查看所有监控服务的状态(pid)
```

##5.配置文件
```xml
<?xml version='1.0' encoding='utf-8'?>
<guard>
    <!--邮件发送服务配置-->
    <mailserver>
        <sender>xxxx@xxx.com</sender>
        <smtp>xxx.ym.163.com</smtp>
        <port>25</port>
        <password>xxxxxx</password>
    </mailserver>
    <!--程序崩溃通知邮箱, 注意如果监控的服务崩溃，无法被启动，邮件不会一直发送，间隔15分钟再次发送-->
    <reciver>xxx1@xxx.com,xxx2@xxx.com,xxx3@xxx.com</reciver>
    <application>
        <name>tomcat</name>
        <key>tomcat</key>
        <startup>sh /usr/local/tomcat/bin/startup.sh</startup>
        <!--是否守护-->
        <guard>no</guard>
        <execuser>root</execuser>
    </application>
</guard>
```
  application 节点的配置，可以用TerrydrGuard.py 工具代替，免去手工修改的麻烦
  

##6.通知邮件内容
    application "tomcat" is breakdown,  terrydrGuard has startup it
    check at: 2016-11-18 14:21:04

    [from terrydrGuard , hostname:taiyuandembp.local]
  

