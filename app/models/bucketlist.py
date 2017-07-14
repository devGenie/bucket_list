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

	def edit(self,name):
		self.name=name

	def add_item(self,name):
		list_item=ListItem(name)
		self.bucketlist_items[name]=list_item

	def edit_item(self,item,name):
		temp=item
		del bucketlist_items[item.name]
		temp.name=name
		bucketlist_items[name]=temp
		return temp.show_info()

	def delete_item(self,name):
		if name and name in self.bucketlist_items:
			del self.bucketlist_items[name]
			return True
		else:
			return False

	def complete_item(self,name):
		pass

	def view_item(self,name):
		if name in self.bucketlist_items:
			item=self.bucketlist_items[name]
			return item.show_info()

	def get_item(self,name):
		if name in self.bucketlist_items:
			item=self.bucketlist_items[name]
			return item
		else:
			return False