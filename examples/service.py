import example
import cv2 as cv
from PIL import Image
import glob
import mytest
import test


if __name__ == '__main__':

    # now this service script is calling mytest.py:
    mytest.main(["-x","7","-y","6"]) 

    # now this service script is calling test.py:
    test.main(["im1.jpg", "im2.jpg"])
