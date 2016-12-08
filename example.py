from spp import visualize
from collections import namedtuple

def main():
    Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])
    r1 = Rectangle(0, 0, 5, 10)
    r2 = Rectangle(5, 0, 15, 9)
    r3 = Rectangle(0, 10, 2, 14)
    r4 = Rectangle(2, 10, 3, 8)
    r5 = Rectangle(5, 10, 10, 20)
    rectangles = [r1, r2, r3, r4, r5]

    visualize(20, 30, rectangles)

if __name__ == "__main__":
    main()