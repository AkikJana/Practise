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

icon_fa='fa-map-marker-alt'
map=folium.Map(location=[22, 88],tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="my_map")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elevation=list(data["ELEV"])
r=len(lat)
for lt,ln,nm,elev in zip(lat,lon,name,elevation):
	fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=nm,fill_color=color_prod(elev),color='grey',fill_opacity=0.7))
map.add_child(fg)
map.save("maptest.html")