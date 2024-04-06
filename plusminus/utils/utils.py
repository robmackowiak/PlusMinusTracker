import streamlit as st


def custom_footer():
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            footer:after {
                content:'PlusMinus Tracker - Made by Rob Mackowiak - 2024'; 
                visibility: visible;
                display: block;
                position: relative;
                text-align: center;
                padding: 5px;
                top: 2px;
                align: center;
                }
            </style>
            """
    return st.markdown(hide_streamlit_style, unsafe_allow_html=True)
