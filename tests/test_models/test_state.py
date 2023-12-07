#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import os
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_state_inherits_from_base_model(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_attributes_assignment(self):
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_state_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)

    def test_state_str_representation(self):
        self.assertEqual(str(self.state), "[State] ({}) {}"
                         .format(self.state.id, self.state.__dict__))


if __name__ == '__main__':
    unittest.main()
