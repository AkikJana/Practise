import folium
import pandas
data=pandas.read_csv("Volcanoes_USA.txt")

def color_prod(elevation):
	if elevation<1000:
		return 'green'
	elif 1000 <=elevation<3000:
		return 'orange'
	else:
		return 'red'

#icon_fa='fa-map-marker-alt'
map=folium.Map(location=[22, 88],tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="Population")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elevation=list(data["ELEV"])
r=len(lat)
for lt,ln,nm,elev in zip(lat,lon,name,elevation):
	fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=nm,fill_color=color_prod(elev),color='grey',fill_opacity=0.7))
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("maptest.html")