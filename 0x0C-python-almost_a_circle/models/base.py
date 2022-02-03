#!/usr/bin/python3
""" Use the module for to instance of the Base class

    Class:
        Base
"""


import json
import csv


class Base:
    """ Class definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            with open(filename, "w", encoding="UTF-8") as file:
                file.write(cls.to_json_string([]))
        else:
            with open(filename, "w", encoding="UTF-8") as file:
                file.write(
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                    )
                )

    @staticmethod
    def from_json_string(json_string):
        obj = json.loads(json_string)
        if json_string is None or len(obj) == 0:
            return []
        else:
            return obj

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(15, 20)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        llist = []
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                file.read()
        except FileNotFoundError:
            return llist
        else:
            with open(filename, "r", encoding="UTF-8") as file:
                list_dictionaries = cls.from_json_string(file.read())
                for dictionary in list_dictionaries:
                    llist.append(cls.create(**dictionary))
            return llist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w") as file:
            writer = csv.writer(file, delimiter=",")
            " writing the items of the iterable in each row of the file "
            writer.writerow(
                obj.to_dictionary() for obj in list_objs
            )

    @classmethod
    def load_from_file_csv(cls):
        llist = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "r") as file:
            " reader(list): contain the rows of the file"
            reader = csv.reader(file)
            for fields in reader:
                " obj(dict): key/value of the instance of cls "
                for obj in fields:
                    obj = json.loads(obj.replace("\'", "\""))
                    llist.append(cls.create(**obj))
        return llist
