import qrcode
from tkinter import PhotoImage

class QRCode(object):

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.qrcode = QRCode.generateQRCode(self.url, self.filename)
    
    @staticmethod
    def generateQRCode(url, filename):
        qr = qrcode.QRCode(
            version=1,  # QRコードのバージョン
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # 誤り訂正レベル
            box_size=10,  # ボックスのサイズ
            border=4,  # 枠の幅
            )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        imgPath = "png/" + filename
        img.save(imgPath)
        return PhotoImage(file=imgPath)