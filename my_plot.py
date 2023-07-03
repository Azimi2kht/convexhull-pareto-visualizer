from matplotlib import pyplot as plt


def my_plot(points, hull):
    plt.figure()
    plt.plot(hull[:, 0], hull[:, 1], "c", picker=5)
    plt.plot([hull[-1, 0], hull[0, 0]], [hull[-1, 1], hull[0, 1]], "c", picker=5)
    plt.plot(points[:, 0], points[:, 1], "o", color="k")
    plt.axis("on")
    plt.show()
