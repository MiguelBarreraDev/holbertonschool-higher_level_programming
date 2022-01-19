#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class that defines a square with size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) \
           or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print()
            for e in range(self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)

    def __str__(self):
        sq = ""
        if self.__size == 0:
            return sq
        else:
            for e in range(self.position[1]):
                sq += '\n'
            for e in range(self.size):
                sq += ' ' * self.position[0]
                sq += '#' * self.size
                if e != (self.size - 1):
                    sq += '\n'
            return sq
