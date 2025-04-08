import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Načtení fiktivního datasetu
@st.cache
def load_data():
    months = pd.date_range(start="2024-01-01", end="2025-03-01", freq="MS")
    branches = ["Praha", "Brno", "Ostrava", "Plzeň", "Hradec Králové"]
    
    data = []
    for month in months:
        for branch in branches:
            cars_sold = np.random.randint(20, 100)
            revenue = cars_sold * np.random.uniform(500_000, 900_000)
            cost_of_sales = revenue * np.random.uniform(0.6, 0.8)
            gross_margin = revenue - cost_of_sales
            opex = np.random.uniform(1_000_000, 5_000_000)
            ebitda = gross_margin - opex
            data.append([
                month.strftime("%Y-%m"), branch, cars_sold, round(revenue),
                round(cost_of_sales), round(gross_margin), round(opex), round(ebitda)
            ])
    
    df = pd.DataFrame(data, columns=[
        "Datum", "Prodejna", "Prodaná auta", "Výnosy",
        "Náklady na prodej", "Hrubá marže", "OPEX náklady", "EBITDA"
    ])
    return df

# Načtení dat
df = load_data()

# Základní rozhraní
st.title("Report prodeje aut")
st.write("Tento dashboard zobrazuje data o prodejích aut na různých prodejnách.")
st.dataframe(df)

# Zobrazení grafu
st.subheader("Tržby podle měsíců a prodejen")
pivot_df = df.pivot_table(values="Výnosy", index="Datum", columns="Prodejna", aggfunc="sum")
st.line_chart(pivot_df)

# Výběr prodejny
selected_branch = st.selectbox("Vyber prodejnu", df["Prodejna"].unique())
filtered_data = df[df["Prodejna"] == selected_branch]
st.write(f"Data pro prodejnu: {selected_branch}")
st.dataframe(filtered_data)