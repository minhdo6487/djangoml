from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

from ConfigParser import ConfigParser, NoOptionError, NoSectionError

import os, sys
from django.conf import settings
import tensorflow as tf
#from code.lib.Config import *
#from lib.Config import Config

sys.path.append('/home/minhdo/code')

from blog.lib.Config import Config

class rec_image:
    def __init__(self):
        # self.path = "Minh"
        self.path = Config().get('paths', 'retrain_dir')
        self.file_retrain_label = Config().get('tensor', 'retrain_label')
        self.file_retrain_graph = Config().get('tensor', 'retrain_graph')

    @classmethod
    def get_img(cls, img_name):
        #image_path = '/media/images/'
        #print settings.MEDIA_ROOT
        #print img_name
        images_path = settings.MEDIA_ROOT
        #print os.path.join(images_path, 'images', img_name)
        #image_full_path = image_path + '/' + img_name
        image_full_path = os.path.join(images_path, 'images', img_name)
        return image_full_path


    @classmethod
    def rec_img(cls, img_name):
        file_dir = rec_image().path
        file_label = rec_image().file_retrain_label
        file_graph = rec_image().file_retrain_graph

        print(file_label, file_graph)
        print(os.path.join(file_dir, file_label))

        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        # change this as you see fit
        #image_path = sys.argv[1]
        #image_path = '/media/images/'
        image_path = rec_image.get_img(img_name)

        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line
                   in tf.gfile.GFile(os.path.join(file_dir, file_label)) ]

        # Unpersists graph from file
        with tf.gfile.FastGFile(os.path.join(file_dir, file_graph), 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

            predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})

            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

            list_result = []
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                print('%s (score = %.5f)' % (human_string, score))
                list_result.append('%s (score = %.5f)' % (human_string, score))
        return list_result, [list_result, img_name]

# class hello:
#     @classmethod
#     def hello(cls):
#         print "hello"

if __name__ == '__main__':
    print (path)
