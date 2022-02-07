#!/usr/bin/env python3


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json


class TestClass(unittest.TestCase):

    def setUp(self):
        self.obj0 = Base()
        self.obj1 = Base(5)
        self.list_dictionaries = [
            [{"width": 5, "height": 7}, {"width": 10, "height": 4}],
            None,
            "hello",
            5,
            [[4, 5], [7, 9], [-5, 13]],
            {"first": 5, "second": 7, "array": ["hola", 7, [7, 3]]},
            (4, "hola", ["perro", 2]),
            ""
        ]

    def test_class(self):
        self.assertIsNotNone(Base)
        self.assertRaises(AttributeError, lambda: Base.__nb_objects)

    def test_instance(self):
        " test for obj0 instance "
        self.assertIsNotNone(self.obj0)
        self.assertIsNotNone(self.obj0.id)
        " test for obj1 instance "
        self.assertEqual(self.obj1.id, 5)
        " test for obj2 instance "
        self.assertRaises(TypeError, lambda: Base(5, 6))

    def test_exist_method_class(self):
        self.assertIsNotNone(Base.to_json_string)
        self.assertIsNotNone(Base.from_json_string)

    def test_exist_static_method(self):
        self.assertIsNotNone(Base.save_to_file)
        self.assertIsNotNone(Base.create)
        self.assertIsNotNone(Base.load_from_file)
        self.assertIsNotNone(Base.save_to_file_csv)
        self.assertIsNotNone(Base.load_from_file_csv)

    def test_to_json_string(self):
        for case in self.list_dictionaries:
            self.assertIsInstance(Base.to_json_string(case), str)
            self.assertEqual(json.dumps(case), Base.to_json_string(case))
        self.assertRaises(TypeError, Base.to_json_string, self.obj0)
