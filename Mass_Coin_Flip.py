import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
st.title("Mass Coin Flip Simulator")
num_people = st.slider("How many people are flipping coins?", 0, 1000, 100)
num_flips = st.slider("How many coins does each person flip?", 0, 1000, 100)
results = []
for person in range(1, num_people + 1):
    flips = [random.choice(["Heads", "Tails"]) for _ in range(num_flips)]
    heads = flips.count("Heads")
    tails = flips.count("Tails")
    results.append({"Person": f"Person {person}", "Heads": heads, "Tails": tails})
df = pd.DataFrame(results)
if not df.empty:
    st.subheader("Summary Table")
    st.dataframe(df)
st.subheader("Histogram: Number of Heads per Person")
fig, ax = plt.subplots()
ax.hist(df["Heads"], bins=20)
ax.set_xlabel("Number of Heads")
ax.set_ylabel("Number of People")
st.pyplot(fig)
total_heads = df["Heads"].sum()
total_tails = df["Tails"].sum()
st.subheader("Overall Results")
st.write(f"Total Heads: {total_heads}")
st.write(f"Total Tails: {total_tails}")
st.warning("Select at least 1 person and 1 flip to run the simulation.")
