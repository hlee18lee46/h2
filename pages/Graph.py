import streamlit as st
import HeatmapGenerator as hm
import HeatmapPandas as hmp
import pandas as pd


df = pd.read_excel(r"Yazaki.xlsx")
print(df)
print(df.columns)


hm.get_chart_1()
hm.get_chart_2()
hm.get_chart_3(df)
#hmp.get_pdchart1()
#hmp.get_pdchart2()