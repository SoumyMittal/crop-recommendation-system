class Soil:
    def __init__(self, nitrogen, phosphorus, potassium, ph):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.ph = ph
    
    def show_soil_data(self):
        print("Soil Data")
        print(f"Nitrogen: {self.nitrogen}")
        print(f"Phosphorus: {self.phosphorus}")
        print(f"Potassium: {self.potassium}")
        print(f"pH: {self.ph}")
