import csv
import pyautogui
import mediapipe as mp
import numpy as np
import cv2

# Load configurations from the CSV file
def load_configurations(file_path):
    configurations = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract the landmarks from the lm_0 to lm_62 columns and store as a numpy array
            landmarks = np.array([float(row[f'lm_{i}']) for i in range(63)])
            configurations.append({
                'character': row['character'],
                'landmarks': landmarks
            })
    return configurations

# Compare the current hand landmarks with the saved configurations
def match_landmarks(current_landmarks, configurations, threshold=0.1):
    # Iterate through each configuration and compare landmarks
    for config in configurations:
        saved_landmarks = config['landmarks']

        # Compute the difference between the current and saved landmarks
        if np.linalg.norm(current_landmarks - saved_landmarks) < threshold:
            return config['character']
    return None

# Main function
def main():
    # Load configurations
    config_file = 'hand_characters.csv'
    configurations = load_configurations(config_file)

    # Mediapipe setup
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils

    # Start video capture
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Process the frame with Mediapipe
        results = hands.process(frame)

        matched_character = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract the landmarks as a flattened array
                landmarks = np.array(
                    [[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]
                ).flatten()

                # Match with the saved configurations
                matched_character = match_landmarks(landmarks, configurations)
                if matched_character:
                    pyautogui.press(matched_character)
                else:
                    pyautogui.press("a")

                # Draw hand landmarks on the frame
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the matched character on the frame
        if matched_character:
            cv2.putText(frame, f'Matched: {matched_character}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
