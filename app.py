import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("NBA.csv")

st.title("NBA Player Points Visualization")

# Show available teams
teams = df['Team'].unique()
selected_team = st.selectbox("Select a Team:", teams)

# Filter data
s = df[df['Team'] == selected_team]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
sb.barplot(x=s['Player'], y=s['Points'], ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()

# Display chart
st.pyplot(fig)
