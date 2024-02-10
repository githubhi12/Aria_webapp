import streamlit as st
tab1,tab2,tab3=st.tabs(["About","Hobbies","Contact"])
tab2.write("🍉 I like to draw , read ,writing stories, and coding😀")
tab3.write("Email - funworldaria@gmail.com")
with tab1:
    col1,col2=st.columns([0.3,0.7])

with col1:
    st.image("IMG_0012.jpg",width=200)
    st.subheader("Aria Verma🐔")



    