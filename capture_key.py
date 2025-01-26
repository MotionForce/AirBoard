import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def get_index_tip(image: cv2.Mat, hand_count: int=1) -> list:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True, max_num_hands=hand_count, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    entry = []

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):

            index_tip = hand_landmarks.landmark[8]
            palm = hand_landmarks.landmark[0]
            entry.append([index_tip.x, index_tip.y, index_tip.z, palm.z, 0 if handedness.classification[0].label == "Left" else 1])
    else:
        print("No hands detected.")

    return entry

def process_character(image: cv2.Mat, character: str) -> list:
    coords = get_index_tip(image)[0]
    coords.append(character)
    return coords

    
