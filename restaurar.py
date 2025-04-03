import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# Teste de execução
if __name__ == "__main__":
    image = cv2.imread("imagens/Syn Shenron.png")


    image_restaured = adjust_temperature(image, -10)
    image_restaured = adjust_contrast(image_restaured, 1.1)
    image_restaured = enhance_whites(image_restaured, 5)

    # Converter para RGB para exibição correta no Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_restaured_rgb = cv2.cvtColor(image_restaured, cv2.COLOR_BGR2RGB)
    #Salvar Imagem restaurada
    cv2.imwrite("imagens_restauradas/Syn Shenron_restaurada.png", cv2.cvtColor(image_restaured_rgb, cv2.COLOR_RGB2BGR))
    # Criar figura para exibição com Matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(image_rgb)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(image_restaured_rgb)
    axes[1].set_title("Processada")
    axes[1].axis("off")

    plt.savefig("comparativo/Syn Shenron.png", dpi=300, bbox_inches="tight")

    plt.show()
