import pandas as pd
import numpy as np
from datetime import datetime
import datetime
from datetime import timedelta
import streamlit as st

# ML libraries
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
pio.renderers.default = 'iframe'

st.markdown('[![datandstories](https://github.com/michael-william/CBD/raw/master/resources/DS_logo_200.png)](https://dataandstories.com)', unsafe_allow_html=True)
st.header("""
**Custom Timeline for COVID**
*From contration through the contagious period*
""")

st.sidebar.header('Resources')
st.sidebar.subheader('[Incubation period](https://www.who.int/news-room/commentaries/detail/transmission-of-sars-cov-2-implications-for-infection-prevention-precautions#:~:text=The%20incubation%20period%20of%20COVID,to%20a%20confirmed%20case.)')
st.sidebar.markdown("""
	The incubation period of COVID-19, which is the time between exposure to the virus and symptom onset, is on **average 5-6 days**, but can be as long as 14 days.
	""")
st.sidebar.header('[Symptom period](https://www.cdc.gov/coronavirus/2019-ncov/hcp/duration-isolation.html)')
st.sidebar.markdown("""
	In this series of patients, it was estimated that 88% and 95% of their specimens no longer yielded replication-competent virus after 10 and 15 days, respectively, following symptom onset.
	""")
st.sidebar.subheader('[Contagious period](https://edition.cnn.com/interactive/2020/health/coronavirus-questions-answers/)')
st.sidebar.markdown("""
	**For symptomatic carriers**: If it’s been at least 10 days since your symptoms started and at least 24 hours since you’ve had a fever (without the help of fever-reducing medication) and your other symptoms have improved, you can go ahead and stop isolating, the CDC says.
	Patients with severe illness may have to keep isolating for up to 20 days after symptoms started.
	**For asymptomatic carriers**: People who tested positive but don’t have any symptoms can stop isolating 10 days after the first positive test – as long as they have not subsequently developed symptoms, the CDC says.
	""")


def user_input_features():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    sympt_start = st.date_input('Symptom start date', today)
    sympt_end = st.date_input('Symptom/fever end date (avg. is 10-15 days from the first day of symptoms)', sympt_start+datetime.timedelta(days=10))
    if sympt_start > sympt_end:
        st.error('Error: End date must fall after or on start date. Average length of sytoms is 10 days')
    #st.sidebar.text('City: '+(location.raw['display_name'].split(',')[3]))
    #st.sidebar.text('Longitude: '+str(longitude))
    #st.sidebar.text('Latitude: '+str(latitude))
    #latitude = st.sidebar.slider('Latitude', 50.770041, 53.333967, 51.2)
    #longitude = st.sidebar.slider('Longitude', 3.554188, 7.036756, 5.2)
    #p_type = st.sidebar.selectbox('Apartment',['Room', 'Studio', 'Apartment', 'Anti-squat', 'Student residence'])
    return today, sympt_start, sympt_end

