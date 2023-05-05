
from open_cv.optical_flow import *

if __name__ == '__main__':

    video_path = "videos/VID_20230407_154458.mp4"
    method1 = cv2.optflow.calcOpticalFlowSparseToDense

    # optical_flow(method, video_path)
    # webcam_acess()

    # params = [8, 128, 0.001, True, 500.0, 3]
    # webcam_optical_flow(method1, params)

    method2 = cv2.calcOpticalFlowFarneback
    params2 = [0.3, 5, 10, 5, 11, 1.5, 0]
    webcam_optical_flow(method2, params2)
