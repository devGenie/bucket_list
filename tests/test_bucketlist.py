import unittest
from app.models.bucketlist import BucketList
from app.models.list_item import ListItem

class TestBucketList(unittest.TestCase):
	def setUp(self):
		self.test_bucketList=BucketList("Bucket1",30)

	def test_bucketlist_created(self):
		self.assertIsInstance(self.test_bucketList,BucketList,"Bucketlist class not instatiated")

	def test_bucketlist_items_container(self):
		self.assertIsInstance(self.test_bucketList.view_bucketlists(),dict,"Bucketlist is not a dictionary")

	def test_bucketlist_add_item(self):
		items_count=len(self.test_bucketList.view_bucketlists())
		self.test_bucketList.add_item("Swimming")
		increment=len(self.test_bucketList.view_bucketlists())
		self.assertNotEqual(items_count,increment,"Item not added to bucketlist")

	def test_bucketlist_edit_item(self):
		self.test_bucketList.add_item("Go Pro")
		item=self.test_bucketList.view_item

	def test_bucketlist_complete_item(self):
		pass

	def test_bucketlist_edit_item(self):
		pass

	def test_bucketlist_delete_item(self):
		pass

	def test_bucket_list_name(self):
		pass

	def test_bucket_list_due_age(self):
		pass

	def test_view_bucketlist(self):
		pass

	def test_view_bucketlist_items(self):
		pass

	def test_view_bucketlist_item(self):
		self.test_bucketList.add_item("Gaming")
		item=self.test_bucketList.view_item("Gaming")
		self.assertEqual(item,{"name":"Gaming","complete_status":False})

	def test_get_bucketlist_item(self):
		self.test_bucketList.add_item("Sporting")
		item=self.test_bucketList.get_item("Sporting")
		self.assertIsInstance(item,ListItem,"List Item not added")


