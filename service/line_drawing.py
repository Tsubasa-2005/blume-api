import cv2

def line_drawing_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("画像を読み込めませんでした。")
        exit()
    # 画像のコントラストを調整
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    # ガウシアンブラーを適用
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # エッジ検出で線画を生成
    edges = cv2.adaptiveThreshold(gray_blurred, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 7, 6)
    
    # 生成した画像を保存
    output_path = 'line_drawing_output.jpg'  # 出力画像のパスを指定
    cv2.imwrite(output_path, edges)
    print(f'{output_path} を保存しました。')
