import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import pandas as pd
import pickle
import PIL.Image

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi'
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah']
st.title('IPL win predictor')

col,col1,col0,col2 = st.columns([0.5,3,0.5,3])
with col:
    image = PIL.Image.open('cricket-bat.png')
    resized_img = image.resize((50, 50))
    st.image(resized_img)
with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
    if batting_team == 'Chennai Super Kings':
        image = PIL.Image.open('chennai super kings.png')
        st.image(image)
    if batting_team == 'Sunrisers Hyderabad':
        image = PIL.Image.open('sunrises_hyderabad.png')
        st.image(image)
    if batting_team == 'Mumbai Indians':
        image = PIL.Image.open('Mumbai_Indians.png')
        st.image(image)
    if batting_team == 'Royal Challengers Bangalore':
        image = PIL.Image.open('royal_challengers.png')
        st.image(image)
    if batting_team == 'Kolkata Knight Riders':
        image = PIL.Image.open('Kolkata night riders.png')
        st.image(image)
    if batting_team == 'Kings XI Punjab':
        image = PIL.Image.open('Kings XI Punjab.png')
        st.image(image)
    if batting_team == 'Rajasthan Royals':
        image = PIL.Image.open('rajasthan royals.png')
        st.image(image)
    if batting_team == 'Delhi Capitals':
        image = PIL.Image.open('delhi capitals.png')
        st.image(image)
with col0:
    image = PIL.Image.open('ball.png')
    resized_img = image.resize((50, 50))
    st.image(resized_img)

with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))
    if bowling_team == 'Chennai Super Kings':
        image = PIL.Image.open('chennai super kings.png')
        st.image(image)
    if bowling_team == 'Sunrisers Hyderabad':
        image = PIL.Image.open('sunrises_hyderabad.png')
        st.image(image)
    if bowling_team == 'Mumbai Indians':
        image = PIL.Image.open('Mumbai_Indians.png')
        st.image(image)
    if bowling_team == 'Royal Challengers Bangalore':
        image = PIL.Image.open('royal_challengers.png')
        st.image(image)
    if bowling_team == 'Kolkata Knight Riders':
        image = PIL.Image.open('Kolkata night riders.png')
        st.image(image)
    if bowling_team == 'Kings XI Punjab':
        image = PIL.Image.open('Kings XI Punjab.png')
        st.image(image)
    if bowling_team == 'Rajasthan Royals':
        image = PIL.Image.open('rajasthan royals.png')
        st.image(image)
    if bowling_team == 'Delhi Capitals':
        image = PIL.Image.open('delhi capitals.png')
        st.image(image)


selected_city = st.selectbox('Select the host city',sorted(cities))

target = st.number_input('Enter the target')
pipe = pickle.load(open('pipe.pkl','rb'))
col3,col4,col5 = st.columns(3)

with col3:
    scores = st.number_input('Current score')
with col4:
    wickets = st.number_input('Wickets out')
with col5:
    overs =  st.number_input('Overs completed')

if st.button('Predict Probablity'):
    runs_left = target - scores
    balls_left  = 120 - 6 * overs
    wickets = 10 - wickets
    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'runs left': [runs_left], 'balls left': [balls_left], 'wickets left': [wickets],
                             'total_runs_y': [target]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
