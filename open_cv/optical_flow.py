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

def webcam_acess():
    cap = cv2.VideoCapture(0)

    while True:
    
        ret, frame = cap.read()
        
        cv2.imshow('Camera', frame)


        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()