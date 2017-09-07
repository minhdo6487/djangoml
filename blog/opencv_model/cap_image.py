
import cv2
print(cv2.__version__)
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
from PIL import Image
def make_image():
    vidcap = cv2.VideoCapture("video.avi")

    print vidcap.read()
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print 'Read a new frame: ', success
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1



def make_video():
    image1 = Image.open("/home/minhdo/Downloads/New-GithubTest/out_image/frame0.jpg")
    image2 = Image.open("/home/minhdo/Downloads/New-GithubTest/out_image/frame1.jpg")
    height, width, layers =  np.array(image1).shape

    # Create the OpenCV VideoWriter
    video = cv2.VideoWriter("/home/minhdo/Downloads/New-GithubTest/out_image/demo3_4.avi", # Filename
                            -1, # Negative 1 denotes manual codec selection. You can make this automatic by defining the "fourcc codec" with "cv2.VideoWriter_fourcc"
                            10, # 10 frames per second is chosen as a demo, 30FPS and 60FPS is more typical for a YouTube video
                            (width,height) # The width and height come from the stats of image1
                            )

    # We'll have 30 frames be the animated transition from image1 to image2. At 10FPS, this is a whole 3 seconds
    for i in xrange(0,30):
        images1And2 = Image.blend(image1, image2, i/30.0)

        # Conversion from PIL to OpenCV from: http://blog.extramaster.net/2015/07/python-converting-from-pil-to-opencv-2.html
        video.write(cv2.cvtColor(np.array(images1And2), cv2.COLOR_RGB2BGR))
        video.release()

make_video()
