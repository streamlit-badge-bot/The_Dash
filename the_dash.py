import pandas as pd
import numpy as np
from datetime import datetime
import datetime
from datetime import timedelta
import streamlit as st
import sqlite3 as sl


# ML libraries
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
pio.renderers.default = 'iframe'


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", ['Setup', 'Game'])
con = sl.connect('the_dash.db')
with con:
    con.execute("""
        CREATE TABLE TEAMS (
            Name TEXT,
            Team TEXT
        );
    """)

def setup():
	df = pd.read_sql('''SELECT Name, Team 
					    FROM TEAMS
					''', con)
	if usr_name in df.Name:
			df.loc[df.Name==usr_name,'Team'] = usr_team
	else:
		df = df.append({'Name': usr_name,'Team':usr_team}, ignore_index=True)
	return df

if selection == 'Setup':
	usr_name = st.text_input("Your name", "Mancy Buckles")
	usr_team = st.selectbox('Team',['Gummies', 'Three Money'])
	if st.button('Update yourself!'):
		team_df = setup()

	st.write(team_df)
