import folium
# python library to create render map from python to html/css/js
import pandas as pd
# library to build dataframe from csv file

data_frame = pd.read_csv('Volcanoes.txt')
lat = list(data_frame["LAT"])
lon = list(data_frame["LON"])
elev = list(data_frame["ELEV"])
name = list(data_frame["NAME"])
loc = list(data_frame["LOCATION"])
volcano_type = list(data_frame["TYPE"])


# function to denote color based on elevation
def elevation_marker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2500:
        return 'orange'
    else:
        return 'red'


# render map
m = folium.Map(
    location=[38.6, -100.0],
    zoom_start=4,
    tiles=
    'https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
    attr='My Data Attribution')

# create geojson var to display coordinates overlay
# went this route instaed of polygon object as it was simpler with available geo.json

geojson = r'geo.json'
folium.GeoJson(geojson, name="geojson").add_to(m)
# var to setup for-loop
fg = folium.FeatureGroup(name="Volcano Map")

# loop through variables to create markers on map
for lt, ln, el, nm, lo, tp in zip(lat, lon, elev, name, loc, volcano_type):
    fg.add_child(
        folium.CircleMarker(location=[lt, ln],
                            radius=6,
                            popup=nm + ", " + lo + ", Elevation " + str(el) +
                            "m",
                            tooltip=nm + ", " + lo + ", " + tp,
                            fill_color=elevation_marker(el),
                            color=elevation_marker(el),
                            fill_opacity=0.7))

m.add_child(fg)

m.save("index.html")