import streamlit as st
import pandas as pd
from datetime import date
import numpy as np
import csv
import os.path
import os

st.markdown("<h1 style='text-align: center; color: black;'>Plus-Minus Tracker</h1>", unsafe_allow_html=True)
top_col1,top_col2,top_col3,top_col4 = st.columns([1,1,1,1])
# Player selection
homeplayers = ["#3: Hailey Franco-Deryck", "#6: Haley Fedick", "#8: Zoe Idahosa", "#10: Jayme Foreman", "#12: Corryn Parker",'#13: Alex Pino','#14: Kaillie Hall','#15: Kait Nichols','#17: Catrina Garvey','#21: Hannah Watson','#22: Lauryn Meek','#23: Tiya Misir','#24: Jamilah Christian','#25: Jessica Keripe']
col1,col2,col3 = st.columns([1,1,1])
col1.subheader('TMU')
# Home team selection
home_team = [player for player in homeplayers if col1.checkbox(f"{player}")]

# Player selection
awayplayers = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5",'Player6','Player7','Player8','Player9','Player10','Player11','Player12','Player13','Player14']
col2.subheader('Away')
# Home team selection
away_team = [player for player in awayplayers if col2.checkbox(f"{player}",key=player)]
##existing file
if os.path.isfile(str(date.today())+'TMU_plusminus.csv'):
    points_data_home = pd.read_csv(str(date.today())+'TMU_plusminus.csv')
    points_data_away = pd.read_csv(str(date.today())+'Away_plusminus.csv')
    st.session_state.home_points = st.session_state.get('home_points', {
        player: points_data_home.loc[points_data_home['Player'] == player, 'Points'].iloc[0]
        if player in points_data_home['Player'].values
        else 0  # Use a default value (e.g., 1) if the player is not found
        for player in homeplayers
    })
    st.session_state.away_points = st.session_state.get('away_points', {
        player: points_data_away.loc[points_data_away['Player'] == player, 'Points'].iloc[0]
        if player in points_data_away['Player'].values
        else 0  # Use a default value (e.g., 1) if the player is not found
        for player in awayplayers
    })
else:
    st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in homeplayers})
    st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in awayplayers})

if len(home_team)==5 and len(away_team)==5:
    if top_col2.button('Add Point TMU'):
        #st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in home_team})  # Retrieve session state
        for player in home_team:
            st.session_state.home_points[player] += 1
        for player in away_team:
            st.session_state.away_points[player] -= 1
        
        new_row_data = [date.today(),home_team[0],home_team[1],home_team[2],home_team[3],home_team[4],1]
        with open('lineup_plusminus.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_row_data)
        home_df = pd.DataFrame(list(st.session_state['home_points'].items()), columns=['Player', 'Points'])
        home_df.to_csv(str(date.today())+'TMU_plusminus.csv', index=False)
        away_df = pd.DataFrame(list(st.session_state['away_points'].items()), columns=['Player', 'Points'])
        away_df.to_csv(str(date.today())+'Away_plusminus.csv', index=False)

    if top_col3.button('Add Point Away'):
        #st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in away_team})  # Retrieve session state
        for player in away_team:
            st.session_state.away_points[player] += 1
        for player in home_team:
            st.session_state.home_points[player] -= 1
        
        new_row_data = [date.today(),home_team[0],home_team[1],home_team[2],home_team[3],home_team[4],-1]
        with open('lineup_plusminus.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(new_row_data)

        home_df = pd.DataFrame(list(st.session_state['home_points'].items()), columns=['Player', 'Points'])
        home_df.to_csv(str(date.today())+'TMU_plusminus.csv', index=False)
        away_df = pd.DataFrame(list(st.session_state['away_points'].items()), columns=['Player', 'Points'])
        away_df.to_csv(str(date.today())+'Away_plusminus.csv', index=False)
else:
    top_col2.button('Invalid Player #',key=0)
    top_col3.button('Invalid Player #',key=1)


with col3:
    table_switch = st.radio("Team",('TMU','Away'),horizontal=True)

if table_switch=='TMU':
    col3.subheader('TMU')
    if 'home_points' in st.session_state:
        height = int(35.2*(len(homeplayers)+1))
        col3.dataframe(st.session_state.home_points.items(),hide_index=True,column_config={'0':'Player','1':'+/-'},use_container_width=True,height=height)
else:
    col3.subheader('Away')
    if 'away_points' in st.session_state:
        height = int(35.2*(len(awayplayers)+1))
        col3.dataframe(st.session_state.away_points.items(),hide_index=True,column_config={'0':'Player','1':'+/-'},use_container_width=True,height=height)

st.text('')
if st.button('Show/Update Lineup +/-'):
    lineup_vals = pd.DataFrame(pd.read_csv('lineup_plusminus.csv',header=None,names=["Date", "P1", "P2", "P3","P4","P5","Points"]))
    lineup_vals = lineup_vals[lineup_vals['Date']==str(date.today())]
    lineup_vals = lineup_vals.groupby(['P1','P2','P3','P4','P5'])['Points'].sum()
    lineup_vals = lineup_vals.sort_values(ascending=False)
    st.dataframe(lineup_vals,width=1000)

st.text('')
st.text('')
st.text('')
st.text('')
st.text('')
visibility = False
if st.checkbox('Allow Reset'):
    visibility = True

if visibility == True:
    if st.button('Reset Values'):
        os.remove('lineup_plusminus.csv')
        os.remove(str(date.today())+'TMU_plusminus.csv')
        os.remove(str(date.today())+'Away_plusminus.csv')
