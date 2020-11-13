import pandas as pd
import streamlit as st

st.beta_set_page_config(layout="wide")

col1, col2 ,col3 = st.beta_columns((2, 2, 1))




original = 'Channel 1'

if col1.button(original):
	st.write("[GitHub](http://github.com)")



grayscale = "Channel 2"

if col2.button(grayscale):
	st.write("[GitHub](http://github.com)")


name="Channel 3"

if col3.button(name):
	st.write("[GitHub](http://github.com)")





col4, col5 ,col6 = st.beta_columns((2, 2, 1))


col4.write("[Channel 4](http://github.com)")
col5.write("[Channel 5](http://github.com)")
col6.write("[Channel 6](http://github.com)")








col7, col8 ,col9 = st.beta_columns((2, 2, 1))

def coll7():
    href = '''<button onclick="location.href = 'https://www.linkedin.com/in/daneshwar-gobbani-baa69516a/';" id="myButton" class="float-left submit-button" >Channel 7</button>'''
    return href
col7.markdown(coll7(), unsafe_allow_html=True)


def coll8():
    href = '''<button onclick="location.href = 'https://www.linkedin.com/in/daneshwar-gobbani-baa69516a/';" id="myButton" class="float-left submit-button" >Channel 8</button>'''
    return href
col8.markdown(coll8(), unsafe_allow_html=True)


def coll9():
    href = '''<button onclick="location.href = 'https://www.linkedin.com/in/daneshwar-gobbani-baa69516a/';" id="myButton" class="float-left submit-button" >Channel 9</button>'''
    return href
col9.markdown(coll9(), unsafe_allow_html=True)




df=pd.read_csv("https://raw.githubusercontent.com/silexxx/test_videos_people_counting/main/hour.csv")
st.dataframe(df)

import plotly.express as px
fig = px.bar(df, x='timestamp', y='total_violations', height=500,width=1500,
              title='Total violations of Hairnet')


st.plotly_chart(fig)

# link = '[GitHub](http://github.com)'
# st.markdown(link, unsafe_allow_html=True)



# import streamlit as st 

# st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")



# def table():
#     href = '''<button onclick="location.href = 'www.yoursite.com';" id="myButton" class="float-left submit-button" >Home</button>'''
#     return href
# st.markdown(table(), unsafe_allow_html=True)




# # <input type="button" value="Button">

# def table():
#     href = '''<input type="button" value="Button">'''
#     return href
# st.markdown(table(), unsafe_allow_html=True)