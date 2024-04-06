import streamlit as st
import pandas as pd
import numpy as np
import os.path
import os
from plusminus.utils.utils import get_roster, get_logo, custom_footer
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(
    page_title="PlusMinus",
    page_icon="📊",
    initial_sidebar_state="expanded",
    menu_items=None,
)

custom_footer()

@st.cache_data(ttl=3600)
def get_rosters(team_1_url, team_2_url):
    team1_df = get_roster(team_1_url)
    team2_df = get_roster(team_2_url)
    get_logo(team_1_url)
    get_logo(team_2_url)
    return team1_df, team2_df


if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame({"team": [], "name": [], "val": []})

if "data_lineup" not in st.session_state:
    st.session_state["data_lineup"] = pd.DataFrame(
        {
            "team": [],
            "player1": [],
            "player2": [],
            "player3": [],
            "player4": [],
            "player5": [],
            "val": [],
        }
    )

with st.sidebar:
    with st.expander("Sport Reference Team Links"):
        team1_col, team2_col = st.columns(2)
        st.session_state["team1_url"] = team1_col.text_input(
            "Team 1"
        )

        st.session_state["team2_url"] = team2_col.text_input(
            "Team 2"
        )
        
        if len(st.session_state["team1_url"]) > 0 and len(st.session_state["team2_url"]) > 0:
            st.session_state["team1_df"], st.session_state["team2_df"] = get_rosters(st.session_state["team1_url"], st.session_state["team2_url"])
            st.caption("Data Uploaded Succesfully ✅")

            team1 = st.session_state["team1_url"].split("/")[5].title()
            team2 = st.session_state["team2_url"].split("/")[5].title()

            team1_df = st.session_state["team1_df"]
            team2_df = st.session_state["team2_df"]

    team1_players_col, team2_players_col = st.columns(2)

    if len(st.session_state["team1_url"]) > 0 and len(st.session_state["team2_url"]) > 0:
        with team1_players_col:
            st.caption(team1.replace('-', ' '))
            team1_active = [
                team1_df["Player"][i]
                for i in range(len(team1_df["Player"]))
                if st.checkbox(f'#{team1_df["#"][i]} {team1_df["Player"][i]}')
            ]

        with team2_players_col:
            st.caption(team2.replace('-', ' '))
            team2_active = [
                team2_df["Player"][i]
                for i in range(len(team2_df["Player"]))
                if st.checkbox(f'#{team2_df["#"][i]} {team2_df["Player"][i]}', key=f'{team2_df["Player"][i]}')
            ]

        st.download_button('Download Player Data', data=st.session_state["data"].to_csv(index=False), file_name=f"{team1.replace('-','')}_{team2.replace('-','')}_plusminus_player_data.csv", use_container_width=True)
        st.download_button('Download Lineup Data', data=st.session_state["data_lineup"].to_csv(index=False), file_name=f"{team1.replace('-','')}_{team2.replace('-','')}_plusminus_lineup_data.csv", use_container_width=True)

        if st.button('Reset App', use_container_width=True, type='primary'):
            streamlit_js_eval(js_expressions="parent.window.location.reload()")

if "team1_df" not in st.session_state or "team2_df" not in st.session_state:
    st.caption(
        "Please use sidebar to initialize two team rosters to start plus-minus tracking."
    )
