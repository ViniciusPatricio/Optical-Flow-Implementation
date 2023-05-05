
from open_cv.optical_flow import optical_flow

if __name__ == '__main__':
    print("Hello-World")

    video_path = "videos/VID_20230407_154458.mp4"
    method = " "
    optical_flow(method, video_path)
