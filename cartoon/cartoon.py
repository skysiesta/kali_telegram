import cv2
import numpy as np

# ПРИМЕР ОБРАБОТКИ ФОТОГРАФИЙ, ТЕСТОВЫЙ ВАРИАНТ
# ПОКА В РАЗРАБОТКЕ, НЕПРОС ДЛЯ ПОНИМАНИЯ, КОММЕНТОВ НЕМНОГО
def colorize(file):
    img = cv2.imread(file)

    # ОБРАБОТКА ФОТОГРАФИИ
    # ГЕОМЕТРИЯ, ОПРЕДЕЛЕНИЕ ЦВЕТОВ
    # 1) Edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 1)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # БЛЮР
    # 2) Color
    # color = cv2.bilateralFilter(img, d=4, sigmaColor=600,sigmaSpace=600)
    color = cv2.medianBlur(img,7)
    color = cv2.medianBlur(color,7)
    color = cv2.medianBlur(color,7)
    color = cv2.medianBlur(color,7)

    # 3) Cartoon
    color = cv2.bitwise_and(color, color, mask=edges)

    # cv2.imshow("Image", img)
    # cv2.imshow("Cartoon", cartoon)
    # cv2.imshow("color", color)
    # cv2.imshow("edges", edges)
    cv2.imwrite(file, color)
# colorize("tests/rus3.jpg")
