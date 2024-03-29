#!/usr/bin/python3
""" Module representing Rectangle class
Parameters:
None

Classes:
Rectangle
"""


class Rectangle:
    """
    Rectangle class definition

    Attributes
    - width (int): Defaults to zero
    - height (int): Defaults to zero
    - print_symbol (char): Defaults to #

    Methods:
    - area: Area of therectangle
    - perimeter: Perimeter of the rectangle

    Tests:
    >>> new = Rectangle(2,4)
    >>> new.width
    2
    >>> new.height
    4
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        >>> new = Rectangle(2,4)
        >>> new.width
        2
        """
        return self.__width

    @property
    def height(self):
        """
        >>> new = Rectangle(2,4)
        >>> new.height
        4
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        >>> new = Rectangle(2,4)
        >>> new.height = 3
        >>> new.height
        3
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        >>> new = Rectangle(2,4)
        >>> new.area()
        8
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        >>> new = Rectangle(2,4)
        >>> new.perimeter()
        12
        >>> new = Rectangle(0,0)
        >>> new.perimeter()
        0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def str(self):
        """
        >>> new = Rectangle(1,1)
        >>> new.str()
        #
        >>> new = Rectangle()
        >>> new.str()
        >>> new = Rectangle(2,4)
        >>> new.print()
        ##
        ##
        ##
        ##
        >>> new.width = 10
        >>> new.height = 3
        >>> new.print()
        ##########
        ##########
        ##########
        """
        width, height = (self.width, self.height)

        for _ in range(height):
            for _ in range(width):
                print(self.print_symbol, end="")
            print()

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        ch = self.print_symbol
        str_repr = ""
        row = str(ch) * self.width
        for i in range(self.height):
            str_repr += row + ("" if i == self.height - 1 else "\n")
        return str_repr

    def __print__(self):
        return self.__str__()

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"<3-rectangle.Rectangle object at {hex(id(self))}>"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_2 if rect_2.area() > rect_1.area() else rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
