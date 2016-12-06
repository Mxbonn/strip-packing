import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy


def visualize(width, height):
    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)
    axes.add_patch(
        patches.Rectangle(
            (0, 0),  # (x,y)
            width,  # width
            height,  # height
            hatch='x',
            fill=False,
        )
    )
    axes.add_patch(
        patches.Rectangle(
            (0, 0),  # (x,y)
            5,  # width
            6,  # height
            color=numpy.random.rand(3, 1),
        )
    )
    axes.add_patch(
        patches.Rectangle(
            (0, 6),  # (x,y)
            15,  # width
            13,  # height
            color=numpy.random.rand(3, 1),
        )
    )
    axes.set_xlim(0, width)
    axes.set_ylim(0, height)
    plt.show()
