from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ee
from functools import partial
from matplotlib.patches import Rectangle as MPLRect
import math
import geemap.foliumap as geemap
from sklearn.metrics import confusion_matrix
import seaborn as sns
from ipyleaflet import Rectangle, LayerGroup
import folium

import go_utils
from go_utils.constants import landcover_protocol

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-2.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted', 'Complete', 'lat', 'lon'])
df2 = pd.DataFrame(columns = ['AOI', 'lat', 'lon'])

i = 0
r = 0
numSet = 0
while i < 111:
  x = 0
  numCompleted = 0
  Finished = True
  while x < 37:
    y = df.iloc[37 * i + x, 7]
    if not pd.isna(y):
      numCompleted += 1
    else:
      Finished = False
    x += 1
  dfcheck.at[i, 'AOI'] = i
  dfcheck.at[i, 'NumCompleted'] = numCompleted
  dfcheck.at[i, 'Complete'] = Finished
  dfcheck.at[i, 'lat'] = df.iloc[i*37, 3]
  dfcheck.at[i, 'lon'] = df.iloc[i*37, 2]
  if Finished:
    numSet += 1
    df2.at[r, 'AOI'] = i
    df2.at[r, 'lat'] = dfcheck.iloc[i, 3]
    df2.at[r, 'lon'] = dfcheck.iloc[i, 4]  
    r += 1
  i += 1

g = str(numSet) + ' AOIs are complete'
st.header('Map of 68 Complete AOIs')
st.map(df2)
st.header('Table of AOIs and Number of Completed Plots')
st.write(dfcheck)
st.write(g)

      
  
