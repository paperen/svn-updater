# -*- coding: UTF-8 -*-

__author__="paperen"
__date__ ="$2012-2-27 21:54:28$"

import SocketServer, os, time

# �����ķָ���
global delimiter
delimiter = '===================='

def currentTime():
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

class MyTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self) :
		self.data = self.request.recv(1024).strip()
		# ���±��ص�ǰ�汾
		if self.data == 'update':
			
			#
			print delimiter + currentTime() + '\n'
			print self.client_address[0] + ' Ҫ����� ' + config['SVNRep'].strip() + '\n'
		
			# CMD
			cmd = config['SVNPath'].strip() + ' update ' + config['SVNRep'].strip()
			oStdout = os.popen( cmd )
			result = ''
			# ��ȡCMD���
			while True:
				data = oStdout.readline()
				if data == '' :
					break
				result += data + '\n'

			self.request.send( result )
			
			#���
			print '�������\n'
			
if __name__ == "__main__" :

	# ����
	global config
	config = []

	# �����˿�
	port = raw_input('����������˿�(Ĭ��Ϊ9999)\n')
	if port == '':
		port = 9999
	
	# ��������
	host = 'localhost'

	# ��ȡ�����ļ�����
	fhandle = open('config.ini', 'r')
	
	fcontent = fhandle.read().split( '\n' )
	for i in fcontent :
		if i == '':
			continue
		tmp = i.split( '=' )
		# ��Ч���ò���
		if len( tmp ) > 2 or len( tmp ) < 1:
			continue
		# ȥ���ո�
		tmp[0] = tmp[0].strip()
		config.append( tuple( tmp ) )
	
	config = dict( config )
	
	# ��������Ƿ��㹻
	if ( 'SVNPath' in config ) != True or ( 'SVNRep' in config ) != True :
		print '����config.ini�ļ����Ƿ�������SVN·����SVN�汾��·��'
	else :
		server = SocketServer.TCPServer((host, port), MyTCPHandler)
		server.serve_forever()

	
    