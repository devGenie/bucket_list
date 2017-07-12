
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

	def login(self,email,password):
		"""The login method checks if the user email and password match the ones provided by the app"""
		pass

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
		return self.bucketlists

	def edit_bucketlist(self,bucket,name,due_age):
		"""This method edits the bucketlist specified"""
		pass

	def delete_bucketlist(self,name):
		pass


