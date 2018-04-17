from socket import *
import optparse
import nmap
from threading import Thread,Semaphore
screenlock=Semaphore(value=1)
def checkPort(source,portlist):
	soc=gethostbyname(source)
	#print(soc)
	nm=nmap.PortScanner()
	nm.scan(soc,portlist)
	state=nm[soc]['tcp'][int(portlist)]['state']
	print("{}\t{}\t{}\t{}".format(nm[soc].hostname(),soc,portlist,state))
