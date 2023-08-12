import tkinter as tk
from tkinter import font
from .QRCode import QRCode
from . import QRWindow
from . import config

def clickGenerate(window, urlEntry, filenameEntry):
    url = urlEntry.get()
    filename = filenameEntry.get()
    print("url = " + url + ", filename = " + filename)
    qr = QRCode(url, filename)
    QRWindow.start(window, qr)
    
    
def start():
    # ウィンドウの生成
    window = tk.Tk()
    window.title("QRコード生成")
    
    # ウィンドウ設定
    # ウィンドウのサイズを指定
    windowWidth = config['mainwindow_width']
    windowHeight = config['mainwindow_height']
    windowsize = (str(windowWidth) + "x" + str(windowHeight))
    window.geometry(windowsize)  # 幅x高さの形式で指定
    
    # ラベルのフォント設定
    labelFont = font.Font(family=config['labelfont_family'], size=config['labelfont_size'])
    
    # URL
    urlLabel = tk.Label(window, text="url = ", font=labelFont)
    urlEntry = tk.Entry(window, width=30)
    
    # 生成するQRコードの名前
    filenameLabel = tk.Label(window, text="filename = ", font=labelFont)
    filenameEntry = tk.Entry(window, width=30)
    
    # QRコード生成ボタン
    generateButton = tk.Button(text="QRコード生成", command=lambda: clickGenerate(window, urlEntry, filenameEntry))
    
    # 配置
    urlLabel.place(x=40, y=30, width=120, height=40)
    urlEntry.place(x=160, y=30, width=400, height=40)
    
    filenameLabel.place(x=40, y=100, width=120, height=40)
    filenameEntry.place(x=160, y=100, width=400, height=40)
    
    generateButton.place(anchor=tk.N, x=windowWidth/2, y=170, width=120, height=40)
    
    # ウィンドウ表示
    window.mainloop()
