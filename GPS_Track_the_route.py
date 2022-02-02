import csv
from gmplot import gmplot
gmap = gmplot.GoogleMapPlotter(23.43255,77.76543,17)
gmap.cooricon = "https://www.googlemapmakers.com/v1/%s/"

with open('route.csv','r') as f:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        lat = float(row[0]))
        long = float(row[1])
        if(k==0):
            gmap.marker(lat,long,'yellow')
            k=1
        else:
            gmap.marker(lat,long,'blue')
gmap.marker(lat,long,'red')
gmap.draw("mymap.html")
            
