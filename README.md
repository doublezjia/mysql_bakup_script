# mysql_bakup_script
python mysql bakup script

环境：python 3.x 
使用类库 os sys time datetime pymysql
因为这里用的是python3.x 所以要用pymysql来连接Mysql
pymysql 是第三方的库，所以要先安装 ，可通过 pip install pymysql 进行安装

使用前先根据实际修改mysql的bin目录 备份文件目录和脚本的日志存放的目录
如果没有这个文件夹的请新建好文件夹

请对下面的数据库的用户名等变量进行修改
mysql地址 端口 用户名 密码 数据库 数据库编码 备份文件名和目录
localhost = 'localhost'
port = 3306
mysqluser = 'root'
mysqlpwd = 'root'
mysqldatabase = 'test'
charset = 'utf8'

目录变量如下，请根据实际修改这几个地方
mysql bin目录 
mysqldir = r'D:/Program Files/phpStudy/MySQL/bin'
备份文件目录
bakupfiledir = r'F:\mysqlbakup'
脚本的日志目录
logdir=r'C:\Users\yw0682\Desktop\mysql_bakup_script\log'


注意：这里的MySQLdump只备份本地数据库，如果要远程等的请修改 mysqlbakup 变量

ver 1.0 2017-08-23
All right reserved by zealous

