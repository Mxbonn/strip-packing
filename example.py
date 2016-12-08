from spp.ph import phspprg
from spp import visualize
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def main():
    boxes = [[5, 3], [5, 3], [2, 14], [35, 8], [10, 20]]
    width = 10
    height, rectangles = phspprg(width, boxes)
    visualize(width, height, rectangles)
    print("The height is: {}".format(height))


if __name__ == "__main__":
    main()
