from flask import render_template,jsonify,request,url_for
from app import app
from app.models import user

"""Views defines routes to be called by the client"""
current_user=""
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/api/register',methods=['POST'])
def register():
	"""Registrtaion route"""
	first_name=request.form['first_name']
	last_name=request.form['last_name']
	email=request.form['email']
	password=request.form['password']
	global current_user
	current_user=user.User(first_name,last_name,email,password)
	return jsonify({'status':"success","message":"User registration successful","name":current_user.name,"email":current_user.email})

@app.route("/api/login",methods=['POST'])
def login():
	"""Login route"""
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
	"""Add user's bucketlist"""
	name=request.form['name']
	due_date=request.form['description']
	global current_user
	current_user.add_bucketlist(name,due_date)
	bucketlist=current_user.view_bucketlist(name)
	return jsonify({"status":"success","message":"Bucketlist added successfully","data":name})

@app.route("/api/bucketlistitem/<string:bucketlist>/item/add",methods=['POST'])
def add_item(bucketlist):
	global current_user
	item=request.form['item']
	item=current_user.add_bucketlist_item(bucketlist,item)
	if item !=False:
		return jsonify({"status":"success","message":"bucketlist item added succcessfully","data":item})
	else:
		return jsonify({"status":"failed","message":"Bucketlist item not added"})

@app.route('/api/<string:bucketlist>/item/<string:item>/edit',methods=['POST'])
def edit_item(bucketlist,item):
	global current_user
	old_name=item
	new_name=request.form['new_name']
	result=current_user.edit_bucketlist_item(bucketlist,old_name,new_name)
	if result !=False:
		return jsonify({"status":"success","message":"Item edited successfully","data":result})
	else:
		return jsonify({"status":"failed","message":"Item failed to edit"})

@app.route("/api/item/<string:name>/delete",methods=['POST'])
def delete_item():
	pass

@app.route("/api/bucketlists",defaults={'bucketname':''})
@app.route("/api/bucketlists/<string:bucketname>")
def view_buckets(bucketname):
	bucketlists=[]
	global current_user
	if not bucketname:
		bucketlists.append(current_user.view_bucketlist())
	else:
		buckets=current_user.view_bucketlist()
		for bucket in buckets:
			bucketlists.append(current_user.view_bucketlist(bucket))
	return jsonify({"status":"success","data":bucketlists})

@app.route("/api/items",defaults={'item_name':''})
@app.route("/api/items/<path:item_name>")
def view_items(item_name):
	pass
