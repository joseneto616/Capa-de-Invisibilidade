import cv2
import time
import numpy as np

#Captura da Webcam
cap = cv2.VideoCapture(0)

# Armazene um único quadro antes de iniciar o loop infinito
_, background = cap.read()
time.sleep(2)
_, background = cap.read()

while cap.isOpened():
    _, frame = cap.read()

    # Detectar o pano
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Intervalo de cor
    lower_bound = np.array([90, 50, 50])  # Azul escuro
    upper_bound = np.array([140, 255, 255])  # Azul escuro
    # Área da máscara
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Suavizar a máscara para reduzir ruídos
    mask = cv2.medianBlur(mask, 5)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Dilatar a máscara para preencher pequenos buracos
    mask = cv2.dilate(mask, None, iterations=2)

    # Erosão para remover ruídos isolados
    mask = cv2.erode(mask, None, iterations=2)

    # Aplique a máscara para obter apenas a região onde nosso pano está presente no quadro atual
    cloak = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    background_masked = cv2.bitwise_and(background, background, mask=mask)

    # Combine os quadros mascarados
    combined = cv2.add(cloak, background_masked)

    # Exibir o vídeo resultante
    cv2.imshow("Invisibility Cloak", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
