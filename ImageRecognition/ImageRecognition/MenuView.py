import tkinter as tk
from tkinter import filedialog, font, ttk
from functools import partial
from . import config

class View():
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        
        # ディレクトリのパス表示用テキスト
        self.dir1_path = tk.StringVar()
        self.dir2_path = tk.StringVar()
        self.dic = {'Directory1': self.dir1_path, 'Directory2': self.dir2_path}
        
        # エラー表示用
        self.error_text = tk.StringVar()
        
        # テキスト一覧
        self.text_list = []
        
        # ソート方法
        self.sort_type = tk.StringVar()
        
         # メインウィンドウの生成
        windowWidth = config['mainwindow_width']
        windowheight = config['mainwindow_height']
        windowSize = str(windowWidth) + "x" + str(windowheight)
        self.root.geometry(windowSize)
        self.root.title('画像認識')
        
        # エラー表示用テキストボックスの作成
        self.error_label = tk.Label(self.root, textvariable=self.error_text)
        self.text_list.append(self.error_text)
        self.error_label.config(foreground="red")
        
        # ラベルのフォント設定
        labelFont = font.Font(family=config['labelfont_family'], size=config['labelfont_size'])
        
        # ボタン用Frame
        self.button_frame = tk.Frame(self.root)
        
        # imageファイルのソートの仕方を設定するcombobox作成
        self.sort_options = [config['sort_type'][0], config['sort_type'][1]]
        self.sort_combobox = ttk.Combobox(self.button_frame, textvariable=self.sort_type, values=self.sort_options, state="readonly")
        self.sort_combobox.set(self.sort_options[0])
        
        # directory1のボタンとテキストボックスの作成
        self.dir1_button = tk.Button(self.root, text='Directory1', font=labelFont)
        self.dir1_button.bind('<Button-1>', partial(self.select_folder, key='Directory1'))
        self.dir1_path_box = tk.Label(self.root, textvariable=self.dir1_path, background="white")
        self.text_list.append(self.dir1_path)
        
        # directory2のボタンとテキストボックスの作成
        self.dir2_button = tk.Button(self.root, text='Directory2', font=labelFont)
        self.dir2_button.bind('<Button-1>', partial(self.select_folder, key='Directory2'))
        self.dir2_path_box = tk.Label(self.root, textvariable=self.dir2_path, background="white")
        self.text_list.append(self.dir2_path)
        
        # 類似度計算ボタンの作成
        self.rec_button = tk.Button(self.button_frame, text='類似度計算', font=labelFont)
        self.rec_button.bind('<Button-1>', partial(self.click_rec_button))

        # クリアボタンの作成
        self.clear_button = tk.Button(self.button_frame, text="クリア", font=labelFont)
        self.clear_button.bind('<Button-1>', partial(self.click_clear_button))
        
        # 配置
        self.error_label.pack(anchor="w")
        self.dir1_button.pack(anchor="w", padx=10, pady=10)
        self.dir1_path_box.pack(anchor="w", fill="x", padx=10, pady=10) 
        self.dir2_button.pack(anchor="w", padx=10, pady=10)
        self.dir2_path_box.pack(anchor="w", fill="x", padx=10, pady=10) 
        
        self.sort_combobox.pack(side="left", padx=10, pady=10)
        self.rec_button.pack(side="left", padx=10, pady=10)
        self.clear_button.pack(side="left", padx=10, pady=10)
        
        self.button_frame.pack(anchor="w")
        
    def select_folder(self, event=None, key=None):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.dic[key].set(folder_path)
            
    def click_rec_button(self, event=None):
        flag = False
        error_str = ""
        for key, value in self.dic.items():
            if value.get() == "":
                error_str += str(key) + " "
                flag = True
        
        if flag:
            error_str += "を設定してください"
            self.error_text.set(error_str)
        else:
            self.error_text.set("")
            self.controller.process_data(self.dic["Directory1"].get(), self.dic["Directory2"].get(), self.sort_type.get())

    def click_clear_button(self, event=None):
        [string_var.set("") for string_var in self.text_list]    