from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import math

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-3.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted', 'Complete', 'lat', 'lon'])
df2 = pd.DataFrame(columns = ['AOI', 'lat', 'lon', 'avg time'])
dfTime = pd.DataFrame(columns = ['AOI', 'Avg Time'])

i = 0
r = 0
numSet = 0
while i < 111:
  x = 0
  numCompleted = 0
  totalTime = 0
  Finished = True
  while x < 37:
    y = df.iloc[37 * i + x, 7]
    time = df.iloc[37 * i + x, 12]
    if not pd.isna(y):
      numCompleted += 1
      if time < 1000: 
        totalTime += time
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
    dfTime.at[r, 'AOI'] = i
    df2.at[r, 'lat'] = dfcheck.iloc[i, 3]
    df2.at[r, 'lon'] = dfcheck.iloc[i, 4]  
    dfTime.at[r, 'avg time'] = totalTime / 37
    r += 1
  i += 1

g = str(numSet) + ' AOIs are complete'
st.header('Map of 68 Complete AOIs')
st.map(df2)
st.header('Table of AOIs and Number of Completed Plots')
st.write(dfcheck)
st.write(g)
st.barChart(dfTime)

      
  
