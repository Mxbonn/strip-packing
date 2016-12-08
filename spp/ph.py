from copy import deepcopy
from collections import namedtuple
import sys
import logging

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_logger = logging.StreamHandler()
console_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
console_logger.setFormatter(formatter)
logger.addHandler(console_logger)

Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])


def phspprg(width, rectangles):
    """
    The PH heuristic for the Strip Packing Problem. This is the RG variant, which means that rotations by
    90 degrees are allowed and that there is a guillotine constraint.

    Parameters
    ----------
    width
        The width of the strip.

    rectangles
        List of list containing width and height of every rectangle, [[w_1, h_1], ..., [w_n,h_h]].
        It is assumed that all rectangles can fit into the strip.

    Returns
    -------
    height
        The height of the strip needed to pack all the items.
    rectangles : list of namedtuple('Rectangle', ['x', 'y', 'w', 'h'])
        A list of rectangles, in the same order as the input list. This contains bottom left x and y coordinate and
        the width and height (which can be flipped compared to input).

    """
    logger.debug('The original array: {}'.format(rectangles))
    result = [None] * len(rectangles)
    remaining = deepcopy(rectangles)
    for idx, r in enumerate(remaining):
        if r[0] > r[1]:
            remaining[idx][0], remaining[idx][1] = remaining[idx][1], remaining[idx][0]
    logger.debug('Swapped some widths and heigt with the following result: {}'.format(remaining))
    sorted_indices = sorted(range(len(remaining)), key=lambda x: -remaining[x][0])
    logger.debug('The sorted indices: {}'.format(sorted_indices))
    sorted_rect = [remaining[idx] for idx in sorted_indices]
    logger.debug('The sorted array is: {}'.format(sorted_rect))
    x, y, w, h, H = 0, 0, 0, 0, 0
    while sorted_indices:
        idx = sorted_indices.pop(0)
        r = remaining[idx]
        if r[1] > width:
            result[idx] = Rectangle(x, y, r[0], r[1])
            x, y, w, h, H = r[0], H, width - r[0], r[1], H + r[1]
        else:
            result[idx] = Rectangle(x, y, r[1], r[0])
            x, y, w, h, H = r[1], H, width - r[1], r[0], H + r[0]
        recursive_packing(x, y, w, h, remaining, sorted_indices, result)
        x, y = 0, H
    logger.debug('The resulting rectangles are: {}'.format(result))

    return H, result


def recursive_packing(x, y, w, h, remaining, indices, result):
    """Helper function to recursively fit a certain area."""
    priority = 6
    for idx in indices:
        for D in range(0, 2):
            if priority > 1 and remaining[idx][(0 + D) % 2] == w and remaining[idx][(1 + D) % 2] == h:
                priority, orientation, best = 1, D, idx
                break
            elif priority > 2 and remaining[idx][(0 + D) % 2] == w and remaining[idx][(1 + D) % 2] < h:
                priority, orientation, best = 2, D, idx
            elif priority > 3 and remaining[idx][(0 + D) % 2] < w and remaining[idx][(1 + D) % 2] == h:
                priority, orientation, best = 3, D, idx
            elif priority > 4 and remaining[idx][(0 + D) % 2] < w and remaining[idx][(1 + D) % 2] < h:
                priority, orientation, best = 4, D, idx
            elif priority > 5:
                priority, orientation, best = 5, D, idx
    if priority < 5:
        if orientation == 0:
            omega, d = remaining[best][0], remaining[best][1]
        else:
            omega, d = remaining[best][1], remaining[best][0]
        result[best] = Rectangle(x, y, omega, d)
        indices.remove(best)
        if priority == 2:
            recursive_packing(x, y + d, w, h - d, remaining, indices, result)
        elif priority == 3:
            recursive_packing(x + omega, y, w - omega, h, remaining, indices, result)
        elif priority == 4:
            min_w = sys.maxsize
            min_h = sys.maxsize
            for idx in indices:
                min_w = min(min_w, remaining[idx][0])
                min_h = min(min_h, remaining[idx][1])
            # Because we can rotate:
            min_w = min(min_h, min_w)
            min_h = min_w
            if w - omega < min_w:
                recursive_packing(x, y + d, w, h - d, remaining, indices, result)
            elif h - d < min_h:
                recursive_packing(x + omega, y, w - omega, h, remaining, indices, result)
            elif omega < min_w:
                recursive_packing(x + omega, y, w - omega, d, remaining, indices, result)
                recursive_packing(x, y + d, w, h - d, remaining, indices, result)
            else:
                recursive_packing(x, y + d, omega, h - d, remaining, indices, result)
                recursive_packing(x + omega, y, w - omega, h, remaining, indices, result)

