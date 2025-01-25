import argparse
import sys
import time

import cv2

def snap_picture(width=640, height=480) -> cv2.UMat:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open video device")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame_in = cap.read()

    if not ret:
        raise Exception("Could not read frame")

    # DEBUG: Save the captured frame
    # cv2.imwrite('captured_image.jpg', frame_in)

    # DEBUG: Display the captured frame
    # cv2.imshow('frame', frame_in)
    # cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()

    return frame_in


def capture_character(character: str, countdown=3, repetitions=50) -> list:
    for i in range(repetitions):
        print(f"{character}: {i+1}")
        for remaining in range(countdown, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write(f"{remaining} seconds remaining.")
            sys.stdout.flush()
            time.sleep(1)
        print("\nCapturing frame...")
        frame = snap_picture()
        # TODO: Analyze the frame using MediaPipe

def cycle_characters(characters: str, countdown=3, repetitions=50):
    for character in characters:
        capture_character(character, countdown, repetitions)

if __name__ == "__main__":
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("--height", type=int, default=480)
    arg_parse.add_argument("--width", type=int, default=640)
    arg_parse.add_argument("--characters_to_cycle", type=str, default="abcdefghijklmnopqrstuvwxyz")
    arg_parse.add_argument("--frames_per_character", type=int, default=50)
    arg_parse.add_argument("--countdown", type=int, default=3)
    args = arg_parse.parse_args()

    cycle_characters(args.characters_to_cycle, args.countdown, args.frames_per_character)

    # frame = snap_picture(args.width, args.height)

