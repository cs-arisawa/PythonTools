import cv2 as cv

# imagePathの画像から特徴点を抽出します
def featureKeypoint(imagePath):
    print(imagePath)
    img = cv.imread(imagePath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    akaze = cv.AKAZE_create()
    kp = akaze.detect(gray)
    img_shift = cv.drawKeypoints(gray, kp, None, flags=4)