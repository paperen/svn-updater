# -*- coding: UTF-8 -*-

__author__="paperen"
__date__ ="$2012-2-27 21:54:28$"

if __name__ == "__main__":
    
	import socket

	host = raw_input( '������SVN��������ַ(Ĭ��Ϊlocalhost)\n' )
	if host == '':
		host = 'localhost'

	print '��������ַΪ' + host + '\n'
	
	port = raw_input( '������SVN�������˿�(Ĭ��Ϊ9999)\n' )
	if port == '':
		port = 9999

	print '�������˿�Ϊ' + repr( port ) + '\n'
		
	cmd = 'update'

try:
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	sock.connect( ( host, port ) )
	sock.send( cmd )

	received = sock.recv(1024)
	print received
	sock.close()
	
except:
	print '�޷���SVN���������ӣ��������Ƿ���'

raw_input('');
