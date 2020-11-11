import pandas as pd
import numpy as np
import time
from datetime import datetime
import datetime
from datetime import timedelta
import streamlit as st
from resources.gamestate import persistent_game_state
from typing import List, Tuple
from string import ascii_lowercase
import types
import random
import dataclasses
import SessionState

# Plotting
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
pio.renderers.default = 'iframe'

@st.cache(allow_output_mutation=True)
def data():
	team_df = pd.read_excel('https://github.com/michael-william/The_Dash/blob/master/resources/teams.xlsx?raw=true')
	dashes = pd.read_excel('https://github.com/michael-william/The_Dash/blob/master/resources/dashes.xlsx?raw=true')
	dashes_list = dashes.Dash.to_list()
	return team_df, dashes_list

team_df, dashes_list = data()

teams = team_df[['Team','Name']].sort_values('Team').reset_index(drop=True)
gummies = team_df[team_df.Team=='Gummies']['Name'].reset_index(drop=True)
threemoney = team_df[team_df.Team=='Three Money']['Name'].reset_index(drop=True)

def turn_order():
	turn_order = []
	unique_names = 4
	for i in range(unique_names):
		turn_order.append(gummies.iloc[i])
		turn_order.append(threemoney.iloc[i])
	return turn_order

turn_order = turn_order()
x=0
ss = SessionState.get(x=x)

def shuffle(x):
    new = x
    random.shuffle(new)
    return new

r1 = shuffle(dashes_list)
r2 = shuffle(dashes_list)
r3 = shuffle(dashes_list)

def main():

	if st.button('Next Word!'):
		ss.x = ss.x + 1
		if ss.x>20:
			ss.x = 0
		st.write(r1[ss.x])
	if st.button('Last Word'):
		if ss.x>0:
			ss.x = ss.x-1
		else:
			ss.x = 0
		st.write(r1[ss.x])


if __name__ == "__main__":
    main()
