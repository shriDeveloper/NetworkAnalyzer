import nmap
import os
import json
import checkopenports
from threading import Thread
from flask import render_template,Flask,Blueprint
networkData=Blueprint('IPScan',__name__)
app=Flask(__name__)
@networkData.route('/IPScan/')
def scanNetworkForIP():
	list=[]
	import xml.etree.cElementTree as ET
	root = ET.Element("connection")
	doc = ET.SubElement(root, "session")
	nm=nmap.PortScanner()
	data=nm.scan(hosts="172.16.162.*",arguments="-sP")
	print("Number of connected IPs: {} ".format(data['nmap']['scanstats']['uphosts']))
	#print(data['scan'])
	a=[ip for ip in data['scan']]
	#print(a)
	print("\n\tList of IPs Connected :")
	print("------------------------------------------------------")
	for i in a:
		q="\t{}IP connected: {}{}".format("|",i,"|")
    	list.append(q)
    	ET.SubElement(doc, "IP").text =	q	
    	print("\t{}IP connected: {}{}".format("|",i,"|"))
	print("-------------------------------------------------------")
	tree = ET.ElementTree(root)
	tree.write("XML/ip_list.xml")
	return render_template('HomePage.html',data=list)
	#for i in a:
    #print("\tIP: {}".format(i))
    #print("Scanning {}".format(i))
    #port=[80,21,29,8090,25,443,445,14147,3306]
    #for j in port:
        #t=Thread(target=checkopenports.checkPort,args=(i,str(j)))
        #t.start()