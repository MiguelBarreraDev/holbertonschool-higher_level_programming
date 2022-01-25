#!/usr/bin/python3
""" You can create instances of objects related to geometric figures

    Class:
        Dimension
        Rectangule
"""


class Dimension:
    """ Define dimensions the Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


class Rectangle(Dimension):
    """ Define the Rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Dimension.__init__(self, width, height)
        Rectangle.number_of_instances += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        A = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            A = 0
        return A

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        ctn = ""
        if self.width == 0 or self.height == 0:
            return ctn
        for e in range(self.height):
            ctn += str(self.print_symbol) * self.width
            if e != self.height - 1:
                ctn += '\n'
        return ctn

    def __repr__(self):
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
