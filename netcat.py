#!/usr/bin/python
import socket

ip = raw_input("Enter IP address: ")
port = input("Enter port: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
	print "Port %d is opened" % port
else:
	print "Port %s is closed" % port