def main():
    st.subheader('Select a date range for your symptonms')
    st.markdown('The graphs below will adjust based on your symptom start and end dates following the guidelines in the Resrources section. These calculations are based on averages and is only meant to help you theorize your specific situation.')
    today, s_start, s_end = user_input_features()
    contag_start = s_start - datetime.timedelta(days=3)
    contag_end = s_start + datetime.timedelta(days=11)
    incubation_start = s_start - datetime.timedelta(days=5)
    incubation_end = s_start
    inc_start = s_start - datetime.timedelta(days=5)
    inc_end = s_start
    
    def sympt():
	    sympt_start = s_start
	    sympt_end = s_end
	    sympt_range = []
	    sympt_delta = sympt_end-sympt_start
	    for i in range(sympt_delta.days+1):
	        day = sympt_start + timedelta(days=i)
	        sympt_range.append(day.isoformat())
	    return sympt_range, sympt_delta

    sympt_range, sympt_delta = sympt()

    def contag():
    	contag_start = s_start - datetime.timedelta(days=3)
    	if len(sympt_range) < 10:
    		contag_end = s_start + datetime.timedelta(days=10)
    	else:
    		contag_end = s_end+timedelta(days=1)
    	contag_range = []
    	contag_delta = contag_end-contag_start
    	for i in range(contag_delta.days+1):
    		day = contag_start + timedelta(days=i)
    		contag_range.append(day.isoformat())
    	return contag_range, contag_delta, contag_end	

    contag_range, contag_delta, contag_end = contag()	

    def inc():
	    inc_start = s_start - datetime.timedelta(days=5)
	    inc_end = s_start
	    inc_range = []
	    inc_delta = inc_end - inc_start
	    for i in range(inc_delta.days+1):
	        day = inc_start + timedelta(days=i)
	        inc_range.append(day.isoformat())
	    return inc_range, inc_delta

    inc_range, inc_delta = inc()
    

    def vis():
	    fig = go.Figure()
	    fig.add_trace(go.Scatter(x=contag_range, y=[1 for i in range(len(contag_range))],
	                        mode='lines',
	                        line=dict(width=3),
	                        text = 'Contagious period',
	                        hovertemplate=
	                            "<b>Potential Contagious period</b><br><br>" +
	                            "Start date: {}<br>".format(contag_start) +
	                            "End date: {}<br>".format(contag_end) +
	                            "Number of days: {}".format(len(contag_range)-1) +
	                            "<extra></extra>",
	                        name='Contagious period'))

	    fig.add_trace(go.Scatter(x=sympt_range, y=[0 for i in range(len(sympt_range))],
	                        mode='lines',
	                        line=dict(width=3),
	                        hoverlabel=dict(font=dict(color='white')),
	                        hovertemplate=
	                            "<b>Symptom</b><br><br>" +
	                            "Start date: {}<br>".format(s_start) +
	                            "End date: {}<br>".format(s_end) +
	                            "Number of days: {}".format(len(sympt_range)-1) +
	                            "<extra></extra>",
	                        name='Symptom period'))

	    fig.add_trace(go.Scatter(x=inc_range, y=[.50 for i in range(len(inc_range))],
	                        mode='lines',
	                        line=dict(width=3),
	                        hoverlabel=dict(font=dict(color='white')),
	                        hovertemplate=
	                            "<b>Incubation</b><br><br>" +
	                            "Start date: {}<br>".format(inc_start) +
	                            "End date: {}<br>".format(inc_end) +
	                            "Number of days: {}".format(len(inc_range)-1) +
	                            "<extra></extra>",
	                        name='Incubation period'))

	    fig.add_trace(go.Scatter(x=[inc_start.isoformat()], y=[.50], hoverinfo='skip',
	    						marker=dict(size=10, color='seagreen')
	                            #text='Possible<br> contraction<br> date',
	                            #textposition=["bottom center"],
	                            #mode="markers+text")
	                            ,showlegend=False))
	    fig.add_trace(go.Scatter(x=[inc_end.isoformat()], y=[.50], hoverinfo='skip',
	    						marker=dict(size=10, color='seagreen')
	                            #text='Possible<br> contraction<br> date',
	                            #textposition=["bottom center"],
	                            #mode="markers+text")
	                            ,showlegend=False))
	    fig.add_trace(go.Scatter(x=[s_start.isoformat()], y=[0], hoverinfo='skip',
	    								marker=dict(size=10, color='salmon')
			                            #text='Possible<br> contraction<br> date',
			                            #textposition=["bottom center"],
			                            #mode="markers+text")
			                            ,showlegend=False))
	    fig.add_trace(go.Scatter(x=[s_end.isoformat()], y=[0], hoverinfo='skip',
	    								marker=dict(size=10, color='salmon')
			                            #text='Possible<br> contraction<br> date',
			                            #textposition=["bottom center"],
			                            #mode="markers+text")
			                            ,showlegend=False))
	    fig.add_trace(go.Scatter(x=[contag_start.isoformat()], y=[1], hoverinfo='skip',
	    								marker=dict(size=10, color='skyblue')
			                            #text='Possible<br> contraction<br> date',
			                            #textposition=["bottom center"],
			                            #mode="markers+text")
			                            ,showlegend=False))
	    fig.add_trace(go.Scatter(x=[contag_end.isoformat()], y=[1], hoverinfo='skip',
	    								marker=dict(size=10, color='skyblue')
			                            #text='Possible<br> contraction<br> date',
			                            #textposition=["bottom center"],
			                            #mode="markers+text")
			                            ,showlegend=False))

	    fig.add_annotation(
	        x=inc_start.isoformat(),
	        y=.55,
	        xref="x",
	        yref="paper",
	        text="Possible<br> contraction<br> date<br>{}".format(inc_start),
	        showarrow=True,
	        font=dict(
	            family="Courier New, monospace",
	            size=12,
	            color="#ffffff"
	            ),
	        align="center",
	        arrowhead=2,
	        arrowsize=2,
	        arrowwidth=2,
	        arrowcolor="#636363",
	        ax=0,
	        ay=80,
	        bordercolor="#c7c7c7",
	        borderwidth=0,
	        borderpad=4,
	        bgcolor="seagreen",
	        opacity=0.8
	        )

	    fig.add_annotation(
	        x=contag_start + timedelta(days=np.ceil(len(contag_range)/2)),
	        y=.70,
	        xref="x",
	        yref="paper",
	        text="Contagious<br>period ({} days)<br>{} to {}".format(len(contag_range)-1,contag_start, contag_end),
	        showarrow=True,
	        font=dict(
	            family="Courier New, monospace",
	            size=12,
	            color="#ffffff"
	            ),
	        align="center",
	        arrowhead=2,
	        arrowsize=2,
	        arrowwidth=2,
	        arrowcolor="#636363",
	        ax=0,
	        ay=-70,
	        bordercolor="#c7c7c7",
	        borderwidth=0,
	        borderpad=4,
	        bgcolor="RoyalBlue",
	        opacity=1
	        )

	    fig.add_annotation(
	        x=s_start + timedelta(days=np.ceil(len(sympt_range)/2)),
	        y=.49,
	        xref="x",
	        yref="paper",
	        text="Symptoms<br>period ({} days)<br>{} to {}".format(len(sympt_range)-1,s_start, s_end),
	        showarrow=True,
	        font=dict(
	            family="Courier New, monospace",
	            size=12,
	            color="#ffffff"
	            ),
	        align="center",
	        arrowhead=2,
	        arrowsize=2,
	        arrowwidth=2,
	        arrowcolor="#636363",
	        ax=0,
	        ay=70,
	        bordercolor="#c7c7c7",
	        borderwidth=0,
	        borderpad=4,
	        bgcolor="darksalmon",
	        opacity=1
	        )

	    fig.update_layout(xaxis = {'title':'Dates', 'type':'date'},
	                      yaxis = {'showgrid': True, # thin lines in the background
	                               'zeroline': True, # thick line at x=0
	                               'visible': False,  # numbers below
	                               'range':[-3, 3]
	                              },
	                      title='Potential Stages and Dates',
	                      height=450,
	                      width=800,
	                      showlegend=True,              
	                      plot_bgcolor="white"
	                      #margin=dict(t=50,l=20,b=10,r=20)
	                                 )

	    return fig

    
    fig = vis()
    fig.show()
    st.plotly_chart(fig, use_container_width=True, config=dict(displayModeBar=False))

if __name__ == "__main__":
    main()