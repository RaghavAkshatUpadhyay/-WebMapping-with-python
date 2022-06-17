import folium
import pandas

data=pandas.read_csv("volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])
def getcolor(x):
    if x>3000:
        return "red"
    elif x > 1000:
        return "orange"    
    else:
        return "green"    
    
#crating map object

map=folium.Map(location=[80.54,-100.66],zoom_start=6,tiles="Stamen Terrain")
#feature group to keep things organised
fgv=folium.FeatureGroup(name="volcanoes")
#creating markers for the map used to add a marker point on the map
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=str(el),fill=True,fill_color=getcolor(el),fill_opacity=0.7))
fgp=folium.FeatureGroup(name="Popultion")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function= lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")

