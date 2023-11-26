import tkinter as tk
from tkinter import filedialog, font, ttk
from . import FeatureKeypoint as fk
from functools import partial
from . import config
from . import OperateImage as oi
root = tk.Tk()

# ボタンとテキストボックスを関連付ける辞書
dir1_path = tk.StringVar()
dir2_path = tk.StringVar()
dic = {'Directory1': dir1_path, 'Directory2': dir2_path}

# エラーメッセージ用
error_text = tk.StringVar()

# テキストのリスト
text_list = []

# コンボボックスの設定値
combo_var = tk.StringVar()

def select_folder(event=None, key=None):
    folder_path = filedialog.askdirectory()
    if folder_path:
        dic[key].set(folder_path)

def click_rec_button(event=None):
    global error_text
    flag = False
    error_str = ""
    for key, value in dic.items():
        if value.get() == "":
            error_str += str(key) + " "
            flag = True
    
    if flag:
        error_str += "を設定してください"
        error_text.set(error_str)
    else:
        error_text.set("")
        oi.set_operate_image_by_folders(dic, combo_var.get())
        oi.print_images()

def click_clear_button(event=None):
    [string_var.set("") for string_var in text_list]

    
def start():
    # メインウィンドウの生成
    windowWidth = config['mainwindow_width']
    windowheight = config['mainwindow_height']
    windowSize = str(windowWidth) + "x" + str(windowheight)
    root.geometry(windowSize)
    root.title('画像認識')

    # ラベルのフォント設定
    labelFont = font.Font(family=config['labelfont_family'], size=config['labelfont_size'])

    # エラー表示用テキストボックスの作成
    error_label = tk.Label(root, textvariable=error_text)
    text_list.append(error_text)
    error_label.config(foreground="red")

    # directory1のボタンとテキストボックスの作成
    dir1_button = tk.Button(root, text='Directory1', font=labelFont)
    dir1_button.bind('<Button-1>', partial(select_folder, key='Directory1'))
    dir1_path_box = tk.Label(root, textvariable=dir1_path, background="white")
    text_list.append(dir1_path)

    # directory2のボタンとテキストボックスの作成
    dir2_button = tk.Button(root, text='Directory2', font=labelFont)
    dir2_button.bind('<Button-1>', partial(select_folder, key='Directory2'))
    dir2_path_box = tk.Label(root, textvariable=dir2_path, background="white")
    text_list.append(dir2_path)

    # ボタン用Frame
    button_frame = tk.Frame(root)

    # imageファイルのソートの仕方を設定するcombobox作成
    sort_options = [config['sort_type'][0], config['sort_type'][1]]
    sort_combobox = ttk.Combobox(button_frame, textvariable=combo_var, values=sort_options, state="readonly")
    sort_combobox.set(sort_options[0])

    # 類似度計算ボタンの作成
    rec_button = tk.Button(button_frame, text='類似度計算', font=labelFont)
    rec_button.bind('<Button-1>', partial(click_rec_button))

    # クリアボタンの作成
    clear_button = tk.Button(button_frame, text="クリア", font=labelFont)
    clear_button.bind('<Button-1>', partial(click_clear_button))


    # 配置
    error_label.pack(anchor="w")
    dir1_button.pack(anchor="w", padx=10, pady=10)
    dir1_path_box.pack(anchor="w", fill="x", padx=10, pady=10)
    dir2_button.pack(anchor="w", padx=10, pady=10)
    dir2_path_box.pack(anchor="w", fill="x", padx=10, pady=10)

    sort_combobox.pack(side="left", padx=10, pady=10)
    rec_button.pack(side="left", padx=10, pady=10)
    clear_button.pack(side="left", padx=10, pady=10)
    button_frame.pack(anchor="w")

    root.mainloop()