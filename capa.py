#Importe os pacotes necessários e inicialize a câmera
import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)


#Armazene um único quadro antes de iniciar o infinito
_,background = cap.read()
time.sleep(2)
_, background = cap.read()
while cap.isOpen():
    _, frame - cap.read()

#Detectar o pano
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_bound = np.array([50,80,50])
upper_bound = np.array([90, 255, 255])
mask = cv2.inRange (hsv, lower_bound, upper_bound)

#Aplique a máscara
#Apply th mask to take only  those region from the saved background
#Where our cloak is present in the current frame
cloak = cv2.bitwise_and(background, background, mask=mask)

#Combine os quadros mascarados
combined = cv2.add(cloak, current_background)

#Removendo ruídos desnecessários da máscara
open_kernel = np.ones((5,5),np.uint8)
close_kernel = np.ones((7,7), np.uint8)
dilation_kernel = np.ones((10,10), np.uint8)