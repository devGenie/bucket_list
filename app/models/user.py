
from .bucketlist import BucketList
class User(object):
	"""
		The user class implements the functionality of a user on the bucketlist application
	"""
	def __init__(self,first_name,last_name,email,password):
		"""The constructor initialises class variables"""
		self.name=first_name+" "+last_name
		self.email=email
		self.password=password
		self.bucketlists={}
		self.login_status=False

	def login(self,email,password):
		"""The login method checks if the user email and password match the ones provided by the app"""
		if email==self.email and password==self.password:
			self.login_status=True
			return True
		else:
			print(self.email)
			print(self.password)
			return False

	def get_info(self):
		"""This method rreturns a dictionary of user info"""
		pass

	def logout(self,email,password):
		""" The logout method toggles the login status to off"""
		pass

	def add_bucketlist(self,name,due_age):
		""" This method adds a new bucketlist"""
		self.bucketlists[name]=BucketList(name,due_age)

	def view_bucketlist(self,name=""):
		"""This method returns a dictionary of bucket list elements"""
		if name and name in self.bucketlists:
			bucketlist=self.bucketlists[name]
			return {"name":bucketlist.name,"due_age":bucketlist.due_age}
		elif not name:
			return self.bucketlists
		elif name not in self.bucketlists:
			return False

	def edit_bucketlist(self,bucket,name,due_age):
		"""This method edits the bucketlist specified"""
		pass

	def edit_bucketlist_item(self,bucket,old_name,new_name):
		"""This edits an item in the bucketlist"""
		if bucket in self.bucketlists:
			conataining_bucket=self.bucketlists[bucket]
			edit_this=conataining_bucket.get_item(old_name)
			return conataining_bucket.edit_item(edit_this,new_name)
		else:
			return False

	def add_bucketlist_item(self,bucketlist,item_name):
		"""This method edits the bucketlist specified"""
		if bucketlist in self.bucketlists:
			bucket=self.bucketlists[bucketlist]
			bucket.add_item(item_name)
			if item_name in bucket.bucketlist_items:
				return bucket.view_item(item_name)
			else:
				return False
		else:
			return False

	def view_bucket_list_item(self,bucketlist,item_name=""):
		if bucketlist in self.bucketlists:
			items=[]
			bucket=self.bucketlists[bucketlist]
			if item_name:
				items.append(bucket.get_item(item_name))
			else:
				res=bucket.view_bucketlists()
				for itm in res:
					items.append(bucket.get_item(itm))
			return items
		else:
			return False

	def delete_bucketlist(self,name):
		if name in self.bucketlists:
			del self.bucketlists[name]
		else:
			return "Bucket list not deleted"



