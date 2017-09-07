
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Images binary classifier based on scikit-learn SVM classifier.
It uses the RGB color space as feature vector.
'''

from __future__ import division
from __future__ import print_function
from PIL import Image
from sklearn import cross_validation
from sklearn import grid_search
from sklearn import svm
from sklearn import metrics
from StringIO import StringIO
from urlparse import urlparse
import urllib2
import sys
import os, ast
import pickle
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

sys.path.append('/home/minhdo/code')

from blog.lib.Config import Config


def process_image_url(image_url):
    '''Given an image URL it returns its feature vector

    Args:
      image_url (str): url of the image to process.

    Returns:
      list of float: feature vector.

    Raises:
      Any exception raised by urllib2 requests.

      IOError: if the URL does not point to a valid file.
    '''
    parsed_url = urlparse(image_url)
    request = urllib2.Request(image_url)
    # set a User-Agent and Referer to work around servers that block a typical
    # user agents and hotlinking. Sorry, it's for science!
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux ' \
            'x86_64; rv:31.0) Gecko/20100101 Firefox/31.0')
    request.add_header('Referrer', parsed_url.netloc)
    # Wrap network data in StringIO so that it looks like a file
    net_data = StringIO(urllib2.build_opener().open(request).read())
    image = Image.open(net_data)
    return process_image(image)


def process_image(image, blocks=4):
    '''Given a PIL Image object it returns its feature vector.

    Args:
      image (PIL.Image): image to process.
      blocks (int, optional): number of block to subdivide the RGB space into.

    Returns:
      list of float: feature vector if successful. None if the image is not
      RGB.
    '''
    if not image.mode == 'RGB':
        return None
    feature = [0] * blocks * blocks * blocks
    pixel_count = 0
    for pixel in image.getdata():
        ridx = int(pixel[0]/(256/blocks))
        gidx = int(pixel[1]/(256/blocks))
        bidx = int(pixel[2]/(256/blocks))
        idx = ridx + gidx * blocks + bidx * blocks * blocks
        feature[idx] += 1
        pixel_count += 1
    return [x/pixel_count for x in feature]

def classification_image(file_pkl, file_label, image_url):
    data_classification = []

    clf = joblib.load(file_pkl)

    features = process_image_url(image_url)
    classifier = clf.best_estimator_
    classifier.probability = True

    with open(file_label, 'r') as f:
        data = f.readlines()

    model_labels = ast.literal_eval(data[0])


    for item in (classifier.predict_proba(features)).tolist():
        for i in range(0,len(item),1 ):
            # print ('accuracy: %20s, label: %20s' % (item[i], model_labels[i]['name'] ) )
            data_classification.append(
                    'accuracy: %20.3f - label: %20s,' % (item[i], model_labels[i]['item'] )
                )


    print ( classifier.predict(features) )
    print ( classifier.predict_proba(features) )
    print (  )
    return data_classification




# def main(file_pkl, image_url):
#     clf = joblib.load(file_pkl)

#     features = process_image_url(image_url)
#     classifier = clf.best_estimator_
#     classifier.probability = True

#     model_labels = [
#             {'name':'baseball'  , 'label':4},
#             {'name':'golf'      , 'label':3},
#             {'name':'basketball', 'label':2},
#             {'name':'football'  , 'label':1},
#             {'name':'swim'      , 'label':0},
#         ]

#     for item in (classifier.predict_proba(features)).tolist():
#         for i in range(0,len(item),1 ):
#             print ('accuracy: %20s, label: %20s' % (item[i], model_labels[i]['name'] ) )


#     print ( classifier.predict(features) )
#     print ( classifier.predict_proba(features) )
#     print (  )



# if __name__ == '__main__':
#     main(sys.argv[1], sys.argv[2])

