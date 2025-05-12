import streamlit as st
import random

st.title("🪙 Coin Flip Results for Each Person")
st.subheader("Simulate 0–100 people flipping up to 1000 coins")

# Input fields
num_people = st.number_input("Number of people", min_value=0, max_value=100, value=10, step=1)
num_flips = st.number_input("Number of coin flips per person", min_value=0, max_value=1000, value=50, step=1)

# Function to simulate flips
def simulate_all_flips(num_people, num_flips):
    all_results = []
    streak_results = []

    for person in range(num_people):
        flips = [random.choice(['H', 'T']) for _ in range(num_flips)]
        flip_str = ''.join(flips)
        streak_10 = 'H'*10 in flip_str or 'T'*10 in flip_str
        all_results.append((person, flip_str))
        streak_results.append(streak_10)

    return all_results, streak_results

# Run simulation
if st.button("Run Simulation"):
    all_results, streak_results = simulate_all_flips(num_people, num_flips)

    st.subheader("📝 Coin Flip Results:")
    for i, (person_index, sequence) in enumerate(all_results):
        st.text
