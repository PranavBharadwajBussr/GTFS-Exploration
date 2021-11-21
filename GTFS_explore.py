import gtfs_kit as gk
import folium
import webbrowser

def initialize():
    path = 'gtfs1.zip'
    feed = (gk.read_feed(path, dist_units='km'))
    return feed

def displayPlots():
    feed = initialize()
    map1 = feed.map_routes(feed.routes.route_id.iloc[:], include_stops=True)
    map1.save('map1.html')
    webbrowser.open('map1.html')

displayPlots()