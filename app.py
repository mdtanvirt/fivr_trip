import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("Trip analysis")
with st.sidebar:
    nav_menu = option_menu("Main Menu", ["Dashboard", "Map", 'Settings'], 
        icons=['clipboard-data', 'map', 'gear'], menu_icon="cast", default_index=0)

if nav_menu == "Dashboard":
    st.write("Analysis Dashboard")

elif nav_menu == "Map":
    st.write("Data exploration with map")

elif nav_menu == "Settings":
    st.write("Raw data")