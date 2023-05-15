import cv2
import time
import numpy as np


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


def webcam_acess():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()
        filter_frame = cv2.medianBlur(frame, 3)
        cv2.imshow('Camera', frame)
        cv2.imshow('Imagem filtrada', filter_frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def webcam_optical_flow(method, params=[], gray=True):

    cap = cv2.VideoCapture(0)

    ret, old_frame = cap.read()
    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255
    prevs_frame = old_frame
    if (gray):
        prevs_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    while True:
        cv2.imshow('Camera', old_frame)

        ret, new_frame = cap.read()
        next_frame = new_frame
        if gray:
            next_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

        flow = method(prevs_frame, next_frame, *params)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang*180/np.pi/2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow('Optical Flow', bgr)
        old_frame = new_frame
        prevs_frame = next_frame

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def video_optical_flow(video_path, method, params=[], gray=True, resize=True, fx=0.5, fy=0.5):
    cap = cv2.VideoCapture(video_path)
    # Read the first frame
    ret, old_frame = cap.read()

    if (resize):
        old_frame = cv2.resize(old_frame,  None, fx=fx, fy=fy)

    prevs_frame = old_frame

    if (gray):
        prevs_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255

    while (True):

        cv2.imshow('Video', old_frame)

        ret, new_frame = cap.read()

        if not ret:
            break
        if (resize):
            new_frame = cv2.resize(new_frame, None, fx=fx, fy=fy)
        next_frame = new_frame

        if gray:
            next_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

        flow = method(prevs_frame, next_frame, *params)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang*180/np.pi/2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow('Optical Flow', bgr)

        old_frame = new_frame
        prevs_frame = next_frame

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
