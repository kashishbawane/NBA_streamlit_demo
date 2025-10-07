import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="NBA Player Points Dashboard", page_icon="🏀", layout="wide")

# --- Load Data ---
df = pd.read_csv("NBA.csv")   # Make sure the CSV path is correct

st.title("🏀 NBA Player Points Analyzer")
st.markdown("Visualize and compare player performances across NBA teams with interactive filters and charts.")

# --- Sidebar Controls ---
st.sidebar.header("⚙️ Filter Options")

teams = sorted(df['bref_team_id'].unique())
selected_team = st.sidebar.selectbox("Select a Team:", teams)

chart_type = st.sidebar.radio("Select Chart Type:", ["Bar Chart", "Pie Chart", "Scatter Plot"])
sort_option = st.sidebar.radio("Sort Players By:", ["Points (High → Low)", "Alphabetical"])

# --- Filter Data ---
team_data = df[df['bref_team_id'] == selected_team]

# --- Sorting ---
if sort_option == "Points (High → Low)":
    team_data = team_data.sort_values(by="pts", ascending=False)
else:
    team_data = team_data.sort_values(by="player")

# --- Layout for Summary ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Players", len(team_data))
col2.metric("Average Points", f"{team_data['pts'].mean():.2f}")
col3.metric("Top Scorer", team_data.iloc[0]['player'])

st.markdown("---")

# --- Plot Section ---
st.subheader(f"📊 {selected_team} Players' Performance")

fig, ax = plt.subplots(figsize=(12, 6))

if chart_type == "Bar Chart":
    sb.barplot(x=team_data['player'], y=team_data['pts'], ax=ax, palette="mako")
    plt.xticks(rotation=90)
    plt.ylabel("Points Scored")
    plt.title(f"{selected_team} Player Points")

elif chart_type == "Pie Chart":
    plt.pie(team_data['pts'], labels=team_data['player'], autopct='%1.1f%%', startangle=90)
    plt.title(f"{selected_team} Points Distribution")

elif chart_type == "Scatter Plot":
    sb.scatterplot(x="player", y="pts", data=team_data, s=100, color="orange", ax=ax)
    plt.xticks(rotation=90)
    plt.title(f"{selected_team} Player Points Scatter")

plt.tight_layout()
st.pyplot(fig)

# --- Data Table Toggle ---
if st.checkbox("📋 Show Team Data Table"):
    st.dataframe(team_data[['player', 'pts', 'bref_team_id']].reset_index(drop=True))

# --- Footer ---
st.markdown("---")
st.markdown("Developed with ❤️ using **Streamlit** | Data Source: NBA Stats")
