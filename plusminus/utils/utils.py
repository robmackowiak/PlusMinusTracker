import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl
import streamlit as st


def get_roster(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    # Replace 'url' with the URL of the webpage containing the HTML table
    url = url+'#roster'

    # Read HTML table into a list of DataFrame objects
    tables = pd.read_html(url)

    # If there are multiple tables on the webpage, you can access each table using indexing
    # For example, to access the first table:
    df = tables[0]
    
    # Now you have the table data in a pandas DataFrame
    return df


def get_logo(url):

    team_name = url.split('/')[5]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with class="teamlogo"
        teamlogos = soup.find_all(class_="teamlogo")

        # Print or do something with the found elements
        for logo in teamlogos:
            img_src = logo['src']
        
        img_data = requests.get(img_src).content
        with open(f'./plusminus/assets/logo/{team_name}.jpg', 'wb') as handler:
            handler.write(img_data)
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)


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