import streamlit as st

def set_bg_hack_url(url):

    
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
             background: url(url);
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )