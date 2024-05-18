import cv2
import time
import numpy as np

# Load the video and background images
video = cv2.VideoCapture(0)
background = cv2.imread("background.jpg")

# Get the width and height of the video
width = int(video.get(3))
height = int(video.get(4))

# Define the range of green color in HSV
lower_green = np.array([55, 50, 50])
upper_green = np.array([95, 255, 255])

while True:
    # Read a frame from the video
    ret, frame = video.read()

    # If the frame was not read successfully, break the loop
    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND the mask and the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Get the background image with the same width and height as the frame
    background_resized = cv2.resize(background, (width, height))

    # Create a final image by adding the background and the result
    final = cv2.add(background_resized, result)

    # Display the final image
    cv2.imshow("Final", final)

    # Wait for a key press and exit if the key is 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
video.release()
cv2.destroyAllWindows()