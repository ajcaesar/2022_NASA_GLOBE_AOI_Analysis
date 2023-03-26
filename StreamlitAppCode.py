import numpy as np
import pandas as pd
import streamlit as st
from io import StringIO

st.title('Which AOIs are complete')
df = pd.read_csv("AOI Updated Comparisons  - imported from collect earth online-2.csv")
dfcheck = pd.DataFrame(columns = ['AOI', 'NumCompleted'])

st.write(df.iloc[5, 7])
st.write(df.iloc[5, 7] == nan)
#i = 0
#while i < 110:
 # x = 0
  #numCompleted = 0
  #Finished = False
 # while x < 37
  #df.iloc[37 * i + x, 7] != 
