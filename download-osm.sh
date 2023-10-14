#!/bin/bash

# Define the Overpass API URL
OVERPASS_API_URL="https://overpass-api.de/api/interpreter"

# Define the bounding box coordinates
BBOX="43.41701888881106,-122.18719482421876,44.623708968901205,-120.09704589843751"

# Define the Overpass QL query
QUERY="[out:protobuf];[bbox:$BBOX];(node;way;relation;);out geom;"

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "data=$QUERY" "$OVERPASS_API_URL" --output data/extract.osm

# convert to .pbf
osmium cat -o data/extract.osm.pbf data/extract.osm

