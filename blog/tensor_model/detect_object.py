import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

#/home/minhdo/opencv/data/haarcascades
#face_cascade = cv2.CascadeClassifier('/root/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#eye_cascade = cv2.CascadeClassifier('/root/opencv/data/haarcascades/haarcascade_eye.xml')

#cap = cv2.VideoCapture(0)
#img = cv2.imread("download.jpg")

class human_detect:
    eye_cascade = cv2.CascadeClassifier('/root/opencv/data/haarcascades/haarcascade_eye.xml')
    face_cascade = cv2.CascadeClassifier('/root/opencv/data/haarcascades/haarcascade_frontalface_alt.xml')
    
    bike_cascade = cv2.CascadeClassifier('/code/blog/opencv_model/data/cascade.xml')
    #bike_cascade = cv2.CascadeClassifier('/code/blog/opencv_model/filter_model/cascade_bike.xml')

    #def __init__(self, detect_face, detect_eyes):
    #    self.detect_face = face_cascade
    #    self.detect_eyes = eye_cascade

    @classmethod
    def face_detect(cls, img_name):
        print img_name
        img = cv2.imread('/media/images/'+img_name)
        #resized_image = cv2.resize(img, (250, 200))
        #img = resized_image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = human_detect.face_cascade.detectMultiScale(gray, 1.3, 5)
        #gray, scaleFactor=1.3,
	#minNeighbors=10, minSize=(75, 75)
                
        # add this
        # image, reject levels level weights.

        bike_cascade  = human_detect.bike_cascade.detectMultiScale(gray, 1.01, 70, 70 )
    
        # add this
        #for (x,y,w,h) in bike_cascade:
        #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        #    font = cv2.FONT_HERSHEY_SIMPLEX
        #    cv2.putText(img,'Bicycle',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

        for (i, (x,y,w,h)) in enumerate(bike_cascade):
            cv2.rectangle(img,(x,y),(x+w,y+h),(225,225,0),2)
            cv2.putText(img, "Bicycle #{}".format(i + 1), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 225), 2)
        
        #for (x,y,w,h) in faces:
        #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #    roi_gray = gray[y:y+h, x:x+w]
        #    roi_color = img[y:y+h, x:x+w]

        #    eyes = human_detect.eye_cascade.detectMultiScale(roi_gray)
        #    for (ex,ey,ew,eh) in eyes:
        #        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #print "status: ok"
        cv2.imwrite('/media/images/obj_detected.jpeg',img)
        urlLink = "/media/images/obj_detected.jpeg"
        return urlLink

if __name__ == "__main__":
    urlLink = human_detect.face_detect('fix_test_pen_rxmMRFe.jpg')
    print urlLink
    #img = cv2.imread("download.jpg")
    #while 1:
        #ret, img = cap.read()
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #for (x,y,w,h) in faces:
    #    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #    roi_gray = gray[y:y+h, x:x+w]
    #    roi_color = img[y:y+h, x:x+w]

    #    eyes = eye_cascade.detectMultiScale(roi_gray)
    #    for (ex,ey,ew,eh) in eyes:
    #        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #print "status: ok"
    #cv2.imwrite('detect_face.png',img)
        #cv2.imshow('img',img)
        #k = cv2.waitKey(30) & 0xff
        #if k == 27:
        #    break

    #cap.release()
    #cv2.destroyAllWindows()
