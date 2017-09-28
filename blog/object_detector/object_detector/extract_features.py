# Import the functions to calculate feature descriptors
from skimage.feature import local_binary_pattern
from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
# To read file names
import argparse as ap
import glob
import os
from config import *
import cv2



if __name__ == "__main__":
    # Argument Parser
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--pospath", help="Path to positive images",
            required=True)
    parser.add_argument('-n', "--negpath", help="Path to negative images",
            required=True)
    parser.add_argument('-d', "--descriptor", help="Descriptor to be used -- HOG",
            default="HOG")
    args = vars(parser.parse_args())

    pos_im_path = args["pospath"]
    neg_im_path = args["negpath"]

    des_type = args["descriptor"]

    print des_type

    # If feature directories don't exist, create them
    if not os.path.isdir(pos_feat_ph):
        os.makedirs(pos_feat_ph)

    # If feature directories don't exist, create them
    if not os.path.isdir(neg_feat_ph):
        os.makedirs(neg_feat_ph)

    print "Calculating the descriptors for the positive samples and saving them"
    for im_path in glob.glob(os.path.join(pos_im_path, "*")):
        # im = imread(im_path, as_grey=True)
        im = imread(im_path, as_grey=True)
        #im = cv2.resize(im, (100,40), interpolation=cv2.INTER_CUBIC)

        if des_type == "HOG":
           #fd =     hog(im, orientations=8, pixels_per_cell=(16, 16),
                    #cells_per_block=(1, 1), visualise=True)
           #fd, hog_image = hog(im, orientations=9, pixels_per_cell=(8, 8),
           #         cells_per_block=(3, 3), visualise=True)
           #fd          = hog(im, orientations, pixels_per_cell, cells_per_block, visualize, normalize)
           fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualise=None, block_norm='L1')
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(pos_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
        print "feature pos: {}, shape {}".format(fd, fd.shape )
    print "Positive features saved in {}".format(pos_feat_ph)

    print "Calculating the descriptors for the negative samples and saving them"
    for im_path in glob.glob(os.path.join(neg_im_path, "*")):
        im = imread(im_path, as_grey=True)
        #im = cv2.resize(im, (100,40), interpolation=cv2.INTER_CUBIC)
        # winSize = (20,20)
        # blockSize = (8,8)
        # blockStride = (4,4)
        # cellSize = (8,8)
        # nbins = 9
        # derivAperture = 1
        # winSigma = -1.
        # histogramNormType = 0
        # L2HysThreshold = 0.2
        # gammaCorrection = 1
        # nlevels = 64
        # signedGradient = True

        #hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradient)

        if des_type == "HOG":
            #fd =     hog(im, orientations=8, pixels_per_cell=(16, 16),
                    #cells_per_block=(1, 1), visualise=True)
            #fd, hog_image = hog(im, orientations=9, pixels_per_cell=(8, 8),
            #        cells_per_block=(3, 3), visualise=True)
            #fd,hogimage = hog(im, orientations, pixels_per_cell, cells_per_block, visualize)
            #fd = hog(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradient)
            fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualise=None, block_norm='L1')
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(neg_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
    print "Negative features saved in {}".format(neg_feat_ph)

    print "Completed calculating features from training images"
