import re


def get_points():
    points = []
    while True:
        line = input().strip().split(" ")
        if "end" in line:
            break
        for s in line:
            points.append(
                tuple([float(s) for s in re.findall(r"[-+]?\d*\.\d+|\d+", s)])
            )
    return points
