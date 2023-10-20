import tkinter as tk
from tkinter import font, Canvas
from PIL import Image, ImageTk
import pathlib
from tkinterdnd2 import DND_FILES, TkinterDnD
from . import config
from . import FeatureKeypoint as fk

def drop(event):
    global display_image, canvas
    canvas.delete("image")
    img = Image.open(event.data)
    display_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image = display_image, anchor = "nw")
    return event.action

def start():
    # メインウィンドウの生成
    display_image = None
    root = TkinterDnD.Tk()
    
    windowWidth = root.winfo_screenwidth()
    windowheight = root.winfo_screenheight()
    windowSize = str(windowWidth) + "x" + str(windowheight)
    root.geometry(windowSize)
    root.title('画像認識')
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)
    
    
    # Canvasウィジェットの生成
    global canvas
    canvas = Canvas(root, width=640, height=480, )
    # ウィジェットの配置
    canvas.pack()

    root.mainloop()