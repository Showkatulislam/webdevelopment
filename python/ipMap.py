import geocoder

import folium

g=geocoder.ip('me')

myaddress=g.latlng

print(myaddress)


my_map1=folium.Map(location=myaddress,zoom_start=12)


