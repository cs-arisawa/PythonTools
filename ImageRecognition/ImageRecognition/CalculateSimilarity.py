import cv2
from skimage.metrics import structural_similarity as ssim

def calculate_histogram_similarity(image1, image2):
    # 画像をグレースケールで読み込む
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # ヒストグラムを計算
    hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

    # ヒストグラムの類似度を計算（0に近いほど類似度が高い）
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    return similarity

def calculate_ssim(image1, image2):
    # 画像を同じ寸法にリサイズ
    target_size = (min(image1.shape[1], image2.shape[1]), min(image1.shape[0], image2.shape[0]))
    resized_image1 = resize_image(image1, target_size)
    resized_image2 = resize_image(image2, target_size)

    # 画像をグレースケールに変換
    gray_image1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)

    # SSIMを計算
    ssim_index, _ = ssim(gray_image1, gray_image2, full=True)

    return ssim_index

def resize_image(image, target_size):
    return cv2.resize(image, target_size)