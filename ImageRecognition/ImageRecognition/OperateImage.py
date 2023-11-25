import os
from PIL import Image

operate_images = []

class Images:

    def __init__(self, folder_path):
        self.image_paths = self.get_image_paths(folder_path)

    @staticmethod
    def get_image_paths(folder_path):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 一般的な画像拡張子

        image_paths = []
        for file_name in os.listdir(folder_path):
            _, extension = os.path.splitext(file_name)
            if extension.lower() in image_extensions:
                image_paths.append(os.path.join(folder_path, file_name))

        return image_paths
    
    def __str__(self):
        str = ""
        for image in self.image_paths:
            str += image + '\n'

        return str

def set_operate_image_by_folders(dic):
    for key, value in dic.items():
        operate_images.append(Images(value.get()))
    
def print_images():
    for image in operate_images:
        print(image)