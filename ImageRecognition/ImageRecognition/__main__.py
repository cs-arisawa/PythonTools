import tkinter as tk
from ImageRecognition.MenuController import Controller

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()