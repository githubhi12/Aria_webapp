import streamlit as st
import os
import pandas as pd
if not os.path.exists('data/rating.csv'):
    rating=pd.DataFrame(columns=["name","feedback","rating"])
    rating.to_csv("data/rating.csv",index=False)

name=st.text_input("Name")
feedback=st.text_input("Feedback")
rating=st.slider("Rating",min_value=1,max_value=5)

if rating==1:
    st.subheader("RATE IT HIGHER😡")

if rating==2:
    st.subheader("RATE IT 5😡")

if rating==3:
    st.subheader("5 IS THE BEST😡")

if rating==4:
    st.subheader("Thank you for giving a good rating🙂")

if rating==5:
    st.subheader("THANK YOU FOR GIVING THE BEST RATING😀")


def insert():
    insert_csv(name,feedback,rating)
def insert_csv(name,feedback,rating):
    DataFrame=pd.read_csv("data/rating.csv")
    DataFrame.loc[len(DataFrame)]= [name,feedback,rating]
    DataFrame.to_csv("data/rating.csv",index=False)
    st.balloons()


button=st.button("Submit",on_click=insert)


