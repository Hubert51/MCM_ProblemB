import matplotlib.pyplot as plt
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class Hospital(object):
    def __init__(self, lat, lon, med1=0, med2=0, med3=0 ):
        self.lat = lat
        self.lon = lon
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3
        self.med_list = []
        self.normalize_med()



    def normalize_med(self):
        raw = [self.med1, self.med2, self.med3]
        self.med_list = [float(i) / sum(raw) for i in raw]



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


colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'purple']


if __name__ == '__main__':
    y = np.array( [ 1.27358e+07, 1.26935e+07,     1.26891e+07,     1.2679e+07,     1.26156e+07] )
    x = np.array( [ 8.61409e+06, 8.62274e+06, 8.60544e+06, 8.60859e+06, 8.60308e+06 ] )
    lat = [18.33, 18.22, 18.44, 18.40, 18.47]
    lon = [-65.65, -66.03, -66.07, -66.16, -66.73]

    req = [(1,0,1), [2,0,1], [1,1,0], [2,1,2], [1,0,0]]

    hosps = []
    for i in range(5):
        hosps.append(Hospital(lat=lat[i], lon=lon[i],
                              med1=req[i][0], med2=req[i][1],med3=req[i][2]))





    L_lon = -67.3
    L_lat = 17.9
    R_lon = -65.6
    R_lat = 18.55

    lon_0 = (L_lon + R_lon) / 2
    lat_0 = (L_lat + R_lat) / 2

    fig = plt.figure(figsize=(11.7, 8.3))
    # Custom adjust of the subplots
    plt.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.05, wspace=0.15, hspace=0.05)
    ax = plt.subplot(111)
    # Let's create a basemap around Belgium
    m = Basemap(resolution=None, projection='lcc', llcrnrlat=L_lat,
                urcrnrlat=R_lat, llcrnrlon=L_lon, urcrnrlon=R_lon,lat_0=lat_0, lon_0=lon_0)  # , lat_ts=51.0

    m.bluemarble()

    # m.fillcontinents(color='#cc9955', lake_color='aqua')
    # m.drawcoastlines()

    # map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')
    #
    # map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize=14)

    m.drawcountries(linewidth=0.5)
    m.drawcoastlines(linewidth=0.5)

    m.drawparallels(np.arange(17.9, 18.6, 0.1), labels=[1, 0, 0, 0], color='black', dashes=[1, 0], labelstyle='+/-',
                    linewidth=0.05)  # draw parallels
    m.drawmeridians(np.arange(-67.1, -65.5, 0.1), labels=[0, 0, 0, 1], color='black', dashes=[1, 0], labelstyle='+/-',
                    linewidth=0.05)  # draw meridians

    # first lon, second lat
    for hosp in hosps:
        X, Y = m(hosp.lon, hosp.lat)
        print([hosp.med1, hosp.med2, hosp.med3])
        draw_pie(ax, [hosp.med_list[0], hosp.med_list[1], hosp.med_list[2]], X, Y, size=300)

    # X, Y = m(5.5, 50.8)
    # draw_pie(ax, [0.20, 0.18, 0.62], X, Y, size=250)
    plt.show()

