import unittest
import os
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        """Set up test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john@example.com"
        self.user.password = "password"

    def test_instance_creation(self):
        """Test User instance creation."""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test User attributes."""
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.password, "password")

    def test_to_dict(self):
        """Test User to_dict method."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['email'], "john@example.com")
        self.assertEqual(user_dict['password'], "password")

    def test_save(self):
        """Test User save method."""
        self.user.save()
        user_id = self.user.id
        user_key = "User." + user_id
        obj_dict = storage.all()
        self.assertIn(user_key, obj_dict)

    def test_reload(self):
        """Test User reload method."""
        self.user.save()
        user_id = self.user.id
        user_key = "User." + user_id
        storage.all().clear()
        storage.reload()
        obj_dict = storage.all()
        self.assertIn(user_key, obj_dict)


if __name__ == "__main__":
    unittest.main()

