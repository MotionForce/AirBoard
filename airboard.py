import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

model_left = tf.keras.models.load_model('models/final_left.keras')
model_right = tf.keras.models.load_model('models/final_right.keras')

cap = cv2.VideoCapture(0) 

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Press 'q' to quit.")

# Capture frames in a loop
while True:
    ret, frame = cap.read()  # Read a single frame
    if not ret:
        print("Failed to capture frame.")
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    data = {"left": [], "right": []}

    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = handedness.classification[0].label

            landmark_array = []
            for landmark in hand_landmarks.landmark:
                landmark_array.extend([landmark.x, landmark.y, landmark.z])

            data["left" if hand_label == "Left" else "right"].append(landmark_array)


    else:
        print("No hands detected.")

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close windows
cap.release()
cv2.destroyAllWindows()
