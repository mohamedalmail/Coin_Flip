import streamlit as st
import random
import pandas as pd

st.title("🪙 Coin Flip Counter")
st.subheader("Simulate people flipping coins and count heads & tails")

# User input
num_people = st.number_input("Number of people", min_value=0, max_value=100, value=10, step=1)
num_flips = st.number_input("Number of coin flips per person", min_value=0, max_value=1000, value=100, step=1)

# Coin flip function
def simulate_counts(num_people, num_flips):
    results = []

    for person in range(num_people):
        flips = [random.choice(['H', 'T']) for _ in range(num_flips)]
        heads = flips.count('H')
        tails = flips.count('T')
        results.append({
            "Person": person,
            "Heads": heads,
            "Tails": tails
        })

    return pd.DataFrame(results)

# Run simulation
if st.button("Run Simulation"):
    df = simulate_counts(num_people, num_flips)

    st.success("✅ Simulation complete!")
    st.dataframe(df, use_container_width=True)

    st.bar_chart(df.set_index("Person")[["Heads", "Tails"]])
