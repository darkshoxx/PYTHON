class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


class Map(object):

    shapes = {
        'rectangle': Rectangle(1, 1),
        'square': Square(1),
    }

    #def __init__(self, shape):
    #    self.shape = shape

    def some_shape(self, shape_name):
        val = Map.shapes.get(shape_name)
        return val

Tennis = Map()

print(Tennis.some_shape(shape_name='square'))