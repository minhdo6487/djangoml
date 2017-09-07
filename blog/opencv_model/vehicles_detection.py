# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2
import sys
import os
sys.path.append('/home/minhdo/code')
from blog.lib.Config import Config
# from config import *

class detect_car:
    @classmethod
    def in_video(cls):
        # capture frames from a video
        cap = cv2.VideoCapture('test_video.mp4')
        # img = cv2.imread('/home/minhdo/Desktop/car.jpg')
        # Trained XML classifiers describes some features of some object we want to detect
        car_cascade = cv2.CascadeClassifier('cars.xml')

        # loop runs if capturing has been initialized.
        while True:
            # reads frames from a video
            ret, frames = cap.read()
            # frames = img
            # convert to gray scale of each frames
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)


            # Detects cars of different sizes in the input image
            cars = car_cascade.detectMultiScale(gray, 1.1, 1)
            # cars = car_cascade.detectMultiScale(gray, 1.1, 13)

            # To draw a rectangle in each cars
            for (x,y,w,h) in cars:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)

            # Display frames in a window
            # cv2.imshow('video2', frames)
            cv2.imshow('video1', gray)
            # Wait for Esc key to stop
            if cv2.waitKey(33) == 27:
                break

        # De-allocate any associated memory usage
        cv2.destroyAllWindows()
        out.release()

    @classmethod
    def in_image(cls, image_url):
        imagge_dir = Config().get('output_file', 'ImageDir')
        imgage_file = Config().get('opencv','object_detect_file')
        car_cascade = cv2.CascadeClassifier('/home/minhdo/code/blog/opencv_model/cars.xml')
        im = cv2.imread(image_url)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x,y,w,h) in cars:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imwrite( os.path.join(imagge_dir, imgage_file), gray )
        detect_haar = os.path.join(imagge_dir, imgage_file)
        return detect_haar