else:
    _, logo1_col, _, _, logo2_col, _ = st.columns([1, 1, 0.5, 0.5, 1, 1])
    try:
        logo1_col.image(f"./plusminus/assets/logo/{team1}.jpg", use_column_width=True)
    except:
        logo1_col.header(team1.replace('-', ''))
    
    try:
        logo2_col.image(f"./plusminus/assets/logo/{team2}.jpg", use_column_width=True)
    except:
        logo2_col.header(team2.replace('-', ''))

    (
        _,
        button_team1,
        _,
        _,
        button_team2,
        _,
    ) = st.columns([1, 1, 0.5, 0.5, 1, 1])

    if button_team1.button(f"+1", use_container_width=True):
        if len(team1_active) == 5:
            for player in team1_active:
                st.session_state["data"].loc[len(st.session_state["data"].index)] = [
                    team1,
                    player,
                    1,
                ]
            for player in team2_active:
                st.session_state["data"].loc[len(st.session_state["data"].index)] = [
                    team2,
                    player,
                    -1,
                ]

            st.session_state["data_lineup"].loc[
                len(st.session_state["data_lineup"].index)
            ] = [
                team1,
                team1_active[0],
                team1_active[1],
                team1_active[2],
                team1_active[3],
                team1_active[4],
                1,
            ]
            st.session_state["data_lineup"].loc[
                len(st.session_state["data_lineup"].index)
            ] = [
                team2,
                team2_active[0],
                team2_active[1],
                team2_active[2],
                team2_active[3],
                team2_active[4],
                -1,
            ]

    if button_team2.button(f"+1", use_container_width=True, key=1):
        if len(team1_active) == 5:
            for player in team2_active:
                st.session_state["data"].loc[len(st.session_state["data"].index)] = [
                    team2,
                    player,
                    1,
                ]
            for player in team1_active:
                st.session_state["data"].loc[len(st.session_state["data"].index)] = [
                    team1,
                    player,
                    -1,
                ]

            st.session_state["data_lineup"].loc[
                len(st.session_state["data_lineup"].index)
            ] = [
                team1,
                team1_active[0],
                team1_active[1],
                team1_active[2],
                team1_active[3],
                team1_active[4],
                -1,
            ]
            st.session_state["data_lineup"].loc[
                len(st.session_state["data_lineup"].index)
            ] = [
                team2,
                team2_active[0],
                team2_active[1],
                team2_active[2],
                team2_active[3],
                team2_active[4],
                1,
            ]

    player, lineup = st.tabs(["Player", "Lineup"])

    with player:
        _, player_col1_title, _, _, player_col2_title, _ = st.columns(
            [1.5, 1, 0.65, 0.5, 1, 1]
        )
        player_col1_title.caption(team1.replace('-', ' '))
        player_col2_title.caption(team2.replace('-', ' '))

        _, player_col1, player_col1_val, player_col2, player_col2_val, _ = st.columns(
            [1.2, 1.8, 1.5, 1.8, 1.5, 0.2]
        )

        ordered_names = (
            st.session_state["data"]
            .query("team==@team1")
            .groupby(by="name")["val"]
            .sum()
            .sort_values(ascending=False)
            .keys()
            .values
        )
        for name in ordered_names:
            number = team1_df[team1_df["Player"] == name]["#"].values[0]
            val = st.session_state["data"].query("name==@name")["val"].sum()
            val = "+" + str(val) if val >= 0 else val
            player_col1.write(f"#{number} {name}")
            player_col1_val.write(f"{val}")

        ordered_names = (
            st.session_state["data"]
            .query("team==@team2")
            .groupby(by="name")["val"]
            .sum()
            .sort_values(ascending=False)
            .keys()
            .values
        )
        for name in ordered_names:
            number = team2_df[team2_df["Player"] == name]["#"].values[0]
            val = st.session_state["data"].query("name==@name")["val"].sum()
            val = "+" + str(val) if val >= 0 else val
            player_col2.write(f"#{number} {name}")
            player_col2_val.write(f"{val}")

    with lineup:
        team1_lineup, team2_lineup = st.tabs([f"{team1.replace('-','')}", f"{team2.replace('-', ' ')}"])

        with team1_lineup:
            st.dataframe(
                st.session_state["data_lineup"]
                .query(f'team=="{team1}"')
                .groupby(by=["player1", "player2", "player3", "player4", "player5"])[
                    "val"
                ]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
                .rename(
                    columns={
                        "player1": "Player 1",
                        "player2": "Player 2",
                        "player3": "Player 3",
                        "player4": "Player 4",
                        "player5": "Player 5",
                        "val": "Plus-Minus",
                    }
                )
                .sort_values(by="Plus-Minus", ascending=False),
                use_container_width=True,
            )

        with team2_lineup:
            st.dataframe(
                st.session_state["data_lineup"]
                .query(f'team=="{team2}"')
                .groupby(by=["player1", "player2", "player3", "player4", "player5"])[
                    "val"
                ]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
                .rename(
                    columns={
                        "player1": "Player 1",
                        "player2": "Player 2",
                        "player3": "Player 3",
                        "player4": "Player 4",
                        "player5": "Player 5",
                        "val": "Plus-Minus",
                    }
                )
                .sort_values(by="Plus-Minus", ascending=False),
                use_container_width=True,
            )
