import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def process_frame(image: cv2.Mat, character: str) -> dict:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    data = {"left": [], "right": []}

    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = handedness.classification[0].label

            landmark_array = []
            for landmark in hand_landmarks.landmark:
                landmark_array.extend([landmark.x, landmark.y, landmark.z])

            landmark_array.append(character)

            data["left" if hand_label == "Left" else "right"].append(landmark_array)

            # DEBUG: Draw the hand landmarks
            # mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        print("No hands detected.")

    return data
