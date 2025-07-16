import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Capital Growth Simulator", layout="centered")
st.title("📈 Capital Growth Simulator")

# Inputs
capital = st.number_input("Initial Capital (₹)", min_value=10000, value=500000, step=10000)
roi = st.number_input("Annual ROI (%)", min_value=0.1, max_value=100.0, value=20.0, step=0.1)
years = st.slider("Duration (Years)", 1, 30, 3)
compound_freq = st.radio("Compounding Frequency", ["Monthly", "Yearly"])

# Calculate compound growth
periods = years * 12 if compound_freq == "Monthly" else years
periodic_roi = roi / 100 / 12 if compound_freq == "Monthly" else roi / 100

capital_history = [capital]
for _ in range(periods):
    capital += capital * periodic_roi
    capital_history.append(capital)

# Display results
st.subheader("Growth Summary")
st.write(f"**Final Capital after {years} years:** ₹{capital:,.2f}")

# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(range(len(capital_history)), capital_history, marker='o', color='green')
ax.set_title("Capital Growth Over Time")
ax.set_xlabel("Period")
ax.set_ylabel("Capital (₹)")
ax.grid(True)
st.pyplot(fig)

# Download option
capital_df = pd.DataFrame({
    "Period": list(range(len(capital_history))),
    "Capital": capital_history
})

csv = capital_df.to_csv(index=False)
st.download_button("📥 Download Growth Data as CSV", data=csv, file_name="capital_growth.csv", mime="text/csv")
