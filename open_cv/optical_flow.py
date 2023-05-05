import cv2
import time


def optical_flow(method, video_path):

    start_time = time.time()

    cap = cv2.VideoCapture(video_path)

    # Read the first frame
    ret, old_frame = cap.read()

    while True:
        ret, new_frame = cap.read()

        if not ret:
            break

    end_time = time.time()

    print("Tempo total de execução: ", end_time-start_time, "segundos.")
