# app.py

import streamlit as st

from recommender import convert_inputs
from models import crop_recommender
from algorithms.searching import Searching

from data.crop_info import crop_info

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌾",
    layout="centered"
)


# =========================
# CREATE OBJECT
# =========================

recommender = crop_recommender.CropRecommender()


# =========================
# TITLE
# =========================

st.title("🌾 Smart Crop Recommendation System")

st.write(
    "Enter soil and environmental conditions to get the best crop recommendations."
)


# =========================
# INPUT SECTION
# =========================

st.subheader("🧪 Soil Nutrient Inputs")

N = st.number_input(
    "Nitrogen (N)",
    min_value=0,
    max_value=200,
    value=50
)

P = st.number_input(
    "Phosphorus (P)",
    min_value=0,
    max_value=200,
    value=50
)

K = st.number_input(
    "Potassium (K)",
    min_value=0,
    max_value=200,
    value=50
)


st.subheader("🌦 Environmental Inputs")

temp = st.number_input(
    "Temperature (°C)",
    min_value=0,
    max_value=50,
    value=25
)

humidity = st.selectbox(
    "Humidity Level",
    ["low", "medium", "high"]
)

rainfall = st.selectbox(
    "Rainfall Level",
    ["none", "low", "medium", "high"]
)

ph = st.selectbox(
    "Soil pH",
    ["acidic", "neutral", "basic"]
)


st.subheader("💹 Market Preference")

market = st.selectbox(
    "Select Market Preference",
    ["high_profit", "low_risk", "balanced"]
)


# =========================
# PREDICTION BUTTON
# =========================

if st.button("🌱 Get Crop Recommendation"):

    # Convert categorical inputs to numerical
    data = convert_inputs(
        N,
        P,
        K,
        temp,
        humidity,
        rainfall,
        ph
    )

    # Farmer preferences
    farmer_inputs = {
        "humidity": humidity,
        "rainfall": rainfall,
        "ph": ph,
        "temp": temp,
        "market": market
    }

    # Get recommendations
    results = recommender.get_recommendations(
        data,
        farmer_inputs
    )

    # =========================
    # DISPLAY RESULTS
    # =========================

    st.subheader("🌾 Top 3 Recommended Crops")

    medals = ["🥇", "🥈", "🥉"]

    for i, (crop, score) in enumerate(results):

        st.markdown(
            f"## {medals[i]} 🌱 {crop.upper()}"
        )

        st.progress(int(score))

        st.success(
            f"Suitability Score: {round(score, 2)} / 100"
        )

        # =========================
        # LINEAR SEARCH USAGE
        # =========================

        crop_names = list(crop_info.keys())

        if Searching.linear_search(
            crop_names,
            crop
        ):

            st.info(
                crop_info[crop]
            )

        else:

            st.warning(
                "Crop information not found."
            )

        st.markdown("---")

# =========================
# FOOTER
# =========================

st.caption(
    "Smart Farmer Crop Recommendation System using Machine Learning, OOP, and DSA"
)