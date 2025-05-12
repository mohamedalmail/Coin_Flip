import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
pip install matplotlib

# Title
st.title("🎯 Projectile Motion Simulator")
st.markdown("Simulates the motion of a projectile launched at an angle.")

# Input parameters
velocity = st.number_input("Initial Velocity (m/s)", min_value=0.0, value=20.0, step=1.0)
angle_deg = st.number_input("Launch Angle (degrees)", min_value=0.0, max_value=90.0, value=45.0, step=1.0)
gravity = st.number_input("Gravity (m/s²)", min_value=1.0, value=9.81, step=0.1)
initial_height = st.number_input("Initial Height (m)", min_value=0.0, value=0.0, step=0.5)

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Initial velocities
v_x = velocity * np.cos(angle_rad)
v_y = velocity * np.sin(angle_rad)

# Time of flight calculation
discriminant = v_y**2 + 2 * gravity * initial_height
t_flight = (v_y + np.sqrt(discriminant)) / gravity

# Time points
t = np.linspace(0, t_flight, num=500)

# Position equations
x = v_x * t
y = initial_height + v_y * t - 0.5 * gravity * t**2

# Max height
t_peak = v_y / gravity
h_max = initial_height + v_y * t_peak - 0.5 * gravity * t_peak**2
range_dist = v_x * t_flight

# Plotting
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Projectile Trajectory")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Height (m)")
ax.grid(True)

st.pyplot(fig)

# Display key results
st.subheader("🔍 Key Results")
st.write(f"**Time of flight:** {t_flight:.2f} seconds")
st.write(f"**Maximum height:** {h_max:.2f} meters")
st.write(f"**Horizontal range:** {range_dist:.2f} meters")
