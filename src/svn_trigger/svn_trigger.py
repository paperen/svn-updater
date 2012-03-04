# -*- coding: UTF-8 -*-

__author__="paperen"
__date__ ="$2012-2-27 21:54:28$"

if __name__ == "__main__":
    
	import socket

	host = raw_input( '请输入SVN监听器地址(默认为localhost)\n' )
	if host == '':
		host = 'localhost'

	port = raw_input( '\n请输入SVN监听器端口(默认为9999)\n' )
	if port == '':
		port = 9999

	cmd = 'update'

try:
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	sock.connect( ( host, port ) )
	sock.send( cmd )

	received = sock.recv(1024)
	print received
	sock.close()
	
except:
	print '无法跟SVN监听器连接，请检查其是否开启'
