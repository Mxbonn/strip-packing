import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random


def visualize(width, height, rectangles):
    """
    Visualization of the a strip of size width x height with the layout of the rectangles.
    The rectangles are annotated with their place in the input list on the figure.

    Parameters
    ----------
    width
        size of the width of the strip

    height
        size of the height of the strip

    rectangles : list of namedtuple('Rectangle', ['x', 'y', 'w', 'h'])
        A list of rectangles. This contains bottom left x and y coordinate and
        the width and height of every rectangle.
    """
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
    for idx, r in enumerate(rectangles):
        axes.add_patch(
            patches.Rectangle(
                (r.x, r.y),  # (x,y)
                r.w,  # width
                r.h,  # height
                color=(random(), random(), random()),
            )
        )
        axes.text(r.x + 0.5 * r.w, r.y + 0.5 * r.h, str(idx))
    axes.set_xlim(0, width)
    axes.set_ylim(0, height)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    plt.savefig('output/visualization.png')
