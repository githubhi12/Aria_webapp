import streamlit as st
import pandas as pd
import os

if not os.path.exists('data'):
    os.makedirs("data")
if not os.path.exists('data/expenses.csv'):
    expenses=pd.DataFrame(columns=["date","category","description","currency","amount"])
    expenses.to_csv("data/expenses.csv",index=False)

date=st.date_input("Date 📅 ")

category=st.selectbox("Category" ,("Food🍉", "personal care🧩", "Housing🏘️", "loan💲", "traveling🚗","other stuff🎲"))
description=st.text_input("description",key="Description_HI")
currency=st.selectbox("Currency",("dollars 💵 ","Euros 💶 "))
amount=st.number_input("Amount💲",max_value=100000000,step=1,key="Amount_HI")

def insert():
    insert_csv(date,category,description,currency,amount)
def insert_csv(date,category,description,currency,amount):
    DataFrame=pd.read_csv("data/expenses.csv")
    DataFrame.loc[len(DataFrame)]= [date,category,description,currency,amount]
    DataFrame.to_csv("data/expenses.csv",index=False)
    
button=st.button("Add Expense",on_click=insert)

def delete():
    st.session_state.Amount_HI=0
    st.session_state.Description_HI=""

button=st.button("Clear Expense", on_click=delete)

