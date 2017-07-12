from flask import render_template,jsonify,request,url_for
from app import app
from app.models import user

current_user=""
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/api/register',methods=['POST'])
def register():
	first_name=request.form['username']
	last_name=request.form['last_name']
	email=request.form['email']
	password=request.form['password']
	global current_user
	current_user=user.User(first_name,last_name,email,password)
	return jsonify({'status':"success","message":"User registration successful","name":current_user.name,"email":current_user.email})

@app.route("/api/login",methods=['POST'])
def login():
	email=request.form['email']
	password=request.form['password']
	global current_user
	temp=current_user.login(email,password)
	if temp==True:
		return jsonify({'status':"success","message":"User logged in successfully"})
	else:
		return jsonify({'status':"failed","message":"User login failed"})

@app.route("/api/bucketlist",methods=['POST'])
def add_bucketlist():
	name=request.form['title']
	due_date=request.form['due_date']
	global current_user
	current_user.add_bucketlist(name,due_date)
	bucketlist=current_user.view_bucketlist(name)
	return jsonify({"status":"success","message":"Bucketlist added successfully","data":bucketlist})

@app.route("/api/bucketlist/<int:bucketlist>/item/add",methods=['POST'])
def add_item(bucketlist):
	pass

@app.route('/api/item<int:item_id>/edit',methods=['POST'])
def edit_item(item_id):
	pass

@app.route("/api/item/<string:name>/delete",methods=['POST'])
def delete_item():
	pass

@app.route("/api/items",defaults={'item_name':''})
@app.route("/api/items/<path:item_name>")
def view_items(item_name):
	pass
