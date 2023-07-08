import streamlit as st

st.title("Basketball Plus-Minus Tracker")
# Player selection
homeplayers = ["Haley Fedick", "Zoe Idahosa", "Jayme Foreman", "Sarai Bailey", "Kaillie Hall",'Kait Nichols','Lauryn Meek','Jamilah Christian','Jess Keripe','Player10']
col1,col2,col3 = st.columns([1,1,1])
col1.subheader('TMU')
# Home team selection
home_team = [player for player in homeplayers if col1.checkbox(f"{player}")]

col2.text('')
col2.text('')

# Player selection
awayplayers = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5",'Player6','Player7','Player8','Player9','Player10']
col1_2,col2_2,col3_2 = st.columns([1,1,1])
col1_2.subheader('Away')
# Home team selection
away_team = [player for player in awayplayers if col1_2.checkbox(f"{player}",key=player)]

if col2.button('Add Point Home'):
    st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in home_team})  # Retrieve session state
    for player in home_team:
        st.session_state.home_points[player] += 1
    for player in away_team:
        st.session_state.away_points[player] -= 1

if col2.button('Add Point Away'):
    st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in away_team})  # Retrieve session state
    for player in away_team:
        st.session_state.away_points[player] += 1
    for player in home_team:
        st.session_state.home_points[player] -= 1

st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in homeplayers})
st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in awayplayers})

col3.subheader('+/-')
if 'home_points' in st.session_state:
    for player, count in st.session_state.home_points.items():
        col3.write(f"{player}: {count}")

col3_2.subheader('+/-')
if 'away_points' in st.session_state:
    for player, count in st.session_state.away_points.items():
        col3_2.write(f"{player}: {count}")

st.write(st.session_state.home_points)
st.write(st.session_state.away_points)


