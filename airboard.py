import asyncio
import base64
import json

import cv2
import mediapipe as mp
import numpy as np
# import tensorflow as tf
import dearpygui.dearpygui as dpg
import websockets
import threading


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# model_left = tf.keras.models.load_model('models/final_left.keras')
# model_right = tf.keras.models.load_model('models/final_right.keras')

async def video_stream(websocket):
        while True:
            in_ret, in_frame = cap.read()
            if not in_ret:
                print("WARNING: Failed to capture frame!")
                await websocket.send("FRAME_ERROR")
                continue

            _, buffer = cv2.imencode('.jpg', in_frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Process hand data
            image_rgb = cv2.cvtColor(in_frame, cv2.COLOR_BGR2RGB)
            results = mp_hands.Hands().process(image_rgb)
            hand_data = {"left": [], "right": []}
            if results.multi_hand_landmarks:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    hand_label = handedness.classification[0].label
                    landmarks = [(landmark.x, landmark.y, landmark.z) for landmark in hand_landmarks.landmark]
                    hand_data["left" if hand_label == "Left" else "right"].append(landmarks)

            # Send both video and hand data
            await websocket.send(json.dumps({"frame": jpg_as_text, "hand_data": hand_data}))
            await asyncio.sleep(1/10)

async def server_main():
    async with websockets.serve(video_stream, "localhost", 8765):
        await asyncio.Future()  # Run forever


def run_server():
    asyncio.run(server_main())

dpg.create_context()
dpg.create_viewport(title='AirBoard', width=1280, height=720)
dpg.setup_dearpygui()

print("Creating video capture object...")
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if not ret:
    print("Failed to capture frame.")
    exit(1)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
cap_fps = int(cap.get(5))

print(f"Frame width: {frame_width}, Frame height: {frame_height}, FPS: {cap_fps}")

frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
frame_rgba = frame_rgba.astype(np.float32) / 255.0
frame_rgba_flat = frame_rgba.flatten()

with dpg.texture_registry(show=False):
    dpg.add_raw_texture(width=frame_width, height=frame_height, default_value=frame_rgba_flat,
                        format=dpg.mvFormat_Float_rgba, tag="texture_tag")

with dpg.window(label="Webcam capture", width=720, height=480):
    dpg.add_text("AirBoard")
    dpg.add_image("texture_tag")
    dpg.set_item_width("texture_tag", 640)
    dpg.set_item_height("texture_tag", 360)

with dpg.window(label="Key presses", width=720, height=480, pos=(450, 125)):
    pass

dpg.show_metrics()
dpg.show_viewport()

server_thread = threading.Thread(target=run_server)
server_thread.start()

while dpg.is_dearpygui_running():
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    frame_rgba = frame_rgba.astype(np.float32) / 255.0
    frame_rgba_flat = frame_rgba.flatten()

    dpg.set_value("texture_tag", frame_rgba_flat)

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    single_data = {"left": [], "right": []}

    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            hand_label = handedness.classification[0].label

            landmark_array = []
            for landmark in hand_landmarks.landmark:
                landmark_array.extend([landmark.x, landmark.y, landmark.z])

            single_data["left" if hand_label == "Left" else "right"].append(landmark_array)
        print(single_data)
    else:
        print("No hands detected.")

    # Render the frame
    dpg.render_dearpygui_frame()

dpg.start_dearpygui()

cap.release()
cv2.destroyAllWindows()
dpg.destroy_context()
