from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-3.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted', 'Complete', 'lat', 'lon', 'Avg Time'])
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
    dfcheck.at[i, 'Avg Time'] = totalTime/ 37
    numSet += 1
    df2.at[r, 'AOI'] = i
    dfTime.at[r, 'AOI'] = i
    df2.at[r, 'lat'] = dfcheck.iloc[i, 3]
    df2.at[r, 'lon'] = dfcheck.iloc[i, 4]  
    dfTime.at[r, 'Avg Time'] = totalTime / 37
    r += 1
  i += 1

st.header('Table of AOIs and Number of Completed Plots')
st.write(dfcheck)
st.header('Map of 68 Complete AOIs')
st.map(df2)
ww = alt.Chart(dfTime, title = 'Average Time (seconds) per plot for 68 Completed AOIs').mark_bar().encode(x="AOI", y="Avg Time")
st.altair_chart(ww)

z = True
for AOI in df["AOI"]:
    if dfTime["AOI"].isin([AOI]).any():
      z = False
    else:
       row = df[df["AOI"] == AOI]
       index = row.index[0]
       df = df.drop(index)  
zz = 0
while zz < len(df):
  qq = df.iloc[zz]['analysis_duration']
  if qq > 1500:
    df.iloc[zz, df.columns.get_loc('analysis_duration')] = np.nan
  zz += 1

st.write(df['analysis_duration'].describe())
st.write(df)


  
