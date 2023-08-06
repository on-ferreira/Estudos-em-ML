from PIL import Image
import numpy as np


def binarize_image_manual(image, threshold):
    # Converter a imagem para um array NumPy
    img_array = np.array(image)

    # Binarizar a imagem
    img_array[img_array < threshold] = 0
    img_array[img_array >= threshold] = 255

    # Criar uma nova imagem a partir do array binarizado
    binarized_image = Image.fromarray(img_array)

    return binarized_image


def grayscale_image_manual(image):
    # Obtém as dimensões da imagem
    width, height = image.size

    # Cria uma nova imagem vazia para armazenar o resultado em tons de cinza
    gray_image = Image.new('L', (width, height))

    # Percorre todos os pixels da imagem
    for x in range(width):
        for y in range(height):
            # Obtém o valor do pixel na posição (x, y)
            pixel = image.getpixel((x, y))

            # Calcula o valor médio dos componentes de cor RGB para obter o tom de cinza
            gray_value = sum(pixel) // 3

            # Define o pixel na imagem em tons de cinza
            gray_image.putpixel((x, y), gray_value)

    return gray_image


# Caminho da imagem
image_path = "rakan.jpg"

# Abrir a imagem original
original_image = Image.open(image_path)

# Exemplo de binarização com limiar 128
threshold = 128
binarized_image = binarize_image_manual(original_image, threshold)

# Exemplo de conversão para tons de cinza
gray_image = grayscale_image_manual(original_image)

# Salvar as imagens binarizada e em tons de cinza
binarized_image.save("binarized_rakan.jpg")
gray_image.save("gray_rakan.jpg")