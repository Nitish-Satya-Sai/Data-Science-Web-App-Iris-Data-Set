# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 08:46:21 2022

@author: hp
"""
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
df_iris=sns.load_dataset("iris")
figure_scatter=px.scatter_3d(data_frame=df_iris,x="sepal_length",y="sepal_width",
                             z="petal_width",color="species")
st.write("""
# **Iris Dataset**
A 3D Scatter plot between sepal_length, sepal_width, and petal_width:-
""")
st.plotly_chart(figure_scatter,use_container_width=True)