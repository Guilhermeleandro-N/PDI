import cv2
import numpy as np

def adjust_temperature(image, value):
    b, g, r = cv2.split(image)
    if value > 0:
        r = cv2.add(r, value)
        b = cv2.subtract(b, value)
    else:
        r = cv2.subtract(r, abs(value))
        b = cv2.add(b, abs(value))
    return cv2.merge((b, g, r))

def adjust_contrast(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

def enhance_whites(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    return cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)

def enhance_blacks(image, value):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.subtract(l, value)
    l = np.clip(l, 0, 255)
    return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)

# Teste de execução
if __name__ == "__main__":
    image = cv2.imread("Goku and Goten.png")
    
    image_restaured = adjust_temperature(image, -13)  # Aumenta a temperatura
    # cv2.imshow("temperatura", image_restaured)
    #image_restaured = adjust_contrast##(image_restaured, 1.1)  # Aumenta o contraste
    #cv2.imshow("contraste", image_restaured)

    image_restaured = enhance_whites(image_restaured, -25)  # Realce de brancos
    cv2.imshow("brancos", image_restaured)

    #image_restaured = enhance_blacks
    #(image_restaured, 15)  # Realce de pretos
    #cv2.imshow("pretos", image_restaured)
    #cv2.imshow("Original", image)


    # temp_image = adjust_temperature(image, 30)  # Aumenta a temperatura
    # contrast_image = adjust_contrast(image, 1.5)  # Aumenta o contraste
    # white_image = enhance_whites(image, 50)  # Realce de brancos
    # black_image = enhance_blacks(image, 50)  # Realce de pretos
    
    # cv2.imshow("Original", image)
    # cv2.imshow("Temperatura", temp_image)
    # cv2.imshow("Contraste", contrast_image)
    # cv2.imshow("Brancos", white_image)
    # cv2.imshow("Pretos", black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
