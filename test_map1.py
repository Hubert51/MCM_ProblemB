from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    # # setup Lambert Conformal basemap.
    # m = Basemap(width=1200000,height=900000,projection='lcc',
    #             resolution='c',lat_1=18.,lat_2=19.,lat_0=-65.,lon_0=-67.)
    # # draw coastlines.
    # m.drawcoastlines()
    # # draw a boundary around the map, fill the background.
    # # this background will end up being the ocean color, since
    # # the continents will be drawn on top.
    # m.drawmapboundary(fill_color='aqua')
    # # fill continents, set lake color same as ocean color.
    # m.fillcontinents(color='coral',lake_color='aqua')
    # # draw parallels and meridians.
    # # label parallels on right and top
    # # meridians on bottom and left
    # parallels = np.arange(0.,81,10.)
    # # labels = [left,right,top,bottom]
    # m.drawparallels(parallels,labels=[False,True,True,False])
    # meridians = np.arange(10.,351.,20.)
    # m.drawmeridians(meridians,labels=[True,False,False,True])
    # plt.show()

    L_lon = -67.2
    L_lat = 17.93
    R_lon = -65.6
    R_lat = 18.5

    lon_0 = (L_lon + R_lon)/2
    lat_0 = (L_lat + R_lat)/2


    map = Basemap(llcrnrlon=L_lon, llcrnrlat=L_lat, urcrnrlon=R_lon, urcrnrlat=R_lat,
                  resolution='h', projection='cass', lat_0=lat_0, lon_0=lon_0)

    map.bluemarble()
    map.drawcoastlines()

    #
    # map = Basemap(llcrnrlon=3.75, llcrnrlat=39.75, urcrnrlon=4.35, urcrnrlat=40.15, epsg = 5520)
    # # http://server.arcgisonline.com/arcgis/rest/services
    # map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels=1500, verbose=True)
    # plt.show()


    # map = Basemap(llcrnrlon=L_lon, llcrnrlat=L_lat, urcrnrlon=R_lon, urcrnrlat=R_lat,
    #                 epsg = 5520)

    # map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels=5000, verbose=True)
    # map.drawmapboundary(fill_color='aqua')
    # map.fillcontinents(color='#cc9955', lake_color='aqua')
    # map.drawcoastlines()
    #
    # map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')
    #
    # map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize=14)

    plt.show()