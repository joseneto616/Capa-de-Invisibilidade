import cv2
import time
import numpy as np

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture a background frame
_, background = cap.read()
time.sleep(2)
_, background = cap.read()

# Define the lower and upper bounds for the cloak color
lower_bound = np.array([50, 80, 50])
upper_bound = np.array([90, 255, 255])

# Initialize the kernel for noise removal
open_kernel = np.ones((5, 5), np.uint8)
close_kernel = np.ones((7, 7), np.uint8)
dilation_kernel = np.ones((10, 10), np.uint8)

# Process the video frames
while cap.isOpened():
    # Capture a new frame
    _, frame = cap.read()

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the cloak color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the background frame
    cloak = cv2.bitwise_and(background, background, mask=mask)

    # Combine the cloak and background frames
    combined = cv2.add(cloak, frame)

    # Remove noise from the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, open_kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, close_kernel)
    mask = cv2.dilate(mask, dilation_kernel)

    # Display the combined frame
    cv2.imshow("Cloak Detection", combined)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()