from flask import render_template, jsonify, request
from app import app
from app.models import user

"""Views defines routes to be called by the client. These rotutes return json data to be consumed by a client. For storing the data 
	during the life time of the application, I am using a super global current user to store an instance of the user class objet

	This module manages communication between the flask server and the Graphic user interface
"""
current_user = ""


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/api/register',methods=['POST'])
def register():
	"""Registrtaion route, it accepts first_name,last_name,email and password from a user form and instatiates a user object which is 
	later assigned to the global variable current_user"""
	first_name=request.form['first_name']
	last_name=request.form['last_name']
	email=request.form['email']
	password=request.form['password']
	global current_user
	current_user=user.User(first_name,last_name,email,password)
	return jsonify({'status':"success","message":"User registration successful","name":current_user.name,"email":current_user.email})

@app.route("/api/login",methods=['POST'])
def login():
	"""Login route accepts email and password from a form and compares it with the ones set in the User class by passing both credentials as arguments
	to the login method"""
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
	"""Add a user's bucketlist"""
	name=request.form['name']
	due_date=request.form['description']
	global current_user
	current_user.add_bucketlist(name,due_date)
	bucketlist=current_user.view_bucketlist(name)
	return jsonify({"status":"success","message":"Bucketlist added successfully","data":name})

@app.route("/api/bucketlistitem/<string:bucketlist>/item/add",methods=['POST'])
def add_item(bucketlist):
	"""This adds an Item to the bucket list and returns a JSON string with the ppropriate status"""
	global current_user
	item=request.form['item']
	item=current_user.add_bucketlist_item(bucketlist,item)
	if item !=False:
		return jsonify({"status":"success","message":"Bucketlist item added succcessfully","data":item})
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

@app.route("/api/bucketlists")
def view_buckets():
	global current_user
	bucketlists=[]

	buckets=current_user.view_bucketlist()
	for bucket in buckets:
		bucketlists.append(current_user.view_bucketlist(bucket))
	return jsonify({"status":"success","data":bucketlists})

@app.route("/api/bucketlist/<string:bucketlist>/edit",methods=['POST'])
def edit_bucketlist(bucketlist):
	global current_user
	if bucketlist in current_user.bucketlists:
		name=request.form['name']
		due_date=request.form['name']
		example=current_user.bucketlists[bucketlist].edit(name,due_date)
		if example:
			tmp=current_user.bucketlists[bucketlist]
			del current_user.bucketlists[bucketlist]
			current_user.bucketlists[name]=tmp
			return jsonify({'status':'success','message':'Bucketlist edited successfully'})
		else:
			return jsonify({'status':'fail','message':'Bucketlist not edited'})
	else:
		return jsonify({'status':'fail','message':'Bucketlist not edited'})

@app.route("/api/bucketlist/<string:bucketname>")
def view_bucket(bucketname):
	global current_user
	resp=current_user.view_bucketlist(bucketname)

	if resp:
		return jsonify([{"status":"success","data":resp}])
	else:
		return jsonify({"status":"failed","message":"Bucketlist does not exist"})		

@app.route("/api/items/bucketlist/<string:bucketlist>",methods=['GET'])
def view_bucketlist_item(bucketlist):
	global current_user
	bucketlist_items=current_user.view_bucket_list_item(bucketlist)
	if bucketlist_items:
		list_items=[]
		for item in bucketlist_items:
			list_items.append(item.show_info())
		return jsonify({"status":"success","data":list_items})
	else:
		return jsonify({"status":"failed","message":"No items returned"})


@app.route("/api/item/<string:bucketlist>/<string:item_name>")
def view_items(bucketlist,item_name):
	global current_user
	bucketlist_item=current_user.view_bucket_list_item(bucketlist,item_name)
	if bucketlist_item:
		list_items=[]
		list_items.append(bucketlist_item[0].show_info())
		return jsonify({"status":"success","data":list_items})
	else:
		return jsonify({"status":"failed","message":"No items returned"})

@app.route("/api/delete/<string:bucketlist>/<string:item_name>")
def delete(bucketlist,item_name):
	global current_user
	bucketlist_item=current_user.delete_bucketlist_item(bucketlist,item_name)
	if bucketlist_item:
		return jsonify({"status":"success","data":"Deleted successfully"})
	else:
		return jsonify({"status":"failed","message":"Delete fail"})

@app.route("/api/complete/<string:bucketlist>/<string:item>")
def complete(bucketlist,item):
	global current_user
	completed=current_user.mark_complete(bucketlist,item)
	if completed:
		return jsonify({"status":"success","data":completed})
	else:
		return jsonify({"status":"failed","message":"Item not marked complete"})