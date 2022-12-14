from cgitb import grey
from turtle import fillcolor
import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
 
html = """<br>
Volcano name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def color_producer(elev):
    if elev < 2000:
        return "green"
    elif elev < 3000:
        return "orange"
    else:
        return "red" 

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), fill_color=color_producer(el), color=grey, fill_opacity = 0.7))
 
map.add_child(fg)
map.save("Map_html_popup_advanced.html")