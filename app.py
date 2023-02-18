import streamlit as st
import pickle as pkl
import pandas as pd

button_style = '''
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
'''


teams = ['','Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']


cities = ['','Kolkata', 'Bangalore', 'Mumbai', 'Delhi', 'Jaipur', 'Sharjah',
       'Centurion', 'Mohali', 'Hyderabad', 'Johannesburg', 'Dharamsala',
       'Chandigarh', 'East London', 'Chennai', 'Ahmedabad', 'Durban',
       'Bloemfontein', 'Visakhapatnam', 'Ranchi', 'Bengaluru',
       'Abu Dhabi', 'Raipur', 'Cape Town', 'Pune', 'Nagpur',
       'Port Elizabeth', 'Indore', 'Cuttack', 'Kimberley']

pipe = pkl.load(open('pipe.pkl','rb'))

st.image("IPL.jpg", width=100)
st.title('IPL Win Prdicator')

col1 ,col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select The Batting Team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select The Bowling Team',sorted(teams))


selected_city = st.selectbox('Select Host City',sorted(cities))

target = st.number_input('Target', min_value=0,step=1)

col3,col4,col5= st.columns(3)

with col3:
    score = st.number_input('Score', min_value=0,max_value=target,step=1)
with col4:
    overs = st.number_input('Overs Completed', min_value=0, max_value=20, step=1)
with col5:
    wickets = st.number_input('Wicket Out', min_value=0,max_value=10,step=1)


if batting_team==bowling_team:
    st.markdown('##### Batting Team and Bowling Team Cannot be Same')
elif st.button('Predict'):
    runs_left = target - score
    balls_left = 120 - overs*6
    wickets = 10- wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],
    'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],
    'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]
    st.write('''
    





    
    
    ''')
    st.markdown(f"##### {batting_team} "+ '- ' + str(round(win*100))+'%')
    st.markdown(f"##### {bowling_team} "+ '- ' + str(round(loss*100))+'%')
    






