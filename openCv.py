import cv2
import numpy as np

# Load the image
image = cv2.imread(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use the HoughCircles function to detect circles
circles = cv2.HoughCircles(gray_blurred, 
                           cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=50, param2=30, minRadius=15, maxRadius=40)

# If some circles are detected, convert the (x, y) coordinates and radius to integers
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # Loop over the detected circles and draw them
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# Display the output image
cv2.imshow("Circle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
