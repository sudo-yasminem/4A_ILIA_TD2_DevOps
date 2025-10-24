from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello_world():
	return "<p> Hello world of Cyrine </p>"
	
@app.route("/cpt")

def cpt():
	count = 42
	count = str(42)
	return count
	
@app.route("/incr")

def incr():
	count2 = int(cpt())
	count2 +=1
	res2 = str(count2)
	return res2
	

@app.route("/decr")

def decr():
	count3 = int(cpt())
	count3 -=1
	res3 = str(count3)
	return res3
	
