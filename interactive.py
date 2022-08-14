from operator import mod
import streamlit as st
import pickle
import pandas as pd

#Help from https://www.youtube.com/watch?v=XWKAt1QlRyI

def callback():
    st.session_state_button_clicked = True

def load_mn():
  with open('models/manhattan_pickle.pkl', 'rb') as f:
    the_model = pickle.load(f)
  return the_model

def load_si():
    with open('models/staten_island_pickle.pkl', 'rb') as f:
      the_model = pickle.load(f)
    return the_model

def load_bx():
    with open('models/bronx_pickle.pkl', 'rb') as f:
      the_model = pickle.load(f)
    return the_model

def load_bk():
    with open('models/brooklyn_pickle.pkl', 'rb') as f:
      the_model = pickle.load(f)
    return the_model

def load_qu():
    with open('models/queens_pickle.pkl', 'rb') as f:
      the_model = pickle.load(f)
    return the_model

st.title('AirBnB price estimator')
st.subheader('Enter the specs of your AirBnB, then click your borough: ')

acc = st.slider('accomodates', 1, 10, on_change=callback)
beds = st.slider('beds', 1, 10, on_change=callback)
private_room = st.slider('Is the room private? 1 for yes, 0 for no', 0, 1, on_change=callback)
entire = st.slider('Does the customer get the full place? 1 for yes, 0 for no', 0, 1, on_change=callback)
lat = st.slider("Latitude of the location?", 40.50863, 40.89711, on_change=callback)
lon = st.slider("Longitude of the location?", -73.73825, -74.24135,  on_change=callback)
max_ni = st.slider("Maximum Nights Allowed", 1, 10000,  on_change=callback)
host_id = st.slider('Is host identity verified? 1 for yes, 0 for no', 0, 1, on_change=callback)
host_hour = st.slider('Does the respond within a few hour? 1 for yes, 0 for no', 0, 1, on_change=callback)
host_super = st.slider('Is the host a superhost? 1 for yes, 0 for no', 0, 1, on_change=callback)

if st.button(label='Manhattan'):
    manhattan = load_mn()
    xdata = {'acc': [acc], 'beds': [beds], 'private_room': [private_room], 'entire': [entire], 'Longitude': [lon], 'Latitude': [lat]}
    X = pd.DataFrame(xdata)
    pred = manhattan.predict(X)
    st.write('Your estimated value is: ', pred)

if st.button(label='Staten Island'):
    staten_island = load_si()
    xdata = {'beds': [beds], 'acc': [acc], 'Latitude': [lat]}
    X = pd.DataFrame(xdata)
    pred = staten_island.predict(X)
    st.write('Your estimated value is: ', pred)

if st.button(label='Bronx'):
    bronx = load_bx()
    xdata = {'entire': [entire], 'acc': [acc], 'private_room': [private_room], 'max_ni': [max_ni], 'Latitude': [lat]}
    X = pd.DataFrame(xdata)
    pred = bronx.predict(X)
    st.write('Your estimated value is: ', pred)

if st.button(label='Brooklyn'):
    brooklyn = load_bk()
    xdata = {'acc': [acc], 'beds': [beds], 'entire': [entire], 'private_room': [private_room], 'Longitude': [lon]}
    X = pd.DataFrame(xdata)
    pred = brooklyn.predict(X)
    st.write('Your estimated value is: ', pred)

if st.button(label='Queens'):
    queens = load_qu()
    xdata = {'acc': [acc], 'beds': [beds], 'entire': [entire], 'private_room': [private_room], 'host_id': [host_id], 'host_hour': [host_hour], 'host_super': [host_super]}
    X = pd.DataFrame(xdata)
    pred = queens.predict(X)
    st.write('Your estimated value is: ', pred)
