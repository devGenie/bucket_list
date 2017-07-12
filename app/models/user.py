class User(object):
	"""
		The user class implements the functionality of a user on the bucketlist application
	"""
	def __init__(self,first_name,last_name):
		"""The constructor initialises class variables"""
		pass

	def login(self,email,password):
		"""The login method checks if the user email and password match the ones provided by the app"""
		pass

	def logout(self,email,password):
		""" The logout method toggles the login status to off"""
		pass

	def add_bucketlist(self,name,due_age):
		""" This method adds a new bucketlist"""
		pass

	def view_bucketlist(self,name=""):
		"""This method returns a dictionary of bucket list elements"""
		pass

	def edit_bucketlist(self,bucket,name,due_age):
		"""This method edits the bucketlist specified"""
		pass

	def delete_bucketlist(self,name):
		pass


