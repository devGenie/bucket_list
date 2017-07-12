import unittest
import context
from app.models import user

class TestUser(unittest.TestCase):
	def setUp(self):
		self.test_user=user.User("Onen","Julius","jonen54@gmail.com","256mygame")
	def test_user_created(self):
		self.assertEqual(self.test_user.name,"Onen Julius","User name not initialized")

	def test_user_is_object(self):
		self.assertIsInstance(self.test_user,user.User,"test user is not an instance of class User")

	def test_add_bucketlist(self):
		bucket_lists=self.test_user.view_bucketlist()
		self.test_user.add_bucketlist("before 30",30)
		new_bucket_lists=self.test_user.view_bucketlist()
		self.assertNotEqual(len(bucket_lists),len(new_bucket_lists),"Bucketlist not added")

	def test_view_bucketlist(self):
		self.test_user.add_bucketlist("before 30",30)
		bucket_list=self.test_user.view_bucketlist("before 30")
		self.assertDictEqual({"name":"before 39","due_age":30},bucket_list,"Bucket list not returned")

	def test_edit_bucket_list(self):
		self.test_user.add_bucketlist("before 25",25)
		bucket_list=self.test_user.view_bucketlist("before 25")
		self.test_user.edit_bucketlist(bucket_list,"before 30",30)
		bucket_list_edit=self.test_user.view_bucketlist

	def test_delete_bucket_list(self):
		self.test_user.add_bucketlist("My bucketist",40)
		bucket_lists1=self.test_user.view_bucketlist("My bucketist")
		self.test_user.delete_bucketlist("My bucketlist")
		bucket_lists2=self.test_user.view_bucketlist()
		self.assertNotEqual(len(bucket_lists2),len(bucket_lists1),"Bucket list has not been deleted")