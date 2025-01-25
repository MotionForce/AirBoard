import argparse
import csv
import sys
import time

import cv2

from imagetocsv import process_frame


def snap_picture(width=640, height=480) -> cv2.UMat:
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
    print(data)
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
        capture_character(character, countdown, repetitions)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open video device")
    print("Video device opened")
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("--height", type=int, default=480)
    arg_parse.add_argument("--width", type=int, default=640)
    arg_parse.add_argument("--characters_to_cycle", type=str, default="abcdefghijklmnopqrstuvwxyz")
    arg_parse.add_argument("--frames_per_character", type=int, default=50)
    arg_parse.add_argument("--countdown", type=int, default=3)
    args = arg_parse.parse_args()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    cycle_characters(args.characters_to_cycle, args.countdown, args.frames_per_character)

    cap.release()
    cv2.destroyAllWindows()

    # frame = snap_picture(args.width, args.height)
