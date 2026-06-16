# model.py

import joblib
import numpy as np

from algorithms.sorting import Sorting

# Load Model
model = joblib.load("crop_model.pkl")

# Load Label Encoder
encoder = joblib.load("label_encoder.pkl")


# Convert UI Inputs to Numerical Values
def convert_inputs(
    N,
    P,
    K,
    temp,
    humidity,
    rainfall,
    ph
):

    humidity_map = {
        "low": 30,
        "medium": 60,
        "high": 90
    }

    rainfall_map = {
        "none": 0,
        "low": 50,
        "medium": 120,
        "high": 250
    }

    ph_map = {
        "acidic": 5.5,
        "neutral": 7.0,
        "basic": 8.5
    }

    return [
        N,
        P,
        K,
        temp,
        humidity_map[humidity],
        ph_map[ph],
        rainfall_map[rainfall]
    ]


# Crop Recommendation Logic
def CropRecommender(data, farmer_inputs):

    probabilities = model.predict_proba([data])[0]

    crop_names = encoder.classes_

    crop_scores = []

    for crop, prob in zip(crop_names, probabilities):

        score = prob * 100

        # Market Preference Logic

        if farmer_inputs["market"] == "high_profit":

            profitable_crops = [
                "cotton",
                "coffee",
                "banana",
                "mango",
                "grapes"
            ]

            if crop in profitable_crops:
                score += 10

        elif farmer_inputs["market"] == "low_risk":

            stable_crops = [
                "rice",
                "maize",
                "wheat",
                "lentil"
            ]

            if crop in stable_crops:
                score += 10

        crop_scores.append(
            (crop, score)
        )

    # Sorting using DSA
    sorted_crops = Sorting.bubble_sort_descending(
        crop_scores
    )

    return sorted_crops[:3]