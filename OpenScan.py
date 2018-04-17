from socket import *
import optparse
import nmap
from threading import Thread,Semaphore
import nmap
import os
import json
from threading import Thread
from flask import render_template,Flask,Blueprint
screenlock=Semaphore(value=1)
openScan=Blueprint('openScan',__name__)
app=Flask(__name__)
@openScan.route('/openScan/')
def scanOpenPort():
	#OPNE A NEW OPEN PORTS FILE
	file=open("Ports.csv","a")
	print("YOU ARE AT OPEN CAN!!")
	list=[]
	nm=nmap.PortScanner()
	data=nm.scan(hosts="172.16.162.*",arguments="-sP")
	#data=nm.Scanning(hosts="192.168.45.10",arguments="-sp")
	print("Number of connected IPs: {} ".format(data['nmap']['scanstats']['uphosts']))
	a=[ip for ip in data['scan']]
	for i in a:
    		print("\tIP: {}".format(i))
    		print("Scanning {}".format(i))
    	port=[80,21,29,8090,25,443,445,14147,3306]
    	for j in port:
        	t=Thread(target=checkPort,args=(i,str(j),file))
        	t.start()
	return render_template('HomePage.html',list=list)
def checkPort(source,portlist,file):
	soc=gethostbyname(source)
	#print(soc)
	nm=nmap.PortScanner()
	nm.scan(soc,portlist)
	state=nm[soc]['tcp'][int(portlist)]['state']
	print("{}\t{}\t{}\t{}".format(nm[soc].hostname(),soc,portlist,state))
	#WRITE HERE
	q="{}\t{}\t{}\t{}".format(nm[soc].hostname(),soc,portlist,state)
	file.write(str(nm[soc].hostname())+",")
	file.write(str(soc)+",")
	file.write(str(portlist)+",")
	file.write(str(state))
	file.write("\n")