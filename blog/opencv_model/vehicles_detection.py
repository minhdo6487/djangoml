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
        cap = cv2.VideoCapture('/home/minhdo/code/blog/opencv_model/video/test_coca.mp4')
        # img = cv2.imread('/home/minhdo/code/blog/opencv_model/test_coca/coca_01_res.jpg')
        # Trained XML classifiers describes some features of some object we want to detect
        car_cascade = cv2.CascadeClassifier('/home/minhdo/code/blog/opencv_model/filter_model/cascade_coca.xml')

        # loop runs if capturing has been initialized.
        count_index = 0
        while True:
            # reads frames from a video
            ret, frames = cap.read()
            # frames = img
            # convert to gray scale of each frames
            # gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)


            # Detects cars of different sizes in the input image
            cars = car_cascade.detectMultiScale(frames, 1.1, 10)
            # cars = car_cascade.detectMultiScale(gray, 1.1, 13)

            # To draw a rectangle in each cars
            for (x,y,w,h) in cars:
                print (x,y,w,h)
                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
                ### roi an image ###
                ### start ###
                """
                @ try cut frame
                @ with x,y,w,h
                """
                roi = frames[y:y+h, x:x+w]

                ### end ###
                ### roi an image ###

            # Display frames in a window
            # cv2.imshow('video2', frames)
            cv2.imshow('video1', frames)
            # cv2.imshow('video2', roi)
            # Wait for Esc key to stop
            cv2.imwrite("/home/minhdo/code/blog/opencv_model/image_from_video/"+str(count_index)+".jpeg", frames )
            if cv2.waitKey(33) == 27:
                break
                
            count_index += 1

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

if __name__ == "__main__":
    detect_car.in_video()
