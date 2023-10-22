import streamlit as st
import HeatmapGenerator as hm
import HeatmapPandas as hmp
import pandas as pd


df = pd.read_excel(r"Yazaki.xlsx")
print(df)
print(df.columns)
#column1 = pd.DataFrame(df, columns=["PlantName"])

dataArr = pd.DataFrame(df).to_numpy()
#print(data1)

PlantName = []
StateProvince = []
ManufacturingRegion = []
CountryName = []
Capacity = []
Usage = []
PreferredLogistics = []

for i in range(len(dataArr)):
    PlantName.append(dataArr[i][0])
    StateProvince.append(dataArr[i][1])
    ManufacturingRegion.append(dataArr[i][2])
    CountryName.append(dataArr[i][3])
    Capacity.append(dataArr[i][4])
    Usage.append(dataArr[i][5])
    PreferredLogistics.append(dataArr[i][6])

print(PlantName)
print(StateProvince)
print(ManufacturingRegion)
print(CountryName)
print(Capacity)
print(Usage)
print(PreferredLogistics)







#hm.get_chart_1()
#hm.get_chart_2()
#hm.get_chart_3(df)
#hmp.get_pdchart1()
#hmp.get_pdchart2()