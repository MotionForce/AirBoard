import cv2

print("starting")

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise Exception("Could not open video device")

# Set video frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture a single frame
ret, frame = cap.read()

# Check if frame is captured
if not ret:
    raise Exception("Could not read frame")

# Save the captured image to a file
# cv2.imwrite('captured_image.jpg', frame)

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()