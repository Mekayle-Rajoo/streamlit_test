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

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.content_based import content_model
from recommenders.background import set_bg_hack_url
from recommenders.streamlitfun import collab

# Data Loading
movies = pd.read_csv('resources/data/movies27000.csv')
train_data = pd.read_csv('resources/data/streamlit_ratings.csv')


# App declaration
def main():
    
    #Our background
    set_bg_hack_url("https://i.ibb.co/X2Phmfx/fall-movies-index-1628968089-02.jpg")
    
    #Our Logo
    st.image("resources/logogif.gif")

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","FAQ", "Insights","Download our app", "Contact Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.markdown('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image("resources/moviesgif.gif")
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',movies["title"][14930:15200])
        movie_2 = st.selectbox('Second Option',movies["title"][25055:25255])
        movie_3 = st.selectbox('Third Option',movies["title"][21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                
                try:
                
                    with st.spinner('Fetching movies...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("Here are some similar movies:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                
                try:
                
                    with st.spinner('Fetching movies ...'):
                        top_recommendations = collab(movie_1,movie_2, movie_3, 1990)
                    st.title("Users with similar taste also enjoyed:")
                    st.subheader("")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                        
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                        
                
                

    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")
        
    if page_selection == "Contact Us":
        st.title("Contact Us")
        st.write("Website: www.lumiere.com") 
        st.write("Address: 123 Richard St., Sandton, 1683") 
        st.write("Tel: +27 32 944 8443\n") 
        st.write("Operating Hours:")
        st.write("Monday - Friday, 8am - 5pm")
        st.write("Saturday, 8am - 1pm") 
        st.write("Sunday, 9am - 1pm")
        
    if page_selection == "FAQ":
        st.title("Frequently Asked Questions")
        select = st.selectbox("FAQ",("What is Lumiere?", "How much does it costs?","Which devices are supported by Lumiere?", "Can I share with my family?", "Can I download to watch offline?", "More questions?"))

        if select == "What is Lumiere?":
            st.write("Lumiere is a subscription-based streaming service that allows our users to watch movies without commercials on an internet-connected device. Lumiere content varies by region and may change over time. You can watch from a wide variety of award-winning movies, documentaries, and more. The more you watch, the better Lumiere gets at recommending movies we think you’ll enjoy.")
        if select == "How much does it costs?":
            st.write("Lumire offers different subscription options to fit a variety of budgets and entertainment needs. There are no hidden costs, long-term commitments, or cancellation fees, and you’re able to switch plans and add-ons at any time. After a free seven-days trail, Lumiere is billed on a monthly basis, unless you subscribe to a quarterly or annual plan. For full details about billing policies and procedures, please review our **Terms of Service**.")
        if select == "Which devices are supported by Lumiere?":
            st.write("You can use Lumiere through any internet-connected device that offers the Lumiere app, including smart TVs, game consoles, streaming media players, set-top boxes, smartphones, and tablets. You can also use Lumiere on your computer using an internet browser. You can review the **system requirements** for web browser compatibility, and check our **internet speed recommendations** to achieve the best performance.")
        if select == "Can I share with my family?":
            st.write("Of course. Lumiere lets you share your subscription with up to five family members.")
        if select == "Can I download to watch offline?":
            st.write("Absolutely. Download your movies to your to your iOS, Android, or Windows 10 device and watch them anywhere, anytime without a Wi-Fi or internet connection.")
        if select == "More questions?":
            st.write("Visit our **Contact Us** page.")
            
    if page_selection == "Download our app":
        st.title("Download our app")
        st.write("The Lumiere app lets you download shows and movies to watch offline.") 
        st.write("It is available for Android and Apple phones. Go to the app store on your device, search ‘Lumiere’, select and download.")
        st.write("To start watching, sign up at www.lumiere.com .")
        st.write("Enjoy Binge-Watching!")
        st.image('resources/imgs/app.jpg', width = 350)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()