import re


def get_points():
    points = []
    while True:
        line = input().split(" ")
        if "end" in line:
            break
        for s in line:
            points.append(tuple([int(s) for s in re.findall(r"\d+", s)]))
    return points
