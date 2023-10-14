from shapely.ops import transform
import pyproj

wgs84 = "EPSG:4326"
# Oregon uses Zone 10. Zone 10 is ESPG:32610: https://epsg.io/32610.
utm10 = "EPSG:32610"

def project_point_to_meters(point):
    project = pyproj.Transformer.from_crs(wgs84, utm10, always_xy=False).transform
    point_utm = transform(project, point)
    return point_utm

def project_line_to_meters(line):
    project = pyproj.Transformer.from_crs(wgs84, utm10, always_xy=False).transform
    line_utm = transform(project, line)
    return line_utm

def project_poly_to_meters(polygon):
    project = pyproj.Transformer.from_crs(wgs84, utm10, always_xy=False).transform
    polygon_utm = transform(project, polygon)
    return polygon_utm

def calculate_buffer(polygon, buffer):
    project = pyproj.Transformer.from_crs(wgs84, utm10, always_xy=False).transform
    polygon_utm = transform(project, polygon)
    # buffer the polygon
    polygon_utm_buffer = polygon_utm.buffer(buffer)
    # transform the polygon back to WGS84
    project = pyproj.Transformer.from_crs(utm10, wgs84, always_xy=False).transform
    polygon_buffer = transform(project, polygon_utm_buffer)
    return polygon_buffer
