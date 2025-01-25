import argparse
import csv
import sys
import time

import cv2
import logging

from imagetocsv import process_frame

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

DEFAULT_CHARACTERS = "a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_space_backspace"

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


def write_to_csv(data: dict):
    logging.debug(data)
    for hand in data["left"]:
        with open("left_hand.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(hand)
    for hand in data["right"]:
        with open("right_hand.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(hand)


def capture_character(character: str, countdown=3, repetitions=50) -> list:
    for i in range(repetitions):
        print(f"{character}: {i + 1}")
        for remaining in range(countdown, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(f"{remaining} seconds remaining.")
            sys.stdout.flush()
            time.sleep(1)
        print("\nCapturing frame...")
        frame = snap_picture()
        res = process_frame(frame, character)
        write_to_csv(res)


def cycle_characters(characters: str, countdown=3, repetitions=50):
    for character in characters:
        logging.warning(f"Changing the captured character to '{character}'")
        time.sleep(3)
        capture_character(character, countdown, repetitions)


if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser(
        description="Capture images of the key presses to train the model",
    )
    arg_parse.add_argument("--width", type=int, default=640, help="Width of the images taken")
    arg_parse.add_argument("--height", type=int, default=480, help="Height of the images taken")
    arg_parse.add_argument("--characters_to_cycle", type=str, default=DEFAULT_CHARACTERS, help="Characters to capture, separated by underscores")
    arg_parse.add_argument("--frames_per_character", type=int, default=50, help="Number of frames to repeat capture for each character")
    arg_parse.add_argument("--countdown", type=int, default=3, help="Number of seconds to wait before capturing the frame")
    arg_parse.add_argument("--debug", type=bool, default=False, help="Enable debug logging")
    args = arg_parse.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logging.debug(f"Arguments: {args}")

    logging.info("Opening video device")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    logging.debug("Video device opened")

    logging.info("Setting video device resolution")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    logging.debug(f"Video device resolution set to {args.width}x{args.height}")

    characters_to_cycle = args.characters_to_cycle.split("_")

    cycle_characters(characters_to_cycle, args.countdown, args.frames_per_character)

    cap.release()
    cv2.destroyAllWindows()

    # frame = snap_picture(args.width, args.height)
