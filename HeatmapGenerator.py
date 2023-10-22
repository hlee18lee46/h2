import streamlit as st
import pandas as pd
import math

def get_chart_1():
    import plotly.express as px

    fig = px.imshow([[1, 20, 30],
                     [20, 1, 60],
                     [30, 60, 1]])

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

def get_chart_2():
    import plotly.express as px

    df = px.data.medals_wide(indexed=True)
    fig = px.imshow(df)

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)



def get_chart_3(df):
    import plotly.express as px
    columns = df.columns.ravel()
    
    #getting the columns off of the data.
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
        if((dataArr[i][4]) is None or math.isnan(dataArr[i][4])):
            Capacity.append(0)
        else:
            Capacity.append(dataArr[i][4])
        if(dataArr[i][5] is None or math.isnan(dataArr[i][5])):
            Usage.append(0)
        else:
            Usage.append(dataArr[i][5])
        PreferredLogistics.append(dataArr[i][6])

    data=[PlantName, Capacity]
    fig = px.imshow(
                    #labels=dict(x=columns[0], y=columns[4], color="Capacity per Plant"),
                    data, text_audo=True
                   )
    fig.update_xaxes(side="top")

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)