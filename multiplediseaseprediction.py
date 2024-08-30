# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:34:19 2024

@author: hp
"""
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/multiple disease prediction system/saved files/diabetes_model.sav'))
heart_disease_model = pickle.load(open('C:/Users/hp/OneDrive/Desktop/multiple disease prediction system/saved files/heart_disease_model.sav'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction','Heart Disease Prediction'], default_index = 0)