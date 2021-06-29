import cv2
import numpy as np

# valor 0 utiliza camera webcam
camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

while True:
    conectado, imagem = camera.read()
    imagem_cinza      = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    placas_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(150, 150))

    corte_x, corte_y, corte_a, corte_l = 0
    for (x, y, l, a) in placas_detectadas:

        # define variáveis do corte com os valores do loop atual
        corte_x, corte_y = x, y
        corte_l, corte_a = l, a

        # desenha retangulo na imagem detectada
        cv2.rectangle(
            imagem,
            (x, y),      # ponto 1
            (x+l, y+a),  # ponto 2
            (255, 0, 0),   # cor
            5 )

        # se detectou imagem, salva
        if len(placas_detectadas) > 0:
            img_cortada = imagem[
                corte_y+5:corte_y+corte_a-5,
                corte_x+5:corte_x+corte_l-5]
            teste = cv2.imwrite('imagens\\deteccao.png', img_cortada)

    # janela com a imagem inteira da camera
    cv2.imshow("teste", imagem)

    # tecla 'q' finaliza execução
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera.release()
        cv2.destroyAllWindows()
        break