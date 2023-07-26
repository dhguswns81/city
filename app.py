import streamlit as st
from streamlit_folium import st_folium
import folium
m = folium.Map(location = [35.165931, 129.135154], zoom_start = 16)
folium.Marker(
    [35.165931, 129.135154],
    popup = "Liberty Bell",
    tooltip = "Liberty Bell"
).add_to(m)

st_data = st_folium(m, width = 725)
