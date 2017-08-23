# 环境：python 3.x 
# 使用类库 os sys time datetime pymysql
# 因为这里用的是python3.x 所以要用pymysql来连接Mysql
# pymysql 是第三方的库，所以要先安装 ，可通过 pip install pymysql 进行安装
#
# 使用前先根据实际修改mysql的bin目录 备份文件目录和脚本的日志存放的目录
# 如果没有这个文件夹的请新建好文件夹
#
# 请对下面的数据库的用户名等变量进行修改
# mysql地址 端口 用户名 密码 数据库 数据库编码 备份文件名和目录
# localhost = 'localhost'
# port = 3306
# mysqluser = 'root'
# mysqlpwd = 'root'
# mysqldatabase = 'test'
# charset = 'utf8'
#
#
# 目录变量如下，请根据实际修改这几个地方
# mysql bin目录 
# mysqldir = r'D:/Program Files/phpStudy/MySQL/bin'
# 备份文件目录
# backupfiledir = r'F:\mysqlbakup'
# 脚本的日志目录
# logdir=r'C:\Users\yw0682\Desktop\mysql_bakup_script\log'
#
#
# 注意：这里的MySQLdump只备份本地数据库，如果要远程等的请修改 mysqlbakup 变量
#
#
# ver 1.0 2017-08-23
# All right reserved by zealous
#
#

import os,sys,time,datetime,pymysql

# 文件目录
# mysql bin目录 
mysqldir = r'D:/Program Files/phpStudy/MySQL/bin'
# 备份文件目录
backupfiledir = r'F:\mysqlbakup'
# 脚本的日志目录
logdir=r'C:\Users\yw0682\Desktop\mysql_backup_script\log'


# 获取时间 用于下面函数的判断删除是否为一个月以上的文件
#取得当前时间
today=datetime.datetime.now()
#定义一个月前
one_month=datetime.timedelta(days=30)
#获取一个月前的日期
one_month_ago=today - one_month
#把日期转为timestamps类型
one_month_ago_timestamps=time.mktime(one_month_ago.timetuple())

# mysql地址 端口 用户名 密码 数据库 数据库编码 备份文件名和目录
localhost = 'localhost'
port = 3306
mysqluser = 'root'
mysqlpwd = 'root'
mysqldatabase = 'phptest'
charset = 'utf8'

# 备份文件名
backupfile_name = mysqldatabase+'-'+today.strftime('%Y-%m-%d')+'.sql'
backupfile = backupfiledir+'\\'+ backupfile_name

# 用mysqldump 备份
mysqlbakup = 'mysqldump -u'+mysqluser+' -p'+mysqlpwd+' --flush-logs '+mysqldatabase+' > '+backupfile


# 日志目录和日志内容
backup_logfile = logdir+'\Backup_log.log'
remove_logfile = logdir+'\Remove_log.log' 
error_logfile = logdir+'\error_log.log'




# mysql数据库连接，用来判断数据库是否能连接上，避免备份出错
def mysql_con():
	try:
		# 连接数据库
		conn = pymysql.connect(host=localhost,port=port,user=mysqluser,passwd=mysqlpwd,db=mysqldatabase,charset=charset)
		# 关闭数据库
		conn.close()
		return 0
	except:
		return 1


# 数据库备份
def mysql_backup():
	# 到mysql的bin目录
	os.chdir(mysqldir)
	# 连接数据库，判断是否数据库是否正常连接
	contip = mysql_con()
	if contip == 0 :
		# 备份数据库
		os.system(mysqlbakup)
		# 备份日志文件内容
		Bakup_log = '[Backup] Backup Successfully. The file is '+backupfile_name+'. -------------- '+today.strftime('%Y-%m-%d %H:%M:%S')+'\n'
		# 写入日志
		with open(backup_logfile,'a') as f:
			f.write(Bakup_log)
	else:
		error_log = '[Error] MySQL connect Error.----------------- '+today.strftime('%Y-%m-%d %H:%M:%S')+'\n'
		with open(error_logfile,'a') as f:
			f.write(error_log)



# 删除一个月前的备份文件
def remove_backup():
	# 到备份文件目录
	os.chdir(backupfiledir)
	# 查找所有文件并删除30天以上的文件
	for i in os.listdir('.'):
		if os.path.isfile(i):
			# 获取文件的修改时间
			f_mtime = os.path.getmtime(i)
			# 判断时间是否是一个月前
			if float(f_mtime) < float(one_month_ago_timestamps):
				# 删除文件
				os.remove(i)
				# 删除日志内容
				remove_log = '[Remove] Remove Backup File '+i+' Successfully. ---------------- '+ today.strftime('%Y-%m-%d %H:%M:%S')+'\n'
				# 写入日志
				with open(remove_logfile,'a') as f:
					f.write(remove_log)
			


if __name__ == '__main__' :
	# 备份
	mysql_backup()
	# 删除超过时间的备份文件
	remove_backup()




