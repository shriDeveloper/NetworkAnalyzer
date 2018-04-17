from flask import Flask,render_template,Response
from Ping import pingdata
import time
from listIP import networkData
from sniffer import captureData
from OpenScan import openScan
from progressUpdate import progressUpdate
from renderStats import render_stat
app=Flask(__name__)
print(app)
app.register_blueprint(pingdata)
app.register_blueprint(captureData)
app.register_blueprint(networkData)
app.register_blueprint(openScan)
app.register_blueprint(render_stat)
@app.route('/')
def hello_world():
	f=open('Data.csv','r')
	l=len(f.readlines())-1
	print(l)
	f.seek(0,0)
	d=[]
	while(l!=0):
		st=f.readline().rstrip().split(",")
		print(st)
		temp=[]
		print(st)
		if(st==['']):
			break

		else:
			for i in st:
				temp.append(i)
				print(i)
			d.append(temp)
		l-=1
	f.close()
	print("TAG: ",d)
	return render_template('HomePage.html',page_ip=d)
if __name__=="__main__":
	app.run(debug=True)