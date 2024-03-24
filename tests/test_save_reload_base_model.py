import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import storage
from models.base_model import BaseModel

class TestSaveReloadBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
   	 storage.all().clear()

    def test_reload(self):
        storage.save()
        storage.reload()
        objs = storage.all()
        self.assertIn("BaseModel.{}".format(self.model.id), objs)

    def test_new(self):
        model = BaseModel()
        storage.reload()
        objs = storage.all()
        self.assertIn("BaseModel.{}".format(model.id), objs)

if __name__ == '__main__':
    unittest.main()

