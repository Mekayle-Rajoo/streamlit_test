"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import joblib,os
import streamlit.components.v1 as components


# Data handling dependencies
import pandas as pd
import numpy as np
import random
import re
from PIL import Image

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from recommenders.streamlitfun import collab 
# Data Loading
movies = pd.read_csv('resources/data/movies1.csv')
train_data = pd.read_csv('resources/data/ratings1.csv')

unpickled_model = joblib.load(open("resources/models/SVD.pkl","rb"))


def callback():
    st.session_state.button_clicked = True
    

    
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.ibb.co/Smvzshf/fall-movies-index-1628968089-01.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    
    # Creates a main title and subheader on your page -
    # these are static across all pages
  
    #set_bg_hack_url()
   
    
    st.image("resources/logogif.gif")
    
   
    #components.html("<style>:root {background-color: grey;}</style>" + b)
    
    page_options = ["HOME","Solution Overview", "FAQ", "Insights","Download our app", "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    
    if page_selection == "FAQ":
            st.write("here are some questions")
            select = st.selectbox("FAQ",("What is Netflix?","How much does it cost?"))
            
            if select == "What is Netflix?":
                st.write("Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries, and more on thousands of internet-connected devices.You can watch as much as you want, whenever you want without a single commercial – all for one low monthly price. There's always something new to discover and new TV shows and movies are added every week!")
            if select == "How much does it cost?":
                st.write("Watch Netflix on your smartphone, tablet, Smart TV, laptop, or streaming device, all for one fixed monthly fee. Plans range from R49 to R199 a month. No extra costs, no contracts.")
    
    if page_selection == "HOME":
        # Header contents
     
        if "button_clicked" not in st.session_state:    
            st.session_state.button_clicked = False
        
        st.image("resources/moviesgif.gif")
        
        
        genre = st.radio( "New to Lumiere? Sign up or login in if you have an account",('login', 'sign up'))
        
        if genre == "sign up":
            email = st.text_input('Ready to watch? Enter your email to start a membership', '')
            
            if (st.button("Next", on_click = callback) or st.session_state.button_clicked): 
            
                if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)):
                    st.write('Welcome to Lumiere', email.split("@")[0].capitalize(),","," looks like you are new here.\n To customize your\
                    experience please select 3 movies which you enjoy.")

                    movie_1 = st.selectbox('First Option',movies["title"][14930:15200])
                    movie_2 = st.selectbox('Second Option',movies["title"][25055:25255])
                    movie_3 = st.selectbox('Third Option',movies["title"][21100:21200])
                    fav_movies = [movie_1,movie_2,movie_3]

                    # Perform top-10 movie recommendation generation


                    if st.button("Recommend"):
                        top_recommendations = content_model(movie_list=fav_movies,top_n=10)
                        st.title("We think you'll like:")
                        for i,j in enumerate(top_recommendations):
                            st.subheader(str(i+1)+'. '+j)
                            
                else:
                    st.write("Please enter a valid email")
                    
            
                
        if genre == "login":
            
            title = st.text_input('email address', '')
            password = st.text_input('password', '', type="password")
      
         
            if (st.button("Login", on_click = callback) or st.session_state.button_clicked):
                
            
                if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',title)) and password != "":

                    st.write('Welcome back to Explore!', title.split("@")[0].capitalize(),"userId ","(",random.randint(0, 10000038),")","here are some titles we think you may enjoy")

                    movie_1 = st.selectbox('First Option',movies["title"][14930:15200])
                    movie_2 = st.selectbox('Second Option',movies["title"][25055:25255])
                    movie_3 = st.selectbox('Third Option',movies["title"][21100:21200])
                    
                    if st.button("Recommend"):
                        tops = collab(movie_1,movie_2, movie_3, 1990)
                        st.subheader("Users with similar taste also enjoyed:")
                        st.subheader("")
                        for i in range(10):
                            st.image(tops["image"][i], width = 150)
                            st.subheader(tops["title"][i])
                            st.subheader(tops["imdblinks"][i])
                            st.subheader(" ")
                            st.subheader(" ")
                            


                else:
                    st.write("Please enter valid login details")
        

        
                

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
