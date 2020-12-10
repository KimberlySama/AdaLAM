import numpy as np
import cv2 as cv
import math

def find_ground_truth(file_path):
    



def read_data(file_path):
    f = open(file_path, 'r')
    data = []
    for line in f:
        data.append([float(coord) for coord in line.split(', ')])
    f.close()
    return np.array(data)