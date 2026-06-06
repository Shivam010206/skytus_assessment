class Rectangle:
    def area(self):
        print("Area of Rectangle")


class Circle:
    def area(self):
        print("Area of Circle")


def show_area(shape):
    shape.area()


r = Rectangle()
c = Circle()

show_area(r)
show_area(c)