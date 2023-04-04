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
  sumBushXSchrub = 0
  sumShadow = 0
  AOInum = 0
  while AOInum < 37:
    sumIrrigationDitch += df.iloc[37*repeats + AOI][15]
    sumGrass += df.iloc[37*repeats + AOI][16]
    sumRiversXStreams += df.iloc[37*repeats + AOI][17]
    sumImperviousSurface += df.iloc[37*repeats + AOI][18]
    sumLakeXPondXContainer += df.iloc[37*repeats + AOI][19]
    sumCultivatedVegetation += df.iloc[37*repeats + AOI][20]
    sumBareGround += df.iloc[37*repeats + AOI][21]
    sumBuilding += df.iloc[37*repeats + AOI][22]
    sumTreatedPool += df.iloc[37*repeats + AOI][23]
    sumTreesXCanopyCover += df.iloc[37*repeats + AOI][24]
    sumUnknown += df.iloc[37*repeats + AOI][25]
    sumBushXSchrub += df.iloc[37*repeats + AOI][26]
    sumShadow += df.iloc[37*repeats + AOI][27]
    AOInum += 1
  dfLandcoverDistributions.iloc[repeats, 'AOI'] = df.iloc[repeats*37][0]
  dfLandcoverDistributions.iloc[repeats, 'sumIrrigationDitch'] = sumIrrigationDitch
  dfLandcoverDistributions.iloc[repeats, 'sumGrass'] = sumGrass
  dfLandcoverDistributions.iloc[repeats, 'sumRivers/Streams'] = sumRiversXStreams
  dfLandcoverDistributions.iloc[repeats, 'sumImperviousSurface'] = sumImperviousSurface
  dfLandcoverDistributions.iloc[repeats, 'sumLake/Pond'] = sumLakeXPondXContainer
  dfLandcoverDistributions.iloc[repeats, 'sumCultivatedVegetation'] = sumCultivatedVegetation
  dfLandcoverDistributions.iloc[repeats, 'sumBareGround'] = sumBareGround
  dfLandcoverDistributions.iloc[repeats, 'sumBuilding'] = sumBuilding
  dfLandcoverDistributions.iloc[repeats, 'sumTreatedPool'] = sumTreatedPool
  dfLandcoverDistributions.iloc[repeats, 'sumTrees/Canopy'] = sumTreesXCanopyCover
  dfLandcoverDistributions.iloc[repeats, 'sumUnknown'] = sumUnknown
  dfLandcoverDistributions.iloc[repeats, 'sumBush/Shrub'] = sumBushXShrub
  dfLandcoverDistributions.iloc[repeats, 'sumShadow'] = sumShadow
  repeats += 1
  
st.write(dfLandCoverDistributions)
  
