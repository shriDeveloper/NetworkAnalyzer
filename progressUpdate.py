from flask import render_template,Flask,Blueprint
import socket
from urllib2 import urlopen, URLError,HTTPError
progressUpdate=Blueprint('Progress',__name__)
#app=Flask(__name__)
@progressUpdate.route('/Progress/')
def progress():	
	print("HELLO YOU ARE HERE")
	return render_template('Progress.html')
#if __name__ == "__main__":
    #app.run()
