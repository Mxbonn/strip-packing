from spp.ph import phspprg
from spp import visualize
from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def main():
    r1 = Rectangle(0, 0, 5, 10)
    r2 = Rectangle(5, 0, 15, 9)
    r3 = Rectangle(0, 10, 2, 14)
    r4 = Rectangle(2, 10, 3, 8)
    r5 = Rectangle(5, 10, 10, 20)
    rectangles = [r1, r2, r3, r4, r5]

    visualize(20, 30, rectangles)

def test():
    boxes = [[5, 3], [5, 3], [2, 14], [35, 8], [10, 20]]
    width = 10
    height, rectangles = phspprg(width, boxes)
    visualize(width, height, rectangles)
    print("The height is: {}".format(height))

def nice1():
    boxes = [[31.94849, 28.48085], [17.06567, 46.53127], [21.41732, 31.32587], [19.61116, 29.71539], [29.41763, 19.24619],
             [17.67189, 31.32587], [11.89663, 46.53127], [19.61116, 25.32328], [19.47804, 20.65838], [16.75077, 22.59542],
             [10.48017, 34.38029], [9.02011, 35.94995], [8.997871, 34.38029], [22.14952, 13.63546], [22.92838, 12.69867],
             [14.7424, 19.24619], [22.92838, 12.10353], [16.25649, 16.32301], [28.96231, 8.950342], [28.96231, 8.949194],
             [22.92838, 11.14775], [14.64505, 16.32301], [16.93969, 13.63546], [16.75077, 12.97378], [13.25848, 16.32301]
             ]
    width = 100
    height, rectangles = phspprg(width, boxes)
    print("The height is: {}".format(height))
    visualize(width, height, rectangles)


if __name__ == "__main__":
    nice1()