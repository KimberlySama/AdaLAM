import numpy as np
import cv2 as cv
import math
# file1 = open('Left_TP.txt', 'r') 
# count = 0
# while True: 
#     count += 1
  
#     # Get next line from file 
#     line = file1.readline() 
    
#     # if line is empty 
#     # end of file is reached 
#     if not line: 
#         break
#     print("Line{}: {}".format(count, line.strip())) 
# print("Lines number is: ", count-1)
  
# file1.close()

def read_data(file_path):
    f = open(file_path, 'r')
    data = []
    for line in f:
        data.append([float(coord) for coord in line.split(', ')])
    f.close()
    return np.array(data)

def find_ground_truth(a1, a2):
    t1 = read_data("Left_TP.txt")
    t2 = read_data("Right_TP.txt")

    F, mask = cv.findFundamentalMat(t1,t2,cv.FM_8POINT)
    print(F)
    print(len(t1), len(t2))
    # pts1 = t1[mask.ravel()==1]
    # pts2 = t2[mask.ravel()==1]
    # out1 = t1[mask.ravel()==0]
    # out2 = t2[mask.ravel()==0]

    # a1 = read_data("Adalam_matched_Left.txt")
    # a2 = read_data("Adalam_matched_Right.txt")

    count = 0
    true_pos = []
    false_pos = []
    # for (p1, p2) in zip(a1, a2):
    for i in range(len(a1)):
        p1 = np.reshape(np.append(a1[i], 1), (3,1))
        p2 = np.reshape(np.append(a2[i], 1), (3,1))

        # print(p1.T, p2.T)
        # l = F.dot(p1)
        # error = abs(p2.T.dot(l)/math.sqrt(l[1]**2+l[2]**2))
        # print(error)
        # if error < 1:
        #     count += 1
        # print(p2.T.dot(F.dot(p1)))
        if abs(p2.T.dot(F.dot(p1))) < 0.01:
            count += 1
            np.append(true_pos, i)
        else:
            np.append(false_pos, i)

    print(len(true_pos), "inliers out of", len(a1))
    print(len(false_pos), "inliers out of", len(a1))
    return true_pos, false_pos