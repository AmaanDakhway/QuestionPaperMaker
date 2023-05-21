import random as r
import pandas as pd
import streamlit as st
import csv

def app(subject): 
    csvsubjectname = subject+".csv"
    # print(csvsubjectname)
    s = st.container()
    df = pd.read_csv(csvsubjectname)

    q1 = df.index[df['Difficulty'] == 2].tolist()
    l_q1 = r.sample(q1,5)
    s.title("Question Paper")
    s.header("Q1. Attempt any four of the following: ")
    c=1
    for i in l_q1:
        s.write('Q'+str(c)+'. '+df.loc[i,'Questions'])
        c+=1

    q2 = df.index[df['Difficulty'] == 2].tolist()
    l_q2 = r.sample(q2,4)
    s.header("Q2. Attempt any three of the following: ")
    c=1
    for i in l_q2:
        s.write('Q'+str(c)+'. '+df.loc[i,'Questions'])
        c+=1