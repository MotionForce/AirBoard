import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import argparse
import csv
import math
import sys
import time
import cv2
import logging
import pyautogui as pag
import mediapipe as mp
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

DEFAULT_CHARACTERS = "a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_space_backspace"
# DEFAULT_CHARACTERS = "1_2_3_4_5_6_7_8_9_0"
TYPE_DELAY = 0.5
DEPTH_THRESHOLD = 0.035

last_activation_time = {
    "Right": 100,
    "Left": 100
}

config = {
    "resting": {
        5: [],
        6: [],
        8: [],
    },
    "standing": {
        5: [],
        6: [],
        8: [],
    },
    "pressing": {
        5: [],
        6: [],
        8: [],
    },
    "points": [

    ]
}

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def get_index_tip(image: cv2.Mat, hand_count: int = 1) -> list:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True, max_num_hands=hand_count, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    entry = []

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            index_tip = hand_landmarks.landmark[8]
            palm = hand_landmarks.landmark[0]
            entry.append([index_tip.x, index_tip.y, index_tip.z, palm.z,
                          0 if handedness.classification[0].label == "Left" else 1])
    else:
        print("No hands detected.")

    return entry


def get_landmarks(image: cv2.Mat, hand_count: int = 1) -> list:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True, max_num_hands=hand_count, min_detection_confidence=0.5) as hands:
        results = hands.process(np.array(image_rgb))

    if results.multi_hand_landmarks:
        return list(zip(results.multi_hand_landmarks, results.multi_handedness))
    else:
        print("No hands detected.")


def process_character(image: cv2.Mat, character: str) -> list:
    coords = get_index_tip(image)
    if not coords:  # Check if the list is empty
        logging.error("No hands detected. Skipping this frame.")
        return []  # Return an empty list or handle appropriately
    coords[0].append(character)  # Access the first element if it exists
    return coords[0]



def snap_picture() -> cv2.UMat:
    ret, frame_in = cap.read()

    if not ret:
        raise Exception("Could not read frame")

    # DEBUG: Save the captured frame
    cv2.imwrite('captured_image.jpg', frame_in)

    # DEBUG: Display the captured frame
    # cv2.imshow('frame', frame_in)
    # cv2.waitKey(0)

    return frame_in


def load_config(file: str) -> dict:
    config = {}
    config["points"] = []

    with open(file, mode="r") as file:
        reader = csv.reader(file)
        config["depth"] = next(reader)[0]
        for row in reader:
            config["points"].append(row)

    return config


