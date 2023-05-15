import cv2
import os
from open_cv.optical_flow import *

if __name__ == '__main__':
    path = os.getcwd()

    while (True):
        select_test = input("\nSelecione o tipo de teste"+"\n" +
                            "1 - Vídeo do diretório\n"+"2 - Webcam\n"+"Selecionar: ")
        if select_test == "1":
            files_videos = os.listdir(str(path)+"/videos")
            print("\nVídeo")
            for vd in range(0, len(files_videos)):
                print(vd+1, "- " + files_videos[vd])
            video_select = input("Selecionar vídeo: ")

            video_path = path+"/videos/"+files_videos[int(video_select)-1]
            while (True):
                select_method = input("Selecione o método do Optical Flow: ")
                if (select_method == "1"):
                    method1 = cv2.optflow.calcOpticalFlowSparseToDense
                    params = [None, 8, 128, 0.001, True, 500.0, 3]
                    video_optical_flow(video_path, method1,
                                       params, resize=True, fx=0.3, fy=0.3)
                elif (select_method == "2"):
                    method2 = cv2.calcOpticalFlowFarneback
                    params2 = [None, 0.3, 5, 10, 5, 11, 1.5, 0]
                    video_optical_flow(video_path, method2,
                                       params2, resize=True, fx=0.3, fy=0.3)
                else:
                    break

        elif select_test == "2":
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
        else:
            break

    """
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
    """
