"""
===================================
Scatter plot with pie chart markers
===================================

This example makes custom 'pie charts' as the markers for a scatter plot.

Thanks to Manuel Metz for the example


import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # first define the ratios
    r1 = 0.2       # 20%
    r2 = r1 + 0.4  # 40%

    # define some sizes of the scatter marker
    sizes = np.array([60, 80, 120])

    # calculate the points of the first pie marker
    #
    # these are just the origin (0,0) +
    # some points on a circle cos,sin
    x = [0] + np.cos(np.linspace(0, 2 * np.pi * r1, 10)).tolist()
    y = [0] + np.sin(np.linspace(0, 2 * np.pi * r1, 10)).tolist()
    xy1 = np.column_stack([x, y])
    s1 = np.abs(xy1).max()

    x = [0] + np.cos(np.linspace(2 * np.pi * r1, 2 * np.pi * r2, 10)).tolist()
    y = [0] + np.sin(np.linspace(2 * np.pi * r1, 2 * np.pi * r2, 10)).tolist()
    xy2 = np.column_stack([x, y])
    s2 = np.abs(xy2).max()

    x = [0] + np.cos(np.linspace(2 * np.pi * r2, 2 * np.pi, 10)).tolist()
    y = [0] + np.sin(np.linspace(2 * np.pi * r2, 2 * np.pi, 10)).tolist()
    xy3 = np.column_stack([x, y])
    s3 = np.abs(xy3).max()

    fig, ax = plt.subplots()
    # ax.scatter(range(3), range(3), marker=xy1,
    #            s=s1 ** 2 * sizes, facecolor='blue')
    # ax.scatter(range(3), range(3), marker=xy2,
    #            s=s2 ** 2 * sizes, facecolor='green')
    # ax.scatter(range(3), range(3), marker=xy3,
    #            s=s3 ** 2 * sizes, facecolor='red')

    ax.scatter(range(3), range(3), marker=xy1,
               s=s1 ** 10 * sizes, facecolor='blue')
    ax.scatter(range(3), range(3), marker=xy2,
               s=s2 ** 10 * sizes, facecolor='green')
    ax.scatter(range(3), range(3), marker=xy3,
               s=s3 ** 10 * sizes, facecolor='red')

    plt.show()

    #############################################################################
    #
    # ------------
    #
    # References
    #
    #
    # The use of the following functions, methods, classes and modules is shown
    # in this example:
    """

#
# BaseMap example by geophysique.be
# tutorial 05

"""
Using :
-- An example makes custom 'pie charts' as the markers for a scatter plot
-- Thanks to Manuel Metz for the example
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'purple']


def draw_pie(ax, ratios=[0.4, 0.3, 0.3], X=0, Y=0, size=1000):
    N = len(ratios)

    xy = []

    start = 0.
    for ratio in ratios:
        x = [0] + np.cos(np.linspace(2 * math.pi * start, 2 * math.pi * (start + ratio), 30)).tolist()
        y = [0] + np.sin(np.linspace(2 * math.pi * start, 2 * math.pi * (start + ratio), 30)).tolist()
        xy1 = np.column_stack([x, y])
        xy.append(xy1)
        start += ratio

    for i, xyi in enumerate(xy):
        print(xyi)
        ax.scatter([X], [Y], marker=xyi, s=size, facecolor=colors[i])

if __name__ == '__main__':

    L_lon = -67.2
    L_lat = 17.93
    R_lon = -65.6
    R_lat = 18.5

    lon_0 = (L_lon + R_lon)/2
    lat_0 = (L_lat + R_lat)/2



    fig = plt.figure(figsize=(11.7, 8.3))
    # Custom adjust of the subplots
    plt.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.05, wspace=0.15, hspace=0.05)
    ax = plt.subplot(111)
    # Let's create a basemap around Belgium
    m = Basemap(resolution='i', projection='merc', llcrnrlat=49.0, urcrnrlat=52.0, llcrnrlon=1., urcrnrlon=8.0, lat_ts=51.0)
    m.drawcountries(linewidth=0.5)
    m.drawcoastlines(linewidth=0.5)

    m.drawparallels(np.arange(49., 53., 1.), labels=[1, 0, 0, 0], color='black', dashes=[1, 0], labelstyle='+/-',
                    linewidth=0.2)  # draw parallels
    m.drawmeridians(np.arange(1., 9., 1.), labels=[0, 0, 0, 1], color='black', dashes=[1, 0], labelstyle='+/-',
                    linewidth=0.2)  # draw meridians

    X, Y = m(4.5, 50.5)
    draw_pie(ax, [0.4, 0.2, 0.4], X, Y, size=300)

    X, Y = m(5.5, 50.8)
    draw_pie(ax, [0.20, 0.18, 0.62], X, Y, size=250)

    plt.show()

