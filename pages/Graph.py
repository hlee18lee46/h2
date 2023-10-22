import streamlit as st
import HeatmapGenerator as hm
import HeatmapPandas as hmp
import pandas as pd


df = pd.read_excel(r"Yazaki.xlsx")
print("First row" + df[0])
print("second row" + df[1])
print("third row" + df[2])
print(df)

hm.get_chart_1()
hm.get_chart_2()

#hmp.get_pdchart1()
#hmp.get_pdchart2()