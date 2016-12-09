from spp.ph import phspprg
from spp import visualize
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def main():
    boxes = [
        [5, 3], [5, 3], [2, 4], [30, 8], [10, 20],
        [20, 10], [5, 5], [5, 5], [10, 10], [10, 5],
        [6, 4], [1, 10], [8, 4], [6, 6], [20, 14]
    ]
    width = 30
    height, rectangles = phspprg(width, boxes)
    visualize(width, height, rectangles)
    print("The height is: {}".format(height))


if __name__ == "__main__":
    main()
