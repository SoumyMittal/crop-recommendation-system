from models.crop import Crop
class Wheat(Crop):
    def __init__(self):
        super().__init__("Wheat")
    
    def crop_type(self):
        return "Winter Crop"