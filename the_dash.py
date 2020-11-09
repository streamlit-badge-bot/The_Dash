import pandas as pd
import numpy as np
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


# Plotting
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
pio.renderers.default = 'iframe'


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", ['Setup', 'Game'])


def main():
	team_df = pd.DataFrame(columns=['Name','Team'])
	def setup_features():
		usr_name = st.text_input("Your name", "Mancy Buckles")
		usr_team = st.selectbox('Team',['Gummies', 'Three Money'])
		return usr_name, usr_team

	
	def team_setup():
		temp_df = team_df
		if usr_name in team_df.Name:
			temp_df.loc[temp_df.Name==usr_name,'Team'] = usr_team
		else:
			temp_df = temp_df.append({'Name': usr_name,'Team':usr_team}, ignore_index=True)
		return temp_df


	if selection == 'Setup':
		usr_name, usr_team = setup_features()
		if st.button('Update yourself!'):
			temp_df = team_setup()
			team_df = pd.concat(team_df,temp_df)

		st.write(team_df)

if __name__ == "__main__":
    main()
