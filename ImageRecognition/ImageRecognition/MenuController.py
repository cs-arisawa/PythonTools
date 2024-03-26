from ImageRecognition.MenuModel import Model
from ImageRecognition.MenuView import View
from ImageRecognition.CSVCreater import create_csv

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)
    
    def process_data(self, dir_path_image1, dir_path_image2, sort_type):
        self.model.set_data(dir_path_image1, dir_path_image2, sort_type)
        
        create_csv(self.model)
