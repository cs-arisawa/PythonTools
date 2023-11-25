import tkinter as tk
from tkinter import filedialog, font
from . import FeatureKeypoint as fk
from functools import partial
from . import config
root = tk.Tk()

# ボタンとテキストボックスを関連付ける辞書
dir1_path = tk.StringVar()
dir2_path = tk.StringVar()
dic = {'Directory1': dir1_path, 'Directory2': dir2_path}

def select_folder(event=None, key=None):
    folder_path = filedialog.askdirectory()
    if folder_path:
        dic[key].set(folder_path)

def start():
    # メインウィンドウの生成
    windowWidth = config['mainwindow_width']
    windowheight = config['mainwindow_height']
    windowSize = str(windowWidth) + "x" + str(windowheight)
    root.geometry(windowSize)
    root.title('画像認識')

    # ラベルのフォント設定
    labelFont = font.Font(family=config['labelfont_family'], size=config['labelfont_size'])

    # directory1のボタンとテキストボックスの作成
    dir1_button = tk.Button(root, text='Directory1', font=labelFont)
    dir1_button.bind('<Button-1>', partial(select_folder, key='Directory1'))
    dir1_path_box = tk.Label(root, textvariable=dir1_path)

    # directory2のボタンとテキストボックスの作成
    dir2_button = tk.Button(root, text='Directory2', font=labelFont)
    dir2_button.bind('<Button-1>', partial(select_folder, key='Directory2'))
    dir2_path_box = tk.Label(root, textvariable=dir2_path)

    # 配置
    dir1_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    dir1_path_box.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    dir2_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    dir2_path_box.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    root.mainloop()