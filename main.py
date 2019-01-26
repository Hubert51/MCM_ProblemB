import matplotlib.pyplot as plt
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages



class Hospital(object):
    def __init__(self, lat, lon, map,med1=0, med2=0, med3=0 ):
        self.lat = lat
        self.lon = lon
        self.med1 = med1
        self.med2 = med2
        self.med3 = med3
        self.med_list = []
        self.normalize_med()
        # m = Basemap()
        self.xpt, self.ypt = map(lon, lat)



    def normalize_med(self):
        raw = [self.med1, self.med2, self.med3]
        self.med_list = [float(i) / sum(raw) for i in raw]


class Container(object):
    def __init__(self, lat, lon, map):
        self.lat = lat
        self.lon = lon
        # m = Basemap()
        self.xpt, self.ypt = map(lon, lat)



def draw_pie(ax, ratios=[0.4, 0.3, 0.3], X=0, Y=0, size=10000):
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
        # print(xyi)
        ax.scatter([X], [Y], marker=xyi, s=size, facecolor=colors[i])


def draw_container(containers):
    for cont in containers:
        xpt, ypt = m(cont.lon, cont.lat)
        m.plot(xpt, ypt, marker="o", color='c', markersize=12, label='location')  # plot a blue dot there


def cont_hosp_dist(containers, hosps ):
    for cont in containers:
        for hosp in hosps:
            dist = math.sqrt( (cont.xpt-hosp.xpt)**2 + (cont.ypt-hosp.ypt)**2  )
            print("distance is {:}".format(dist))
        print()



def R_func():
    r=robjects.r
    r.source("BoxPacking-master/R/PerformBoxPacking.R")
    import rpy2.rinterface
    # rpy2.rinterface.set_initoptions((b'rpy2', b'--no-save', b'--no-restore', b'--quiet'))
    from rpy2.robjects.packages import importr
    base = importr('base')
    print(base._libPaths())
    packnames = ['BoxPacking']
    utils = importr("utils")
    d = {'print.me': 'print_dot_me', 'print_me': 'print_uscore_me'}
    thatpackage = importr('BoxPacking', robject_translations=d,
                          lib_loc="/Library/Frameworks/R.framework/Versions/3.5/Resources/library")

    # R vector of strings
    from rpy2.robjects.vectors import StrVector

    # Selectively install what needs to be install.
    # We are fancy, just because we can.
    if len(packnames) > 0:
        utils.install_packages(StrVector(packnames))
    r.library("BoxPacking")

    # BoxPacking = rpackages.importr(StrVector("BoxPacking"))

    # BoxPacking = importr('BoxPacking')

    # r("library(BoxPacking)")

# create medical package
# setClass("Med", slots=list(ID="character", Weight="numeric", Box(length = "numeric", height = "numeric", width = "numeric"  )))

# Med1 = new("Med", a = 12, b = 42)

    r("Box1 = Box(length = 14, height = 5, width = 7)")
    r("Box2 = Box(length = 5, height = 8, width = 5) ")
    r("Box3 = Box(length = 12, height = 4, width = 7)")


colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'purple']





if __name__ == '__main__':

    R_func()

    y = np.array( [ 1.27358e+07, 1.26935e+07,     1.26891e+07,     1.2679e+07,     1.26156e+07] )
    x = np.array( [ 8.61409e+06, 8.62274e+06, 8.60544e+06, 8.60859e+06, 8.60308e+06 ] )
    lat = [18.33, 18.22, 18.44, 18.40, 18.47]
    lon = [-65.65, -66.03, -66.07, -66.16, -66.73]

    req = [(1,0,1), [2,0,1], [1,1,0], [2,1,2], [1,0,0]]



    L_lon = -67.5
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
    m = Basemap(resolution='i', projection='merc', llcrnrlat=L_lat,
                urcrnrlat=R_lat, llcrnrlon=L_lon, urcrnrlon=R_lon,lat_0=lat_0, lon_0=lon_0)  # , lat_ts=51.0

    # m.bluemarble()

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

    hosps = []
    for i in range(5):
        hosps.append(Hospital(lat=lat[i], lon=lon[i], map=m,
                              med1=req[i][0], med2=req[i][1],med3=req[i][2]))

    # first lon, second lat
    for hosp in hosps:
        X, Y = m(hosp.lon, hosp.lat)
        # print([hosp.med1, hosp.med2, hosp.med3])
        draw_pie(ax, [hosp.med_list[0], hosp.med_list[1], hosp.med_list[2]], X, Y, size=300)

    # plt.annotate('Jul-24-2012', xy=(0, 0.5),  arrowprops=dict(facecolor='red', shrink=0.05),xycoords='axes fraction' )
    # plt.annotate('Jul-24-2012', xy=(0, 0.5),  arrowprops=dict(facecolor='red', shrink=0.05),xycoords='axes fraction' )
    #
    # plt.text(1000, 1000, r'$\delta$',
    #          {'color': 'k', 'fontsize': 24, 'ha': 'center', 'va': 'center',
    #           'bbox': dict(boxstyle="round", fc="w", ec="k", pad=0.2)})
    # X, Y = m(5.5, 50.8)
    # draw_pie(ax, [0.20, 0.18, 0.62], X, Y, size=250)
    # plt.legend( ["med1", "med2", "med3"], colors=["red", "blue", "green"])

    lon, lat = -67.45, 18.4  # Location of Boulder
    # convert to map projection coords.
    # Note that lon,lat can be scalars, lists or numpy arrays.
    xpt, ypt = m(lon, lat)
    # convert back to lat/lon
    lonpt, latpt = m(xpt, ypt, inverse=True)
    m.plot(xpt, ypt, marker="s", color='r', markersize=12, label='Med1')  # plot a blue dot there
    m.plot(xpt, ypt, marker="s", color='b', markersize=12, label='Med2')  # plot a blue dot there
    m.plot(xpt, ypt, marker="s", color='g', markersize=12, label='Med3')  # plot a blue dot there
    m.plot(xpt, ypt, marker="s", color='w', markersize=12)  # plot a blue dot there

    containers = [ Container(lon=-66.2745, lat=18.3825, map=m), Container(lon=-65.9775, lat= 18.3475,map=m)  ]
    draw_container(containers)

    dist = math.sqrt((containers[0].xpt - hosps[1].xpt) ** 2 + (containers[0].ypt - hosps[1].ypt) ** 2)
    print("distance is {:}".format(dist))

    cont_hosp_dist(containers, hosps)



    # put some text next to the dot, offset a little bit
    # (the offset is in map projection coordinates)
    # plt.text(xpt , ypt , 'Med1')
    plt.legend()

    plt.show()

