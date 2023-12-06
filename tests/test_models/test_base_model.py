#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import os
import re
import time
import json
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Sets up test methods."""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_str_representation(self):
        str_representation = str(self.base_model)
        self.assertIn('[BaseModel]', str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('created_at', str_representation)
        self.assertIn('updated_at', str_representation)

    def test_save_updates_updated_at(self):
        """Tests that calling save updates the updated_at attribute."""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str_method(self):
        """Tests the string representation of the object."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_save_calls_storage_save(self):
        """Tests that calling save also calls storage.save()."""
        self.reset_storage()
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as File:
            self.assertEqual(len(File.read()), len(json.dumps(d)))
            File.seek(0)
            self.assertEqual(json.load(File), d)


if __name__ == '__main__':
    unittest.main()
