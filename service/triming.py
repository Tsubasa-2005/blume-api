import cv2
import numpy as np

def crop_to_non_bg(image_path, output_path):
    image = cv2.imread(image_path)
    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # バイナリ画像に変換（背景が白色と仮定）
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # 画像の幅と高さを取得
    height, width = binary.shape
    
    # 左から右へ走査して最初の黒色ピクセルのx座標を見つける
    crop_x_left = 0
    for x in range(width):
        if np.any(binary[:, x] < 255):
            crop_x_left = x
            break
    
    # 右から左へ走査して最初の黒色ピクセルのx座標を見つける
    crop_x_right = width
    for x in range(width-1, -1, -1):
        if np.any(binary[:, x] < 255):
            crop_x_right = x
            break
    
    # 上から下へ走査して最初の黒色ピクセルのy座標を見つける
    crop_y_top = 0
    for y in range(height):
        if np.any(binary[y, :] < 255):
            crop_y_top = y
            break
    
    # 下から上へ走査して最初の黒色ピクセルのy座標を見つける
    crop_y_bottom = height
    for y in range(height-1, -1, -1):
        if np.any(binary[y, :] < 255):
            crop_y_bottom = y
            break
    
    # 画像をトリミング
    cropped_image = image[crop_y_top:crop_y_bottom+1, crop_x_left:crop_x_right+1]

    cv2.imwrite(output_path, cropped_image)
    print(f'{output_path} を保存しました。')
