import cv2

def snap_picture():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open video device")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame_in = cap.read()

    if not ret:
        raise Exception("Could not read frame")

    # DEBUG: Save the captured frame
    # cv2.imwrite('captured_image.jpg', frame)

    cap.release()
    cv2.destroyAllWindows()

    return frame_in


if __name__ == "__main__":
    frame = snap_picture()