import pandas as pd
import numpy as np
import streamlit as st
import random
import SessionState

st.markdown('[![datandstories](https://github.com/michael-william/CBD/raw/master/resources/DS_logo_200.png)](https://dataandstories.com)', unsafe_allow_html=True)
st.header("""
**The Dash**
*A fun game combining Balderdash, Charades, and Dictionary*
""")

@st.cache(allow_output_mutation=True)
def data():
	team_df = pd.read_csv('https://github.com/michael-william/The_Dash/blob/master/resources/teams.csv?raw=true')
	dashes = pd.read_csv('https://github.com/michael-william/The_Dash/blob/master/resources/The_Dash_Responses.csv?raw=true')
	dashes.drop('Timestamp',axis=1,inplace=True)
	dashes = dashes.stack().reset_index()
	dashes.columns = ['index','question','dashes']
	dashes_list = dashes.dashes.to_list()
	dash_num = len(dashes)
	return team_df, dashes_list, dash_num, dashes

team_df, dashes_list, dash_num, dashes = data()

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
x=-1
ss = SessionState.get(x=x)

@st.cache()
def shuffle(x,num):
    r1 = random.sample(x, num)
    r2 = random.sample(x, num)
    r3 = random.sample(x, num)
    return r1, r2, r3

r1, r2, r3 = shuffle(dashes_list,dash_num)



def main():

	round_type = st.selectbox('Choose the round',('Test','Description','Charades','1 Word','Review'))
	current_round = round_type
	if current_round =='Test':
		r=['This is a sample dash', 'cruise missile lana', 'gypsy Molly', 'Mike is the greatest!']
		st.header("This is a test round")
		st.write("1) If you are the first person in the round, click the plus sign for the next word")
		st.write("2) If you are not the first person, enter the clue count to start")
		st.write("3) After 60 seconds, your turn is over")
		st.write("4) Relay the clue count to the group and place your phone face down on the table")
		ss.x = st.number_input('Clue Count',min_value=-1, max_value=dash_num+1, value=-1,step=1)
		if ss.x==-1:
			st.markdown('**Start the round!**')
		elif ss.x ==dash_num+1:
			#st.markdown('**End of Round**!')
			"""### Round Over!"""
			st.markdown("![Alt Text](https://media.giphy.com/media/R3eONMIcGP8nr8ajSs/giphy.gif)")
			st.balloons()
		else:
			st.markdown('**{}**'.format(r[ss.x]))
	elif current_round =='Description':
		r=r1
		ss.x=-1
		st.header("Welcome to the 1st Round of The Dash")
		st.write("1) If you are the first person in the round, click the plus sign for the next word")
		st.write("2) If you are not the first person, enter the clue count to start")
		st.write("3) After 60 seconds, your turn is over")
		st.write("4) Relay the clue count to the group and place your phone face down on the table")
		ss.x= st.number_input('Clue Count',min_value=-1, max_value=dash_num, value=-1,step=1)
		if ss.x==-1:
			st.markdown('**Start the round!**')
		elif ss.x ==dash_num:
			"""### Round Over!"""
			st.markdown("![Alt Text](https://media.giphy.com/media/R3eONMIcGP8nr8ajSs/giphy.gif)")
			st.balloons()
		else:
			st.write(r[ss.x])
	elif current_round =='Charades':
		r=r2
		st.header("Welcome to the 2nd Round of The Dash")
		st.write("Use normal charades to help your team guess the answer")
		st.write("1) If you are the first person in the round, click the plus sign for the next word")
		st.write("2) If you are not the first person, enter the clue count to start")
		st.write("3) After 60 seconds, your turn is over")
		st.write("4) Relay the clue count to the group and place your phone face down on the table")
		ss.x= st.number_input('Clue Count',min_value=-1, max_value=dash_num, value=-1,step=1)
		if ss.x==-1:
			st.markdown('**Start the round!**')
		elif ss.x ==dash_num:
			"""### Round Over!"""
			st.markdown("![Alt Text](https://media.giphy.com/media/PhH6eIv19BsnDTrX0F/giphy.gif)")
			st.balloons()
		else:
			st.write(r[ss.x])
	elif current_round =='1 Word':
		r=r3
		st.header("Welcome to the Last Round of The Dash!")
		st.write("Use only one word,including proper nouns, to help your team guess the clue")
		st.write("1) If you are the first person in the round, click the plus sign for the next word")
		st.write("2) If you are not the first person, enter the clue count to start")
		st.write("3) After 60 seconds, your turn is over")
		st.write("4) Relay the clue count to the group and place your phone face down on the table")
		ss.x= st.number_input('Clue Count',min_value=-1, max_value=dash_num, value=-1,step=1)
		if ss.x==-1:
			st.markdown('**Start the round!**')
		elif ss.x ==dash_num:
			"""### Round Over!"""
			st.markdown("![Alt Text](https://media.giphy.com/media/oOEtax0fEqdoiNNfnP/giphy.gif)")
			st.balloons()
		else:
			st.write(r[ss.x])
	else:
		st.dataframe(dashes['dashes'])


if __name__ == "__main__":
    main()
