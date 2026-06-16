import joblib
import numpy as np
from algorithms.sorting import Sorting

class CropRecommender:
    def __init__(self):

        self.model = joblib.load("crop_model.pkl")
        self.encoder = joblib.load("label_encoder.pkl")
    
    def get_recommendations(self, data, farmer_inputs):

        probabilities = self.model.predict_proba([data])[0]

        crop_names = self.encoder.classes_

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
                    "lentil",
                    "chickpea"
                ]

                if crop in stable_crops:
                    score += 10

            crop_scores.append(
                (crop, score)
            )

        # Sort crops
        sorted_crops = Sorting.bubble_sort_descending(crop_scores)

        # Top 3 crops
        top_3 = sorted_crops[:3]

        # Highest score among top 3
        highest_score = top_3[0][1]

        normalized_results = []

        # Normalize scores to 100
        for crop, score in top_3:

            normalized_score = (
                score / highest_score
            ) * 100

            normalized_results.append(
                (crop, normalized_score)
            )

        return normalized_results