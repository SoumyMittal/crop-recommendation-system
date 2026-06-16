from models.crop import Crop
class Maize(Crop):
    def __init__(self):
        super().__init__("Maize")
    
    def crop_type(self):
        return "Cereal Crop"
