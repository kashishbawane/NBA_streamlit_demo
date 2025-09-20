import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("NBA.csv")

st.title("NBA Player Performance Visualization")

# Show available teams
teams = df['Team'].unique()
selected_team = st.selectbox("Select a Team:", teams)

# Filter data
team_data = df[df['Team'] == selected_team]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
sb.barplot(x=team_data['Player'], y=team_data['PTS'], ax=ax)
plt.xticks(rotation=90)
plt.ylabel("Total Points (PTS)")
plt.xlabel("Player")
plt.title(f"Points scored by players in {selected_team}")
plt.tight_layout()

# Display chart
st.pyplot(fig)
