import streamlit as st
import HeatmapGenerator as hm
import HeatmapPandas as hmp
import pandas as pd


df = pd.read_excel(r"Yazaki.xlsx")
print(df)
print(df.columns)
column1 = pd.DataFrame(df, columns=["PlantName"])
print(column1)
data1 = pd.DataFrame(df).to_numpy()
print(data1)


hm.get_chart_1()
hm.get_chart_2()
hm.get_chart_3(df)
#hmp.get_pdchart1()
#hmp.get_pdchart2()