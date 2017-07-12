from .list_item import ListItem
class BucketList(object):
	def __init__(self,name,due_age):
		self.name=name
		self.due_age=due_age
		self.bucketlist_items={}

	def get_info(self):
		pass

	def view_bucketlists(self):
		return self.bucketlist_items

	def add_item(self,name):
		list_item=ListItem(name)
		self.bucketlist_items[name]=list_item

	def edit_item(self,item,name):
		pass

	def delete_item(self,name):
		pass

	def complete_item(self,name):
		pass

	def view_item(self,name):
		pass