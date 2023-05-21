import pandas as pd
import streamlit as st

import medium_qp
import hard_qp
import easy_qp
from PIL import Image

def space(ele,num):
    for i in range(num):
        ele.text(" ")

st.set_page_config(page_title='QPM-CMPN-A',page_icon="qmaker.png")

m = st.markdown("""
<style>
div.stButton > button:first-child {
height: 3em;
width: 13em; 
}
</style>""", unsafe_allow_html=True)

read_ai = pd.read_csv('ai.csv')
read_ai.sort_values(["Difficulty"])

read_os = pd.read_csv('os.csv')
read_os.sort_values(["Difficulty"])

read_sql = pd.read_csv('sql.csv')
read_sql.sort_values(["Difficulty"])

read_ds = pd.read_csv('ds.csv')
read_ds.sort_values(["Difficulty"])

read_other = pd.read_csv('other.csv')
read_other.sort_values(["Difficulty"])

cont_title = st.container()
col1, col2 = st.columns([1,20])
logo = Image.open('qmaker.png')
with cont_title:
    with col1:
        st.image(logo, width=120)
    with col2:
        st.markdown('<h1 style="float: right;">Question Paper Maker</h1>',unsafe_allow_html=True)

cont1 = st.container()
cont2 = st.container()
cont3 = st.container()
cont1.subheader("Select the subject for the paper:")

sel_sub = cont1.selectbox("",('AI', 'OS', 'SQL', 'DS', 'Other'))
space(cont1,1)

show = cont1.button("Display Question Bank")
if show:
    if sel_sub == 'AI':
        cont2.write(read_ai.sort_values(["Difficulty"]))
    elif sel_sub == 'OS':
        cont2.write(read_os.sort_values(["Difficulty"]))
    elif sel_sub == 'SQL':
        cont2.write(read_sql.sort_values(["Difficulty"]))
    elif sel_sub == 'DS':
        cont2.write(read_ds.sort_values(["Difficulty"]))
    else:
        cont2.write(read_other.sort_values(["Difficulty"]))
space(cont2,1)
col1, col2, col3 = st.columns([1,1,1])
with cont3:
    with col1:
        easy = st.button("Easy")
    with col2:
        medium = st.button("Medium")
    with col3:
        hard = st.button("Hard")
    
if easy:
    easy_qp.app(sel_sub.lower())
if medium:
    medium_qp.app(sel_sub.lower())
if hard:
    hard_qp.app(sel_sub.lower())