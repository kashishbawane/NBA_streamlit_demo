import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("NBA.csv")   # or "/mnt/data/NBA.csv" if needed

st.title("NBA Player Points Visualization")

# Quick fix: use the actual column names in this CSV
teams = df['bref_team_id'].unique()
selected_team = st.selectbox("Select a Team:", teams)

# Filter data
s = df[df['bref_team_id'] == selected_team]

# Plot players vs points
fig, ax = plt.subplots(figsize=(12, 6))
sb.barplot(x=s['player'], y=s['pts'], ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()

# Display chart
st.pyplot(fig)
