import folium
import pandas

data = pandas.read_csv("Volcanoes.txt",sep=";",encoding = "utf-8-sig")

lat = data["LAT"]
lon = data["LON"]
name = data["NAME"]
elev = data["ELEV"]

def color_producer(elev):
    if elev < 2000:
        return "green"
    elif elev < 3000:
        return "orange"
    else:
        return "red" 

map = folium.Map(location=[45, -120], zoom_start=8, tiles="Stamen Terrain")

fgp = folium.FeatureGroup(name = "Population")    
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),  
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 else 'yellow' 
if 20000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
else 'red'}, tooltip = folium.features.GeoJsonTooltip(fields=['NAME','AREA','POP2005'],
aliases=['NAME:','AREA:','POPULATION:'],
style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))))

fgv = folium.FeatureGroup(name = "Volcanoes")
for ln, lt, name1, elv in zip(lon , lat, name, elev):
    
    fgv.add_child(folium.CircleMarker(location = [lt ,ln], popup =name1 + " " + str(elv) + " m", 
    color='grey',fill_color=color_producer(elv), fill_opacity=.7 , radius=6))



map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")