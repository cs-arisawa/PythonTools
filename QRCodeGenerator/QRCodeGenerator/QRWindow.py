import tkinter as tk
from QRCodeGenerator import config

def start(mainWindow, qr):
    
    # ウィンドウの生成
    window = tk.Toplevel(mainWindow)
    window.title(qr.filename)
    
    # ウィンドウ設定
    # ウィンドウのサイズを指定
    windowWidth = config['qrwindow_width']
    windowHeight = config['qrwindow_height']
    windowsize = (str(windowWidth) + "x" + str(windowHeight))
    window.geometry(windowsize)  # 幅x高さの形式で指定
    
    # QRコードイメージの設定
    windowAve = (windowWidth + windowHeight) / 2
    qrImageLabel = tk.Label(window, image=qr.qrcode)
    
    # 配置
    qrImageLabel.place(anchor=tk.CENTER, x=windowWidth/2, y=windowHeight/2, width=windowAve, height=windowAve)
    
    # ウインドウを生成
    window.mainloop()