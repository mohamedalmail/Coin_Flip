import streamlit as st
import random

st.title("🔁 Coin Flip Simulator")
st.subheader("Simulate up to 1000 people flipping up to 1000 coins")

# User inputs with both typing and scrolling support
num_people = st.number_input("Number of people", min_value=0, max_value=1000, value=500, step=1)
num_flips = st.number_input("Number of coin flips per person", min_value=0, max_value=1000, value=500, step=1)

def simulate_coin_flips(num_people, num_flips):
    result = {
        '10_heads_in_a_row': False,
        '10_tails_in_a_row': False,
        'person_index': None,
        'sequence': None
    }

    for person in range(num_people):
        flips = [random.choice(['H', 'T']) for _ in range(num_flips)]
        flip_str = ''.join(flips)

        if 'H' * 10 in flip_str:
            result['10_heads_in_a_row'] = True
            result['person_index'] = person
            result['sequence'] = flip_str
            break
        elif 'T' * 10 in flip_str:
            result['10_tails_in_a_row'] = True
            result['person_index'] = person
            result['sequence'] = flip_str
            break

    return result

if st.button("Run Simulation"):
    outcome = simulate_coin_flips(num_people, num_flips)

    if outcome['10_heads_in_a_row'] or outcome['10_tails_in_a_row']:
        st.success(f"🎉 Person #{outcome['person_index']} got 10 {'heads' if outcome['10_heads_in_a_row'] else 'tails'} in a row!")
        st.code(outcome['sequence'], language='text')
    else:
        st.warning("😕 No one
