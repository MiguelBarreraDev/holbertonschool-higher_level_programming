#!/usr/bin/python3
""" Use the module for to instance of the Base class

    Class:
        Base
"""


import json
import csv


class Base:
    """ Base class definition to be inherit

        Inherit Instances:
            Members:
                id(int): Unique indentifier of the instance

            Methods:
                Special:
                    __init__

        Class Attributes:
            __nb_objects(int): private attribute to be assigned as id, if not
            received as instance parameter

        Class methods:
            save_to_file, create, load_from_file,
            save_to_file_csv, load_from_file_csv
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method to initialize fields at istantiate time """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Parse to list object in json """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Store a list with representations objects in a file
        Args:
                list_objs: list to save
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="UTF-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                file.write(
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                    )
                )

    @staticmethod
    def from_json_string(json_string):
        """ Parse json to list object  """
        if json_string is None or obj == []:
            return []
        else:
            obj = json.loads(json_string)
            return obj

    @classmethod
    def create(cls, **dictionary):
        """ Create object with the members store in dictionary """
        dummy = cls(10, 5, 20)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load instances based on the list dictionaries
        stored in the file with json format
        """
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
        """ Store a representation object in csv format in a file """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w") as file:
            writer = csv.writer(file, delimiter=",")
            " writing the items of the iterable in each row of the file "
            writer.writerow(
                obj.to_dictionary() for obj in list_objs
            )

    @classmethod
    def load_from_file_csv(cls):
        """ Load instances based on the list of dictionaries
        stored in the file with csv format
        """
        llist = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", encoding="UTF-8") as file:
                file.read()
        except FileNotFoundError:
            return llist
        else:
            with open(filename, "r") as file:
                " reader(list): contain the rows of the file"
                reader = csv.reader(file)
                for fields in reader:
                    " obj(dict): key/value of the instance of cls "
                for obj in fields:
                    obj = json.loads(obj.replace("\'", "\""))
                    llist.append(cls.create(**obj))
        return llist
