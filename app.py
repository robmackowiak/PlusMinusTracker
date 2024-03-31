import streamlit as st
import pandas as pd
import numpy as np
import os.path
import os

st.set_page_config(
    page_title="PlusMinus",
    page_icon="📊",
    initial_sidebar_state="expanded",
    menu_items=None,
)

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
    with st.expander("Upload Data"):
        team1_col, team2_col = st.columns(2)
        st.session_state["team1_df"] = team1_col.file_uploader(
            "Upload Team 1 File Here", type=["csv"]
        )
        st.session_state["team2_df"] = team2_col.file_uploader(
            "Upload Team 2 File Here", type=["csv"], key=1
        )

    if (
        st.session_state["team1_df"] is not None
        and st.session_state["team2_df"] is not None
    ):
        team1 = st.session_state["team1_df"].name.split("_")[1].split(".")[0].upper()
        team2 = st.session_state["team2_df"].name.split("_")[1].split(".")[0].upper()

        team1_players_col, team2_players_col = st.columns(2)
        team1_df = pd.read_csv(st.session_state["team1_df"])
        team2_df = pd.read_csv(st.session_state["team2_df"])

        with team1_players_col:
            st.caption(team1)
            team1_active = [
                team1_df["Name"][i]
                for i in range(len(team1_df["Name"]))
                if st.checkbox(f'#{team1_df["Number"][i]} {team1_df["Name"][i]}')
            ]

        with team2_players_col:
            st.caption(team2)
            team2_active = [
                team2_df["Name"][i]
                for i in range(len(team2_df["Name"]))
                if st.checkbox(f'#{team2_df["Number"][i]} {team2_df["Name"][i]}')
            ]

if st.session_state["team1_df"] is None or st.session_state["team2_df"] is None:
    st.caption(
        "Please use sidebar to upload two team roster files to start plus-minus tracking."
    )
else:
    _, logo1_col, _, _, logo2_col, _ = st.columns([1, 1, 0.5, 0.5, 1, 1])
    logo1_col.image(f"./plusminus/assets/logo/{team1}.png", use_column_width=True)
    logo2_col.image(f"./plusminus/assets/logo/{team2}.png", use_column_width=True)

    (
        _,
        button_team1,
        _,
        _,
        button_team2,
        _,
    ) = st.columns([1, 1, 0.5, 0.5, 1, 1])

    if button_team1.button(f"{team1} +1", use_container_width=True):
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

    if button_team2.button(f"{team2} +1", use_container_width=True):
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
        _, player_col1_title, _, _, player_col2_title, _ = st.columns([1.5,1,0.65,0.5,1,1])
        player_col1_title.caption(team1)
        player_col2_title.caption(team2)

        _, player_col1, player_col1_val, player_col2, player_col2_val, _ = st.columns([1.2, 1.8, 1.5, 1.8, 1.5, 0.2])

        ordered_names = st.session_state['data'].query('team==@team1').groupby(by='name')['val'].sum().sort_values(ascending=False).keys().values
        for name in ordered_names:
            number = team1_df[team1_df['Name']==name]["Number"].values[0]
            val = st.session_state['data'].query('name==@name')['val'].sum()
            val = "+" + str(val) if val >= 0 else val
            player_col1.write(f"#{number} {name}")
            player_col1_val.write(
                f"{val}"
            )
        
        ordered_names = st.session_state['data'].query('team==@team2').groupby(by='name')['val'].sum().sort_values(ascending=False).keys().values
        for name in ordered_names:
            number = team2_df[team2_df['Name']==name]["Number"].values[0]
            val = st.session_state['data'].query('name==@name')['val'].sum()
            val = "+" + str(val) if val >= 0 else val
            player_col2.write(f"#{number} {name}")
            player_col2_val.write(
                f"{val}"
            )

    with lineup:
        team1_lineup, team2_lineup = st.tabs([f"{team1}", f"{team2}"])

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
                .rename(columns={"player1": "Player 1", "player2": "Player 2", "player3": "Player 3", "player4": "Player 4", "player5": "Player 5", "val": "Plus-Minus"})
                .sort_values(by="Plus-Minus", ascending=False)
            , use_container_width=True
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
                .rename(columns={"player1": "Player 1", "player2": "Player 2", "player3": "Player 3", "player4": "Player 4", "player5": "Player 5", "val": "Plus-Minus"})
                .sort_values(by="Plus-Minus", ascending=False)
            , use_container_width=True
            )
