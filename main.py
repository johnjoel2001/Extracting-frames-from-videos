# read video and extract frames

import cv2
def framecapture(path):
    vid=cv2.VideoCapture(path)
    count=0
    success=1
    while success:
        success,image=vid.read()
        cv2.imwrite("frame%d.jpg" % count,image)
        count+=1
if __name__ == '__main__':
    framecapture("C:\\Users\\John Joel\\PycharmProjects\\frames from videos\\nature.mp4")