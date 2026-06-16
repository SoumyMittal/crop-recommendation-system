from models.crop import Crop
class Rice(Crop):
    def __init__(self):
        super().__init__("Rice")
    
    def crop_type(self):
        return "Water Intensive Crop"
