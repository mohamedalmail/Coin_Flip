import streamlit as st
import random
st.title("Coin Flip Simulator")
num_flips = st.slider("How many coins do you want to flip?", 0, 1000, 100)
results = [random.choice(["Heads", "Tails"]) for _ in range(num_flips)]
heads = results.count("Heads")
tails = results.count("Tails")
st.subheader("Results:")
st.write(f"Total Flips: {num_flips}")
st.write(f"Heads: {heads}")
st.write(f"Tails: {tails}")
st.subheader("Flip Counts")
st.bar_chart({"Heads": heads, "Tails": tails})
if num_flips > 0:
    running_heads_percentage = []
    heads_so_far = 0
    for i, flip in enumerate(results):
        if flip == "Heads":
            heads_so_far += 1
        running_heads_percentage.append(heads_so_far / (i + 1) * 100)

    st.subheader("Running Percentage of Heads")
    st.line_chart(running_heads_percentage)