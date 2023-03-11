# streamlit place picker test
# Pick a place and get ECHO facilities
#https://docs.streamlit.io/library/get-started/create-an-app 

import pandas as pd
import urllib.parse
from hello import hello_world

# Map
from ipyleaflet import Map, Marker, basemaps, basemap_to_tiles
m = Map(
    basemap=basemap_to_tiles(basemaps.CartoDB.Positron),
    center=(40, -74), 
    zoom=7
  ) # Default to NJ

marker = Marker(location=(40, -74), draggable=True) # defaults to New Jersey for SDWA project
m.add_layer(marker);

display(m)

# Goal = get marker, get facilities near marker, get violations 
def load_data(sql):
  url= 'https://portal.gss.stonybrook.edu/echoepa/?query='
  data_location = url + urllib.parse.quote_plus(sql) + '&pg'
  data = pd.read_csv(data_location, encoding='iso-8859-1', dtype={"REGISTRY_ID": "Int64"})
  #data["LAT"] = data["FAC_LAT"]
  #data["LON"] = data["FAC_LONG"]
  # add data to map
  return data
sql= 'select * from "ECHO_EXPORTER" where "FAC_CITY" = \'PEEKSKILL\''

# Streamlit section
import streamlit as st
"""
import streamlit as st
data_load_state = st.text('Loading data...')
message = hello_world()
data_load_state.text(message)
