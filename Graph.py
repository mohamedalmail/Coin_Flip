import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Custom Graph Plotter")

# --- Graph Settings ---
st.header("1. Graph Configuration")

graph_title = st.text_input("Graph Title", value="My Graph")
x_label = st.text_input("X-axis Label", value="X")
y_label = st.text_input("Y-axis Label", value="Y")

x_scale = st.selectbox("X-axis Scale", ["Linear", "Logarithmic", "Polynomial"])
y_scale = st.selectbox("Y-axis Scale", ["Linear", "Logarithmic", "Polynomial"])

poly_degree = None
if x_scale == "Polynomial" or y_scale == "Polynomial":
    poly_degree = st.number_input("Polynomial Degree", min_value=1, max_value=10, value=2)

# --- Data Input Method ---
st.header("2. Provide Data")

data_method = st.radio("How would you like to provide the data?", ["Manual Entry", "Upload CSV"])

x_data = []
y_data = []

if data_method == "Manual Entry":
    x_input = st.text_area("Enter X values (comma-separated)", value="1, 2, 3, 4, 5")
    y_input = st.text_area("Enter Y values (comma-separated)", value="1, 4, 9, 16, 25")

    try:
        x_data = [float(i) for i in x_input.split(",")]
        y_data = [float(i) for i in y_input.split(",")]
    except:
        st.error("⚠️ Please enter valid numeric values separated by commas.")

else:
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of CSV:")
        st.dataframe(df)

        columns = df.columns.tolist()
        x_col = st.selectbox("Select X column", columns)
        y_col = st.selectbox("Select Y column", columns)

        x_data = df[x_col].values
        y_data = df[y_col].values

# --- Plot Button ---
if st.button("📈 Plot Graph"):
    if len(x_data) != len(y_data):
        st.error("❌ X and Y must have the same number of values.")
    elif len(x_data) == 0:
        st.warning("⚠️ Please enter or upload data.")
    else:
        fig, ax = plt.subplots()

        x_plot = np.array(x_data)
        y_plot = np.array(y_data)

        # Apply polynomial transformation if needed
        if x_scale == "Polynomial":
            x_plot = np.power(x_plot, poly_degree)
            ax.set_xlabel(f"{x_label} (x^{poly_degree})")
        else:
            ax.set_xlabel(x_label)

        if y_scale == "Polynomial":
            y_plot = np.power(y_plot, poly_degree)
            ax.set_ylabel(f"{y_label} (y^{poly_degree})")
        else:
            ax.set_ylabel(y_label)

        if x_scale == "Logarithmic":
            ax.set_xscale("log")
        if y_scale == "Logarithmic":
            ax.set_yscale("log")

        ax.plot(x_plot, y_plot, marker='o')
        ax.set_title(graph_title)
        ax.grid(True)

        st.pyplot(fig)
