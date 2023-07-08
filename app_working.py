import streamlit as st

def calculate_plus_minus(players, scores):
    plus_minus = {player: 0 for player in players}
    for player in players:
        for score in scores:
            if player in score['home']:
                plus_minus[player] += 1
            if player in score['away']:
                plus_minus[player] -= 1
    return plus_minus

st.title("Basketball Plus-Minus Tracker")
col1, col2 = st.columns([1, 1])
# Player selection
homeplayers = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]
awayplayers = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

# Home team selection
col1.subheader("Home Team")
home_team = [player for player in homeplayers if col1.checkbox(f"Home {player}")]

# Away team selection
col2.subheader("Away Team")
away_team = [player for player in awayplayers if col2.checkbox(f"Away {player}")]

if col1.button('Add Point Home'):
    st.session_state.home_points = st.session_state.get('home_points', {player: 0 for player in home_team})
    for player in home_team:
        st.session_state.home_points[player] += 1

if col2.button('Add Point Away'):
    st.session_state.away_points = st.session_state.get('away_points', {player: 0 for player in away_team})
    for player in away_team:
        st.session_state.away_points[player] += 1

if 'home_points' in st.session_state:
    st.subheader("Home Team Points")
    for player, count in st.session_state.home_points.items():
        st.write(f"{player}: {count}")

if 'away_points' in st.session_state:
    st.subheader("Away Team Points")
    for player, count in st.session_state.away_points.items():
        st.write(f"{player}: {count}")
