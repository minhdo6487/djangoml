import numpy as np
import cv2
import os, sys

sys.path.append('/home/minhdo/code')
sys.path.append('/home/minhdo/')
from blog.lib.Config import Config


class human_detect:
    # path_dir = Config().get('paths','opencv_data_dir')
    # path_face = Config().get('opencv', 'face_cascade')
    # path_eye = Config().get('opencv', 'eye_cascade')
    # path_dir_image = Config().get('output_file','ImageDir')
    # path_file_imagedetected = Config().get('opencv', 'image_detect_file')

    def __init__(self):
       path_dir = Config().get('paths','opencv_data_dir')
       path_face = Config().get('opencv', 'face_cascade')
       path_eye = Config().get('opencv', 'eye_cascade')
       path_dir_image = Config().get('output_file','ImageDir')
       path_file_imagedetected = Config().get('opencv', 'image_detect_file')

       self.detect_face = os.path.join(path_dir, path_face)
       self.detect_eyes = os.path.join(path_dir, path_eye)
       self.path_dir_image = path_dir_image
       self.full_dir_image = os.path.join(path_dir_image, path_file_imagedetected)
    # print (path_dir)
    # print (os.path.join(path_dir, path_eye))

    @classmethod
    def face_detect(cls, img_name):
        x, y, w, h = "", "", "", ""
        eye_cascade = cv2.CascadeClassifier(human_detect().detect_eyes)
        face_cascade = cv2.CascadeClassifier(human_detect().detect_face)

        img = cv2.imread( os.path.join(human_detect().path_dir_image, img_name) )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        count_point = 0
        store_box_face = []
        for (x,y,w,h) in faces:

            box_face = "point_" + str(count_point)
            store_box_face.append(
                {'box_face': box_face, 'value': [x, y, w, h]}
            )

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            count_point += 1
        if not store_box_face:
            flat_face = False
        else:
            flat_face = True

        print " list box contain face {} ".format( store_box_face )

        cv2.imwrite(human_detect().full_dir_image, img)
        urlLink = human_detect().full_dir_image
        return urlLink, store_box_face, flat_face

# if __name__ == "__main__":
#     urlLink = human_detect.face_detect('download.jpg')
#     print urlLink
