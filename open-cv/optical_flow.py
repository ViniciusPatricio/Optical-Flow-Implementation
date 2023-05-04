import cv2


def optical_flow(method, video_path):
    cap = cv2.VideoCapture(video_path)
