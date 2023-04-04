from io import StringIO
import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
import os 
import streamlit-folium

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

df.reset_index(drop=True, inplace=True)
st.subheader('time statistics')
st.write(df['analysis_duration'].describe())
st.subheader('new dataset, removed unfinished AOIs')
st.write(df)


dfLandcoverDistributions = pd.DataFrame(columns = ['AOI', 'sumIrrigationDitch', 'sumGrass', 'sumRivers/Streams', 'sumImperviousSurface', 'sumLake/Pond', 
                                                  'sumCultivatedVegetation', 'sumBareGround', 'sumBuilding', 'sumTreatedPool', 'sumTrees/Canopy', 'sumUnknown', 'sumBush/Shrub',
                                                  'sumShadow'])
repeats = 0
while repeats < 68:
  sumIrrigationDitch = 0
  sumGrass = 0
  sumRiversXStreams = 0
  sumImperviousSurface = 0
  sumLakeXPondXContainer = 0
  sumCultivatedVegetation = 0
  sumBareGround = 0
  sumBuilding = 0
  sumTreatedPool = 0
  sumTreesXCanopyCover = 0
  sumUnknown = 0
  sumBushXShrub = 0
  sumShadow = 0
  AOInum = 0
  while AOInum < 37:
    sumIrrigationDitch += df.iloc[37*repeats + AOInum, 15]
    sumGrass += df.iloc[37*repeats + AOInum, 16]
    sumRiversXStreams += df.iloc[37*repeats + AOInum, 17]
    sumImperviousSurface += df.iloc[37*repeats + AOInum, 18]
    sumLakeXPondXContainer += df.iloc[37*repeats + AOInum, 19]
    sumCultivatedVegetation += df.iloc[37*repeats + AOInum, 20]
    sumBareGround += df.iloc[37*repeats + AOInum, 21]
    sumBuilding += df.iloc[37*repeats + AOInum, 22]
    sumTreatedPool += df.iloc[37*repeats + AOInum, 23]
    sumTreesXCanopyCover += df.iloc[37*repeats + AOInum, 24]
    sumUnknown += df.iloc[37*repeats + AOInum, 25]
    sumBushXShrub += df.iloc[37*repeats + AOInum, 26]
    sumShadow += df.iloc[37*repeats + AOInum, 27]
    AOInum += 1
  dfLandcoverDistributions.at[repeats, 'AOI'] = df.iloc[37*repeats, 0]
  dfLandcoverDistributions.at[repeats, 'sumIrrigationDitch'] = sumIrrigationDitch
  dfLandcoverDistributions.at[repeats, 'sumGrass'] = sumGrass
  dfLandcoverDistributions.at[repeats, 'sumRivers/Streams'] = sumRiversXStreams
  dfLandcoverDistributions.at[repeats, 'sumImperviousSurface'] = sumImperviousSurface
  dfLandcoverDistributions.at[repeats, 'sumLake/Pond'] = sumLakeXPondXContainer
  dfLandcoverDistributions.at[repeats, 'sumCultivatedVegetation'] = sumCultivatedVegetation
  dfLandcoverDistributions.at[repeats, 'sumBareGround'] = sumBareGround
  dfLandcoverDistributions.at[repeats, 'sumBuilding'] = sumBuilding
  dfLandcoverDistributions.at[repeats, 'sumTreatedPool'] = sumTreatedPool
  dfLandcoverDistributions.at[repeats, 'sumTrees/Canopy'] = sumTreesXCanopyCover
  dfLandcoverDistributions.at[repeats, 'sumUnknown'] = sumUnknown
  dfLandcoverDistributions.at[repeats, 'sumBush/Shrub'] = sumBushXShrub
  dfLandcoverDistributions.at[repeats, 'sumShadow'] = sumShadow
  repeats += 1
 
st.write(dfLandcoverDistributions)
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
csv = convert_df(dfLandcoverDistributions)

st.download_button(
   "Press to Download Above table as CSV",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv')

st.write('stats for irrigation ditch')
st.write(dfLandcoverDistributions['sumIrrigationDitch'].describe())
st.write('stats for Grass')
st.write(dfLandcoverDistributions['sumGrass'].describe())
st.write('stats for rivers/streams')
st.write(dfLandcoverDistributions['sumRivers/Streams'].describe())
st.write('stats for impervious surface')
st.write(dfLandcoverDistributions['sumImperviousSurface'].describe())
st.write('stats for lake/pond')
st.write(dfLandcoverDistributions['sumLake/Pond'].describe())
st.write('stats for cultivated vegetation')
st.write(dfLandcoverDistributions['sumCultivatedVegetation'].describe())
st.write('stats for bare ground')
st.write(dfLandcoverDistributions['sumBareGround'].describe())
st.write('stats for building')
st.write(dfLandcoverDistributions['sumBuilding'].describe())
st.write('stats for treated pool')
st.write(dfLandcoverDistributions['sumTreatedPool'].describe())
st.write('stats for trees/canopy')
st.write(dfLandcoverDistributions['sumTrees/Canopy'].describe())
st.write('stats for unknown')
st.write(dfLandcoverDistributions['sumUnknown'].describe())
st.write('stats for bush/shrub')
st.write(dfLandcoverDistributions['sumBush/Shrub'].describe())
st.write('stats for shadow')
st.write(dfLandcoverDistributions['sumShadow'].describe())
  