def capture_character(character: str, countdown=3, repetitions=50, wait_time=5) -> list:
    for remaining in range(wait_time, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining} seconds remaining.")
        sys.stdout.flush()
        time.sleep(1)
    if wait_time == 0:
        time.sleep(0.1)
    for i in range(repetitions):
        print(f"{character}: {i + 1}")
        for remaining in range(countdown, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(f"{remaining} seconds remaining.")
            sys.stdout.flush()
            time.sleep(1)
        if countdown == 0:
            time.sleep(0.1)
        print("\nCapturing frame...")
        frame = snap_picture()
        res = process_character(frame, character)
        if not res:
            logging.warning("Skipping frame due to missing hand detection.")
            continue
        config["points"].append(res)



def cycle_characters(characters: str, countdown=3, repetitions=50, wait_time=5):
    for character in characters:
        logging.warning(f"Changing the captured character to '{character}'")
        capture_character(character, countdown, repetitions, wait_time)


def manual_capture(countdown=3, repetitions=1, wait_time=5):
    while True:
        character = input("Enter the character to capture (or 'exit' to exit): ")
        if character == "exit":
            break
        capture_character(character, countdown, repetitions, wait_time)


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser(
        description="Capture images of the key presses to create a config",
    )
    arg_parse.add_argument("--width", type=int, default=640, help="Width of the images taken")
    arg_parse.add_argument("--height", type=int, default=480, help="Height of the images taken")
    arg_parse.add_argument("--characters-to-cycle", type=str, default=DEFAULT_CHARACTERS,
                           help="Characters to capture, separated by underscores")
    arg_parse.add_argument("--countdown", type=int, default=0,
                           help="Number of seconds to wait before capturing the frame")
    arg_parse.add_argument("--debug", type=bool, default=False, help="Enable debug logging")
    arg_parse.add_argument("--manual", type=bool, default=False, help="Enable per frame manual character capture")
    arg_parse.add_argument("--pre-cycle-wait", type=int, default=5,
                           help="Number of seconds to wait before starting the character cycle")
    arg_parse.add_argument("--train", type=bool, default=False, help="Whether to start using AirBoard")
    args = arg_parse.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logging.debug(f"Arguments: {args}")

    logging.info("Opening video device")
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    logging.debug("Video device opened")

    logging.info("Setting video device resolution")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    logging.debug(f"Video device resolution set to {args.width}x{args.height}")

    if args.train:
        logging.warning("Place only one hand in the frame. Hide your other hand from the camera.")

        logging.info("Getting depth: place your hand in a resting position. Data will be captured in 3 seconds.")
        time.sleep(3)
        frame = snap_picture()
        data = get_landmarks(frame, hand_count=1)
        five = data[0][0].landmark[5].z
        six = data[0][0].landmark[6].z
        eight = data[0][0].landmark[8].z
        config["resting"][5] = five
        config["resting"][6] = six
        config["resting"][8] = eight
        logging.info(f"Resting depth: 5: {five}, 6: {six}, 8: {eight}")

        logging.info("Getting depth: place your hand in a standing position. Data will be captured in 3 seconds.")
        time.sleep(3)
        frame = snap_picture()
        data = get_landmarks(frame, hand_count=1)
        five = data[0][0].landmark[5].z
        six = data[0][0].landmark[6].z
        eight = data[0][0].landmark[8].z
        config["standing"][5] = five
        config["standing"][6] = six
        config["standing"][8] = eight
        logging.info(f"Standing depth: 5: {five}, 6: {six}, 8: {eight}")

        logging.info("Getting depth: place your hand in a pressing position. Data will be captured in 3 seconds.")
        time.sleep(3)
        frame = snap_picture()
        data = get_landmarks(frame, hand_count=1)
        five = data[0][0].landmark[5].z
        six = data[0][0].landmark[6].z
        eight = data[0][0].landmark[8].z
        config["pressing"][5] = five
        config["pressing"][6] = six
        config["pressing"][8] = eight
        logging.info(f"Pressing depth: 5: {five}, 6: {six}, 8: {eight}")

        logging.info("Starting character cycling")
        characters_to_cycle = args.characters_to_cycle.split("_")
        cycle_characters(characters_to_cycle, args.countdown, 1, args.pre_cycle_wait)

    logging.info("Starting AirBoard")
    while True:
        frame = snap_picture()
        data = get_landmarks(frame, hand_count=2)
        if not data:
            continue
        for hand_instance in data:

            print(hand_instance)

            if len(data) == 0:
                continue
            current_time = time.time()
            hand = hand_instance[1].classification[0].label

            time_since_last_activation = current_time - last_activation_time[hand]
            if time_since_last_activation < TYPE_DELAY:
                continue

            # Update the last activation time for the hand

            x = hand_instance[0].landmark[8].x
            y = hand_instance[0].landmark[8].y
            zeight = hand_instance[0].landmark[8].z
            zfive = hand_instance[0].landmark[5].z
            zsix = hand_instance[0].landmark[6].z

            flat_distance = 100000
            depth_distance = 100000
            depth_pos = ""
            for i in ["resting", "standing", "pressing"]:
                dist = abs(zfive - config[i][5]) + abs(zsix - config[i][6]) + abs(zeight - config[i][8])
                if dist < depth_distance:
                    depth_pos = i
                    depth_distance = dist
            if depth_pos == "pressing":
                character = 'none'
                for row in config["points"]:
                    distance = math.sqrt((x - float(row[0])) ** 2 + (y - float(row[1])) ** 2)
                    if distance < flat_distance:
                        flat_distance = distance
                        character = row[5]
                        last_activation_time[hand] = current_time
                pag.press(character)
            else:
                logging.info("Not pressing")

    cap.release()
    cv2.destroyAllWindows()