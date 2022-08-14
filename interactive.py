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



#manhattan = load_mn()

st.title('AirBnB price estimator')
st.subheader('Enter the specs of your AirBnB, then click your borough: ')

acc = st.slider('accomodates', 1, 10, on_change=callback)
beds = st.slider('beds', 1, 10, on_change=callback)
private_room = st.slider('Is the room private? 1 for yes, 0 for no', 0, 1, on_change=callback)
entire = st.slider('Does the customer get the full place? 1 for yes, 0 for no', 0, 1, on_change=callback)
lat = st.slider("Latitude of the location?", 40.50863, 40.89711, on_change=callback)
lon = st.slider("Longitude of the location?", -73.73825, -74.24135,  on_change=callback)

if st.button(label='Manhattan'):
    manhattan = load_mn()
    xvars = [acc, beds, private_room, entire, lon, lat]
    xdata = {'acc': [acc], 'beds': [beds], 'private_room': [private_room], 'entire': [entire], 'Longitude': [lon], 'Latitude': [lat]}
    X = pd.DataFrame(xdata)


    #fill_in_array = xvars.reshape(-1,1)
    pred = manhattan.predict(X)
    st.write('Your estimated value is: ', pred)
