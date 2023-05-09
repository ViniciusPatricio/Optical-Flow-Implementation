import cv2
from open_cv.optical_flow import *

if __name__ == '__main__':

    video_path = "videos/VID_20230407_154458.mp4"

    while (True):

        select_method = input("Selecione o método do Optical Flow: ")

        if (select_method == "1"):
            method1 = cv2.optflow.calcOpticalFlowSparseToDense
            params = [None, 8, 128, 0.001, True, 500.0, 3]
            webcam_optical_flow(method1, params)
        elif (select_method == "2"):
            method2 = cv2.calcOpticalFlowFarneback
            params2 = [None, 0.3, 5, 10, 5, 11, 1.5, 0]
            webcam_optical_flow(method2, params2)
        elif (select_method == "3"):
            method3 = cv2.optflow.calcOpticalFlowSF
            params3 = [1, 1, 1]
            webcam_optical_flow(method3, params3)
        elif (select_method == "4"):
            method4 = cv2.optflow.calcOpticalFlowDenseRLOF
            rlof_param = cv2.optflow.RLOFOpticalFlowParameter_create()
            params4 = [None, rlof_param, cv2.optflow.INTERP_RIC]
            webcam_optical_flow(method4, params4, False)
        else:
            break
