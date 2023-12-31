import os
import cv2
from PIL import Image
from . import config
from . import CalculateSimilarity as cs

operate_images = []

class Images:
    def __init__(self, folder_path, sort_type):
        self.image_paths = self.get_image_paths(folder_path, sort_type)

    @staticmethod
    def get_image_paths(folder_path, sort_type):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 一般的な画像拡張子

        image_paths = []
        for file_name in os.listdir(folder_path):
            _, extension = os.path.splitext(file_name)
            if extension.lower() in image_extensions:
                image_paths.append(os.path.join(folder_path, file_name))
        
        if sort_type == config['sort_type'][1]: # 更新日時順
            image_paths = sorted(image_paths, key=os.path.getmtime)

        return image_paths
    
    def __str__(self):
        str = ""
        for image in self.image_paths:
            str += image + '\n'

        return str

def set_operate_image_by_folders(dic, sort):
    for key, value in dic.items():
        operate_images.append(Images(value.get(), sort))
    
def print_images():
    for image in operate_images:
        print(image)

def calculate_similarity():
    for i1, i2 in zip(operate_images[0].image_paths, operate_images[1].image_paths):
        image1 = cv2.imread(i1)
        image2 = cv2.imread(i2)
        print("hist:" + str(cs.calculate_histogram_similarity(image1, image2)))
        print("ssim:" + str(cs.calculate_ssim(image1, image2)))