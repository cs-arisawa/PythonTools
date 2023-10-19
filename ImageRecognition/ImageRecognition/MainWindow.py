import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk
import pathlib
from tkinterdnd2 import DND_FILES, TkinterDnD
from . import config
    
class MainWindow():
    def __init__(self):
        super().__init__()
        
        # ウィンドウの生成
        window = TkinterDnD.Tk()
        window.title("QRコード生成")
        
        # ウィンドウ設定
        # ウィンドウのサイズを指定
        windowWidth = config['mainwindow_width']
        windowHeight = config['mainwindow_height']
        windowsize = (str(windowWidth) + "x" + str(windowHeight))
        window.geometry(windowsize)  # 幅x高さの形式で指定
        
        window.mainloop()