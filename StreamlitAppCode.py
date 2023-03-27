import numpy as np
import math 
import pandas as pd
import streamlit as st
from io import StringIO

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-2.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted', 'Complete', 'lat', 'lon'])

i = 0
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
  i += 1

df2 = dfcheck[['lat', 'lon']]
g = numSet + ' AOIs are complete'
st.map(df2)
st.write(dfcheck)
st.write(g)

      
  
