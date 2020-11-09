import streamlit as st
import pandas as pd
st.markdown('[![datandstories](https://github.com/michael-william/CBD/raw/master/resources/DS_logo_200.png)](https://dataandstories.com)', unsafe_allow_html=True)
st.header("""
**The Dash**
*A simple game based on on Balderdash and charades*
""")
@st.cache
def write():
	teams = pd.DataFrame(columns=['Name','Team'])
	usr_name = st.text_input("Your name", "Mancy Buckles")
	usr_team = st.selectbox('Team',['Gummies', 'Three Money'])
	if st.button('Update yourself!'):
		if usr_name in teams.Name:
			teams.loc[teams.name==usr_name,'Team'] = usr_team
		else:
			teams = teams.append({'Name': usr_name,'Team':usr_team}, ignore_index=True)

	st.write(teams)
write()
