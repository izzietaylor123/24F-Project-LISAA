import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('GEO Admin Home Page')
st.write('')
st.write('')
st.write(f"Hello {st.session_state['first_name']}, what would you like to do today?")

if st.button('GEO Point of Contact', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_GEO_Contact.py')

if st.button('Current Abroad Programs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Programs.py')

if st.button('Engagement Analytics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Engagement_Analytics.py')

#if st.button("Current Programs Ratings",
             #type='primary',
             #use_container_width=True):
 # st.switch_page('pages/_API_Test.py')

if st.button("Manage Mentors",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Mentor_Management.py')

if st.button("Manage Alerts",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_Alerts_Management.py')
