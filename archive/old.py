import csv
import cv2
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
left_hand_csv = "left_hand.csv"
right_hand_csv = "right_hand.csv"
# for one image
image_path = "test-image.jpg"
image = cv2.imread(image_path)
character="a"
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
    results = hands.process(image_rgb)
if results.multi_hand_landmarks:
    for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
        hand_label = handedness.classification[0].label
        landmark_array = []
        for landmark in hand_landmarks.landmark:
            landmark_array.extend([landmark.x, landmark.y, landmark.z])
        
        landmark_array.append(character)
        csv_file = left_hand_csv if hand_label == "Left" else right_hand_csv
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(landmark_array)
        print(f"{hand_label} hand data saved to {csv_file}.")
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
else:
    print("No hands detected.")
scale_percent = 20
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Hand Landmarks", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()