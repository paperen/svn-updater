# -*- coding: UTF-8 -*-

__author__="paperen"
__date__ ="$2012-2-27 21:54:28$"

import SocketServer, os, time

# 华丽的分隔符
global delimiter
delimiter = '===================='

def currentTime():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

class MyTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self) :
		self.data = self.request.recv(1024).strip()
		# 更新本地当前版本
		if self.data == 'update':
			
			#
			print delimiter + currentTime() + '\n'
			print self.client_address[0] + ' 要求更新 ' + config['SVNRep'].strip() + '\n'
		
			# CMD
			cmd = config['SVNPath'].strip() + ' update ' + config['SVNRep'].strip()
			oStdout = os.popen( cmd )
			result = ''
			# 读取CMD结果
			while True:
				data = oStdout.readline()
				if data == '' :
					break
				result += data + '\n'

			self.request.send( result )
			
			#结果
			print '更新完毕\n'
			
if __name__ == "__main__" :

	# 配置
	global config
	config = []

	# 监听端口
	port = raw_input('请输入监听端口(默认为9999)\n')
	if port == '':
		port = 9999
	
	# 监听本地
	host = 'localhost'

	# 读取配置文件内容
	fhandle = open('config.ini', 'r')
	
	fcontent = fhandle.read().split( '\n' )
	for i in fcontent :
		if i == '':
			continue
		tmp = i.split( '=' )
		# 无效配置参数
		if len( tmp ) > 2 or len( tmp ) < 1:
			continue
		# 去除空格
		tmp[0] = tmp[0].strip()
		config.append( tuple( tmp ) )
	
	config = dict( config )
	
	# 必需参数是否足够
	if ( 'SVNPath' in config ) != True or ( 'SVNRep' in config ) != True :
		print '请检查config.ini文件中是否有配置SVN路径与SVN版本库路径'
	else :
		server = SocketServer.TCPServer((host, port), MyTCPHandler)
		server.serve_forever()

	
    