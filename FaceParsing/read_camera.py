import cv2
import time
from inference import Inference

def read_camera():
    camera_number = 0  # 0: 笔记本自带， 1是USB外接, 台式机外接用0
    cap = cv2.VideoCapture(camera_number)
    if not cap.isOpened():  # 判断视频流是否打开
        print('Failed to read camera')
        exit()
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # 视频的平均帧率
    predictor = Inference()
    start_time = time.time()
    count = 0  # 帧数计数
    while True:
        flag, frame = cap.read()
        if not flag:
            print('Failed to read frame')
            cap.release()
            break
        count += 1
        cv2.putText(frame, "FPS: {0}".format(float('%.1f' % (count / (time.time() - start_time)))), (20, 20),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

        cv2.imshow('window', frame)  # 可以通过resize frame的大小，达到修改窗口大小的效果
        key = cv2.waitKey(1)  # 检测按键时间，如果按键，返回键值ASCII否则返回-1。如果参数为0，直到按键才继续，
        if key == ord('q'):
            predictor.inference(frame)
            cap.release()
            break
    cv2.destroyAllWindows()
read_camera()