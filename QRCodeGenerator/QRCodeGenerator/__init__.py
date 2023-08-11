import os
import json

# config フォルダ内の config.json を読み込む
config_file_path = os.path.join(os.path.dirname(__file__), '../config', 'config.json')

with open(config_file_path) as jsonFile:
    config = json.load(jsonFile)