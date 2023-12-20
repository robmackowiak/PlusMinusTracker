import streamlit as st
import pandas as pd
from datetime import date
import numpy as np
import csv
import os.path
import os

st.markdown("<h1 style='text-align: center; color: black;'>Plus-Minus Tracker</h1>", unsafe_allow_html=True)
top_col2,top_col3,top_col4,top_col5 = st.columns([1,1,1,1])

# Player selection
homeplayers = ["#3: Hailey Franco-Deryck", "#6: Haley Fedick", "#8: Zoe Idahosa", "#9: Sarai Bailey", "#10: Jayme Foreman", "#12: Hannah Watson",'#13: Alex Pino','#14: Kaillie Hall','#15: Kait Nichols','#17: Catrina Garvey','#21: Corrynn Parker','#22: Lauryn Meek','#23: Ailani Curvan','#24: Jamilah Christian','#25: Jessica Keripe']
col1,col2,col3 = st.columns([1,1,1])
col1.subheader('TMU')
# Home team selection
home_team = [player for player in homeplayers if col1.checkbox(f"{player}")]

# Player selection
awayplayers = ["#2: Arnold", "#3: Edwards", "#4: Samuels", "#5: Bueckers", "#10: Muhl", "#12: Shade", "#21: Bettencourt", "#24: Alfy", "#25: Brady", "#33: Ducharme", "#34: Patterson", "#35: Fudd", "#42: DeBerry", "#44: Griffin"]
col2.subheader('Away')
# Home team selection
away_team = [player for player in awayplayers if col2.checkbox(f"{player}",key=player)]
##existing file
if os.path.isfile(str(date.today())+'TMU_plusminus.csv') and os.path.isfile(str(date.today())+'TMU_possession_counts.csv'):
    points_data_home = pd.read_csv(str(date.today())+'TMU_plusminus.csv')
    points_data_away = pd.read_csv(str(date.today())+'Away_plusminus.csv')
    possession_data_home = pd.read_csv(str(date.today())+'TMU_possession_counts.csv')
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
    st.session_state.home_possessions = st.session_state.get('home_possessions', {
        player: possession_data_home.loc[possession_data_home['Player'] == player, 'Possessions'].iloc[0]
        if player in possession_data_home['Player'].values
        else 0  # Use a default value (e.g., 1) if the player is not found
        for player in homeplayers
    })
else:
    st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in homeplayers})
    st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in awayplayers})
    st.session_state.home_possessions = st.session_state.get('home_possessions', {player: 0 for player in homeplayers})

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
    
    if top_col4.button('Add Possession TMU'):
        #st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in away_team})  # Retrieve session state
        for player in home_team:
            st.session_state.home_possessions[player] += 1

        home_possession_df = pd.DataFrame(list(st.session_state['home_possessions'].items()), columns=['Player', 'Possessions'])
        home_possession_df.to_csv(str(date.today())+'TMU_possession_counts.csv', index=False)

    home_possession_df = pd.DataFrame(list(st.session_state['home_possessions'].items()), columns=['Player', 'Possessions'])
    top_col5.caption('Possessions: '+str(int(np.nansum(home_possession_df.values[:,1])/5)))

else:
    top_col2.button('Invalid Player #',key=0)
    top_col3.button('Invalid Player #',key=1)
    top_col4.button('Invalid Player #',key=2)
    home_possession_df = pd.DataFrame(list(st.session_state['home_possessions'].items()), columns=['Player', 'Possessions'])
    top_col5.caption('Possessions: '+str(int(np.nansum(home_possession_df.values[:,1])/5)))

with col3:
    table_switch = st.radio("Team",('TMU','Away'),horizontal=True)

if table_switch == 'TMU':
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

visibility_download = False
if st.checkbox('Allow Download'):
    visibility_download = True

if visibility_download:
    csv = points_data_home.to_csv(index=False)
    csv2 = points_data_away.to_csv(index=False)
    lineup_vals = pd.DataFrame(pd.read_csv('lineup_plusminus.csv',header=None,names=["Date", "P1", "P2", "P3","P4","P5","Points"]))
    lineup_vals = lineup_vals[lineup_vals['Date']==str(date.today())]
    lineup_vals = lineup_vals.groupby(['P1','P2','P3','P4','P5'])['Points'].sum()
    lineup_vals = lineup_vals.sort_values(ascending=False)
    csv3 = lineup_vals.to_csv(index=True)
    st.download_button(
        label="Download Home +/-",
        data=csv,
        key="download-csv.csv",
        on_click=None,
    )
    st.download_button(
        label="Download Away +/-",
        data=csv2,
        key="download-csv1.csv",
        on_click=None,
    )
    st.download_button(
        label="Download Lineup +/-",
        data=csv3,
        key="download-csv2.csv",
        on_click=None,
    )

visibility_reset = False
if st.checkbox('Allow Reset'):
    visibility_reset = True

if visibility_reset:
    if st.button('Reset Values'):
        try:
            os.remove('lineup_plusminus.csv')
        except:
            pass
        try:
            os.remove(str(date.today())+'TMU_plusminus.csv')
        except:
            pass
        try:
            os.remove(str(date.today())+'Away_plusminus.csv')
        except:
            pass
        try:
            os.remove(str(date.today())+'TMU_possessions.csv')
        except:
            pass
