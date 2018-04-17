from flask import render_template,Flask,Blueprint
import socket
from urllib2 import urlopen, URLError,HTTPError
pingdata=Blueprint('ping',__name__)
#app=Flask(__name__)
@pingdata.route('/ping/')
def ping():	
	print("HELLO YOU ARE HERE")
	return render_template('HomePage.html')
#if __name__ == "__main__":
    #app.run()
