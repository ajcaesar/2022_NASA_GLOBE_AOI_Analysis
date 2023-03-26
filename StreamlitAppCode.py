import numpy as np
import math 
import pandas as pd
import streamlit as st
from io import StringIO

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-2.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted'])

i = 0
while i < 110:
  x = 0
  numCompleted = 0
  Finished = True
  while x < 37:
    y = df.iloc[37 * i + x, 7]
    if not pd.isna(y):
      numCompleted += 0
    else:
      Finished = False
    x += 1
  st.write(i)
  st.write(numCompleted)
  st.write(Finished)
  i += 1
    
    
