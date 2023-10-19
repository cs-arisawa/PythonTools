import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk
import pathlib
from tkinterdnd2 import DND_FILES, TkinterDnD
from . import config
    
class MainWindow(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        
        # 画像が表示されているかどうか管理するフラグ
        # 表示されている場合 -> True
        # 表示されていない場合 -> False
        self.flag = False
        
        # ウィンドウの生成
        self.title("画像認識")
        
        # ウィンドウ設定
        # ウィンドウのサイズを指定
        windowWidth = config['mainwindow_width']
        windowHeight = config['mainwindow_height']
        windowsize = (str(windowWidth) + "x" + str(windowHeight))
        self.geometry(windowsize)  # 幅x高さの形式で指定
        
        # 画像を表示するゾーンの設定
        self.labelFrame = tk.LabelFrame(self, width=400, height=400, text="画像をドラッグ&ドロップ", labelanchor="n")
        self.labelFrame.drop_target_register(DND_FILES)
        self.labelFrame.dnd_bind('<<Drop>>', self.funcDragAndDrop)
        self.labelFrame.pack()
    
    def funcDragAndDrop(self, event):
        # ファイル名にスペースがあると{$path}で返却される
        # 参考：https://juu7g.hatenablog.com/entry/Python/csv/viewer
        self.path = event.data
        # 画像を表示
        self.load_image_drog_and_drop()
    
    #画像表示
    def load_image_drog_and_drop(self):

        if self.flag:
            self.clear_image()

        file_path = self.path
        image = Image.open(open(file_path, 'rb'))
        # アスペクトを維持しながら、指定したサイズ以下に画像を縮小
        image.thumbnail((400, 400))
        photoImage = ImageTk.PhotoImage(image)
        # 画像を表示
        self.image_label = tk.Label(self.labelFrame, image=photoImage)
        self.image_label.image = photoImage
        self.image_label.pack()

        self.flag = True