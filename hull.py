import numpy as np
import matplotlib.pyplot as plt


def turn_right(p1, p2, p3):
    if (p3[1] - p1[1]) * (p2[0] - p1[0]) >= (p2[1] - p1[1]) * (p3[0] - p1[0]):
        return False
    return True


def graham_scan(p):
    p.sort()
    lu = [p[0], p[1]]

    for i in range(2, len(p)):
        lu.append(p[i])
        while len(lu) > 2 and not turn_right(lu[-1], lu[-2], lu[-3]):
            del lu[-2]
    ll = [p[-1], p[-2]]

    for i in range(len(p) - 3, -1, -1):
        ll.append(p[i])
        while len(ll) > 2 and not turn_right(ll[-1], ll[-2], ll[-3]):
            del ll[-2]
    del ll[0]
    del ll[-1]
    l = lu + ll
    return np.array(l)
