#!/usr/bin/python3
""" Use the module for to instance of the Square class

    Class:
        Square
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """ Class definition
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            args = list(args)
            if len(args) > 1:
                args.insert(2, args[1])
            for i in range(len(args)):
                setattr(self, (list(self.__dict__.keys()))[i], args[i])
        else:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        return dict(zip(
            ["id", "size", "x", "y"],
            [self.id, self.size, self.x, self.y]
        ))
