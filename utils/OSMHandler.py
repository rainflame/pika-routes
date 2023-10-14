import osmium 
from shapely.geometry import Point, LineString, Polygon

# Define a class to handle OSM data parsing
class OSMHandler(osmium.SimpleHandler):
    def __init__(self):
        super(OSMHandler, self).__init__()
        self.hiking_trails = []
        self.lakes = []
        self.trailheads = []
        self.bodies = ['lake', 'reservoir', 'pond']


    def way(self, w):
        if 'highway' in w.tags and w.tags['highway'] == 'trailhead':
            if w.location.valid():
                trailhead_meta = {
                    'id': w.id,
                    'name': w.tags['name'] if 'name' in w.tags else '',
                }
                self.trailheads.append((Point(w.location.lat, w.location.lon), trailhead_meta))

        if 'highway' in w.tags and w.tags['highway'] == 'path':
            trail_coords = []
            for n in w.nodes:
                if n.location.valid():
                    trail_coords.append(Point(n.location.lat, n.location.lon))
            if len(trail_coords) > 1:
                trail_line = LineString(trail_coords)
                trail_meta = {
                    'id': w.id,
                    'name': w.tags['name'] if 'name' in w.tags else '',
                }
                self.hiking_trails.append((trail_line, trail_meta))

       
        if 'natural' in w.tags and w.tags['natural'] == 'water' and 'water' in w.tags and w.tags['water'] in self.bodies:
            lake_coords = []
            for n in w.nodes:
                if n.location.valid():
                    lake_coords.append(Point(n.location.lat, n.location.lon))
            if len(lake_coords) > 1:
                lake_meta = {
                    'id': w.id,
                    'name': w.tags['name'] if 'name' in w.tags else '',
                }
                line = LineString(lake_coords)
                if line.is_closed:
                    polygon = Polygon(lake_coords)
                    self.lakes.append((polygon, lake_meta))