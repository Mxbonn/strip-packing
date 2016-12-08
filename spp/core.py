from copy import deepcopy
from collections import namedtuple
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


def hprg(width, rectangles):
    result = [None] * len(rectangles)
    remaining = deepcopy(rectangles)
    logger.debug('Original itens : {}'.format(rectangles))
    for idx, r in enumerate(remaining):
        if r[0] > r[1]:
            remaining[idx][0], remaining[idx][1] = remaining[idx][1], remaining[idx][0]
    logger.debug('Items after swapping: {}'.format(remaining))
    sorted_indices = sorted(range(len(remaining)), key=lambda x: remaining[x][0])
    logger.debug('Indices of remaining items sorted by decreasing width: {}'.format(sorted_indices))
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

    return H, result


def recursive_packing(x, y, w, h, remaining, indices, result):
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
            recursive_packing(x + omega, y, w - omega, h)
#        elif priority == 4:
