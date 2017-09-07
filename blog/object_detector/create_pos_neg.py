import re
import cv2
import os

DIR_PATH_FILE = '/home/minhdo/data_train_dog/list_dog.txt'
DIR_PATH = '/home/minhdo/data_train_dog/'
DIR_FOLDER = 'resize_dog4train'

reg_pattern = re.compile(r'[A-z0-9]+-[A-z0-9]+-[A-z0-9]+-[A-z0-9]+-[A-z0-9]+')

def create_pos():
    DIR_PATH_FILE = '/home/minhdo/data_train_dog/list_dog.txt'
    DIR_PATH = '/home/minhdo/data_train_dog/'
    DIR_FOLDER = 'resize_dog4train'
    with open(DIR_PATH_FILE, 'r') as f:
        data = f.readlines()

    data_remove = [i.replace('\n','') for i in data]

    for item in data_remove:
        image_name = re.sub('dog.','pos-',item)
        img = cv2.imread(DIR_PATH+item)
        image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        resize_image = cv2.resize(image_gray, (100,75))
        cv2.imwrite( os.path.join(DIR_PATH,DIR_FOLDER,image_name) , resize_image)

def create_neg():
    DIR_PATH_FILE = '/home/minhdo/data_train_neg/list_neg.txt'
    DIR_PATH = '/home/minhdo/data_train_neg/'
    DIR_FOLDER = 'resize_neg4train'
    with open(DIR_PATH_FILE, 'r') as f:
        data = f.readlines()

    data_remove = [i.replace('\n','') for i in data]

    count_index = 0
    for item in data_remove:
        image_name = re.sub(reg_pattern, 'neg-'+str(count_index), item)
        img = cv2.imread(DIR_PATH+item)
        image_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        resize_image = cv2.resize(image_gray, (47,92))
        cv2.imwrite( os.path.join(DIR_PATH,DIR_FOLDER,image_name) , resize_image)
        count_index += 1

if __name__ == '__main__':
    # print "create pos"
    # create_pos()
    print "create neg"
    create_neg()
