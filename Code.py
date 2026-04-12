import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Supply Chain Digital Twin", layout="wide")

st.title("🚚 AI Supply Chain Digital Twin")
st.markdown("Simulate supply chain scenarios and predict outcomes")

# -----------------------------
# INPUTS
# -----------------------------
st.sidebar.header("⚙️ Supply Chain Inputs")

demand = st.sidebar.slider("Daily Demand", 100, 1000, 500)
production = st.sidebar.slider("Production Capacity", 100, 1000, 600)
lead_time = st.sidebar.slider("Delivery Lead Time (days)", 1, 10, 3)
inventory = st.sidebar.slider("Initial Inventory", 0, 1000, 300)

days = 30

# -----------------------------
# SIMULATION
# -----------------------------
inventory_levels = []
stockouts = 0

for day in range(days):

    # production adds inventory
    inventory += production

    # demand reduces inventory
    if inventory >= demand:
        inventory -= demand
    else:
        stockouts += 1
        inventory = 0

    inventory_levels.append(inventory)

# -----------------------------
# COST CALCULATION
# -----------------------------
holding_cost = sum(inventory_levels) * 0.5
stockout_cost = stockouts * 1000

total_cost = holding_cost + stockout_cost

# -----------------------------
# OUTPUT
# -----------------------------
st.subheader("📊 Supply Chain Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Final Inventory", inventory)
c2.metric("Stockout Days", stockouts)
c3.metric("Total Cost", int(total_cost))

# -----------------------------
# VISUALIZATION
# -----------------------------
st.subheader("📈 Inventory Over Time")

fig, ax = plt.subplots()
ax.plot(inventory_levels)
ax.set_xlabel("Days")
ax.set_ylabel("Inventory")

st.pyplot(fig)

# -----------------------------
# AI INSIGHT
# -----------------------------
st.subheader("🧠 AI Recommendations")

if stockouts > 5:
    st.error("High stockout risk → Increase production or inventory")

elif total_cost > 20000:
    st.warning("High holding cost → Optimize inventory levels")

else:
    st.success("Balanced supply chain performance")