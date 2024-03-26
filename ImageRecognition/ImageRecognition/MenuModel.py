import os
from . import config

class Model():
    def __init__(self):
        self.__dir_path_image1 = ""
        self.__image1_file_paths = []
        self.__dir_path_image2 = ""
        self.__image2_file_paths = []
        self.__sort_type = ""
    
    def set_data(self, dir_path_image1, dir_path_image2, sort_type):
        self.__dir_path_image1 = dir_path_image1
        self.__image1_file_paths = self.get_files_paths(dir_path_image1)
        self.__dir_path_image2 = dir_path_image2
        self.__image2_file_paths = self.get_files_paths(dir_path_image2)
        self.__sort_type = sort_type
        
    def get_dir_path_image1(self):
        return self.__dir_path_image1
    
    def get_image1_file_paths(self):
        return self.__image1_file_paths
    
    def get_dir_path_image2(self):
        return self.__dir_path_image2
    
    def get_image2_file_paths(self):
        return self.__image2_file_paths
    
    def get_sort_type(self):
        return self.__sort_type
    
    def get_files_paths(self, dir_path):
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # 一般的な画像拡張子

        image_paths = []
        for file_name in os.listdir(dir_path):
            _, extension = os.path.splitext(file_name)

            if extension.lower() in image_extensions:
                image_paths.append(os.path.join(dir_path, file_name))
        
        if self.__sort_type == config['sort_type'][1]: # 更新日時順
            image_paths = sorted(image_paths, key=os.path.getmtime)

        return image_paths