import sys


def sgvcp(width, height, rectangles, g_max=1000, h_max=None, n_0=None):
    if h_max is None:
        h_max = width
    if n_0 is None:
        n_0 = 100 if rectangles.size() < 500 else 200

    # SGVCP step 1
    c = []
    for w, h in rectangles:
        c.append(w * h)
    g = 0
    H_best = sys.maxsize

    while(g < g_max):  # step 2
        # step 3
        g += 1
        n_left = rectangles.size()
        k = 0
        # TODO: let all items be remaining ones
