import streamlit as st

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