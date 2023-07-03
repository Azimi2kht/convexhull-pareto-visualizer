from matplotlib import pyplot as plt

pareto_color = "#FF2171"
convexhull_color = "#A2FF86"


def my_plot(points, hull, p):
    plt.figure()
    plt.plot(hull[:, 0], hull[:, 1], color=convexhull_color, picker=5)
    plt.plot(
        [hull[-1, 0], hull[0, 0]],
        [hull[-1, 1], hull[0, 1]],
        color=convexhull_color,
        picker=5,
    )
    plt.fill(hull[:, 0], hull[:, 1], color=convexhull_color, label="feasable area")
    plt.plot(points[:, 0], points[:, 1], ".", color="k")
    plt.plot(p[:, 0], p[:, 1], color=pareto_color, picker=5, label="pareto points")
    plt.plot(p[:, 0], p[:, 1], "o", color=pareto_color)
    plt.axis("on")
    plt.legend()
    plt.show()
