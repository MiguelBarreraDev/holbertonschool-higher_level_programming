#!/usr/bin/python3
"""class - square"""


class Square:
    """
    Define:
        Property
            size
            position
        Methos
            area
            my_print
    """
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
        x, y = value
        band = isinstance(x, int) and isinstance(y, int)
        if len(value) == 2 and band and x >= 0 and y >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for e in range(self.__position[1]):
                print()
            for e in range(self.__size):
                print(' ' * self.__position[0], end="")
                print('#' * self.__size)
