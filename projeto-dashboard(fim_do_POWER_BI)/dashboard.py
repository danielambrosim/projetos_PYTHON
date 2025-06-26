import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Leitura e preparação
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].dt.strftime("%Y-%m")

month = st.sidebar.selectbox("Selecione o mês", sorted(df["Month"].unique()))
df_filtered = df[df["Month"] == month]
st.dataframe(df_filtered)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# 1. Faturamento por Dia (Barras verticais, cor por valor)
fig_date = px.bar(
    df_filtered.groupby("Date")["Total"].sum().reset_index(),
    x="Date", y="Total",
    title="Faturamento diário",
    color="Total",
    color_continuous_scale="blues"
)
fig_date.update_layout(xaxis_title="Data", yaxis_title="Faturamento (R$)")
col1.plotly_chart(fig_date, use_container_width=True)

# 2. Faturamento por Tipo de Produto (ordem decrescente)
prod_total = df_filtered.groupby("Product line")["Total"].sum().reset_index().sort_values("Total", ascending=False)
fig_prod = px.bar(
    prod_total,
    x="Total", y="Product line",
    orientation="h",
    title="Faturamento por tipo de produto",
    color="Total",
    color_continuous_scale="greens"
)
fig_prod.update_layout(xaxis_title="Faturamento (R$)", yaxis_title="Tipo de Produto")
col2.plotly_chart(fig_prod, use_container_width=True)

# 3. Faturamento por Filial (Cidade)
city_total = df_filtered.groupby("City")["Total"].sum().reset_index().sort_values("Total", ascending=False)
fig_city = px.bar(
    city_total,
    x="City", y="Total",
    title="Faturamento por filial",
    color="City"
)
fig_city.update_layout(yaxis_title="Faturamento (R$)")
col3.plotly_chart(fig_city, use_container_width=True)

# 4. Faturamento por Tipo de Pagamento (Pizza)
payment_total = df_filtered.groupby("Payment")["Total"].sum().reset_index()
fig_kind = px.pie(
    payment_total,
    values="Total", names="Payment",
    title="Faturamento por tipo de pagamento",
    hole=0.4
)
col4.plotly_chart(fig_kind, use_container_width=True)

# 5. Avaliação média por Filial (Barras horizontais)
city_rating = df_filtered.groupby("City")["Rating"].mean().reset_index().sort_values("Rating", ascending=True)
fig_rating = px.bar(
    city_rating,
    x="Rating", y="City",
    orientation="h",
    title="Avaliação média por filial",
    color="Rating",
    color_continuous_scale="reds"
)
fig_rating.update_layout(xaxis_title="Nota Média", yaxis_title="Filial")
col5.plotly_chart(fig_rating, use_container_width=True)
