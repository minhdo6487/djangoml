
'''
Set the config variable.
'''

import ConfigParser as cp
import json, sys
sys.path.append('/home/minhdo/code')

from blog.lib.Config import Config

# config = cp.RawConfigParser()
# config.read('../data/config/config.cfg')
# config.read('/home/minhdo/code/blog/object-detector/data/config/config.cfg')

min_wdw_sz = json.loads(Config().get("hog","min_wdw_sz"))
step_size = json.loads(Config().get("hog", "step_size"))
orientations = Config().getint("hog", "orientations")
pixels_per_cell = json.loads(Config().get("hog", "pixels_per_cell"))
cells_per_block = json.loads(Config().get("hog", "cells_per_block"))
visualize = Config().getboolean("hog", "visualize")
normalize = Config().getboolean("hog", "normalize")
pos_feat_ph = Config().get("paths", "pos_feat_ph")
neg_feat_ph = Config().get("paths", "neg_feat_ph")
model_path = Config().get("paths", "model_path")
threshold = Config().get("nms", "threshold")


