from flask import Flask,render_template,Response,Blueprint
render_stat=Blueprint('Stats',__name__)
app=Flask(__name__)
@render_stat.route('/Stats/')
def showStats():
	f=open("Ports.csv","r")
	l=len(f.readlines())-1
	f.seek(0,0)
	d=[]
	while(l!=0):
		st=f.readline().rstrip().split(",")
		temp=[]
		print(st)
		l-=1
		for i in st:
			temp.append(i)
			print(i)
		d.append(temp)
      	l-=1
	f.close()
	print("TAG: ",d)
	return render_template('ShowStats.html',open_ports=d)