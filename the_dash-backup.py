import pandas as pd
import numpy as np
from datetime import datetime
import datetime
from datetime import timedelta
import streamlit as st
import pages.set_up
import pages.game


# ML libraries
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio
import plotly.offline as pyo
pio.renderers.default = 'iframe'


PAGES = {
    "Setup": pages.set_up,
    "Game": pages.game
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))


if __name__ == "__main__":
    main()