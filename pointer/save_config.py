import cv2
import csv
import time
import mediapipe as mp
import numpy as np

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

# Configuration
CHARACTERS = "1234567890"
CSV_FILE = "hand_characters.csv"
COUNTDOWN_SEC = 3
SAMPLE_DELAY = 1  # Seconds between samples


def get_landmarks(frame):
    """Extract normalized hand landmarks"""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        return [np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()
                for hand in results.multi_hand_landmarks]
    return None


def save_sample(character, landmarks):
    """Save to CSV with timestamp and character label"""
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        for hand in landmarks:
            writer.writerow([time.time(), character, *hand])


def capture_session():
    cap = cv2.VideoCapture(0)
    current_char = 0

    while cap.isOpened() and current_char < len(CHARACTERS):
        char = CHARACTERS[current_char]
        ret, frame = cap.read()
        if not ret:
            continue

        # Display instructions
        cv2.putText(frame, f"Show gesture for: {char}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, "Press SPACE to capture", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow('Character Capture', frame)

        key = cv2.waitKey(1)
        if key == 32:  # SPACE
            print(f"Capturing {char} in {COUNTDOWN_SEC} seconds...")
            time.sleep(COUNTDOWN_SEC)

            landmarks = get_landmarks(frame)
            if landmarks:
                save_sample(char, landmarks)
                print(f"Saved {len(landmarks)} hand samples for {char}")
                current_char += 1
            else:
                print("No hands detected!")

            time.sleep(SAMPLE_DELAY)

        elif key == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Initialize CSV with headers
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'character'] + [f'lm_{i}' for i in range(63)])  # 21 landmarks * 3 coordinates

    print(f"Starting capture session for characters: {CHARACTERS}")
    capture_session()
    print("Capture completed! Data saved to", CSV_FILE)