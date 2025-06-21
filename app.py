import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import plotly.express as px

st.title("Mi primera app en Streamlit")

st.write("**¡Hola mundo!**")

url_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"

df = pd.read_csv(url_data)

st.header("Dataset de tips")

min_tip = st.slider("Seleccione un valor mínimo",
                    min_value=1.0, max_value=10.0, step=0.5)

st.dataframe(df.query("tip>=@min_tip"))

st.subheader("Propina promedio por día de la semana")

tip_by = df.groupby("day")["tip"].mean()

st.bar_chart(tip_by)

fig1 = px.box(df, y="total_bill")
st.plotly_chart(fig1)


if "mostrar" not in st.session_state:

    st.session_state.mostrar = False

if not st.session_state.mostrar:

    if st.button("Mostrar histograma"):

        st.session_state.mostrar = True

        st.rerun()

else:

    st.subheader("Histograma de la cuenta")

    st.write("El usuario ya presionó el botón")

    fig, (ax1, ax2) = plt.subplots(1, 2)

    df["tip"].hist(ax=ax1)

    tip_by.plot(kind="bar", ax=ax2)

    st.pyplot(fig)
