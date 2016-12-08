import matplotlib.pyplot as plt
import matplotlib.patches as patches
from random import random


def visualize(width, height, rectangles):
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
