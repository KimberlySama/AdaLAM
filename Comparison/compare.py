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

k1 = read_data("Left_TP.txt")
k2 = read_data("Right_TP.txt")
f1 = read_data("Left_TN.txt")
f2 = read_data("Right_TN.txt")

F, mask = cv.findFundamentalMat(k1,k2,cv.FM_8POINT)
pts1 = k1[mask.ravel()==1]
pts2 = k2[mask.ravel()==1]
out1 = k1[mask.ravel()==0]
out2 = k2[mask.ravel()==0]

a1 = read_data("Adalam_matched_Left.txt")
a2 = read_data("Adalam_matched_Right.txt")
l = 0
count = 0
for (p1, p2) in zip(a1, a2):
    p1 = np.reshape(np.append(p1, 1), (3,1))
    p2 = np.reshape(np.append(p2, 1), (3,1))
    # print(p1.T, p2.T)
    l = F.dot(p1)
    error = abs(p2.T.dot(l)/math.sqrt(l[1]**2+l[2]**2))
    #print(p2.T.dot(l))
    # print(error)
    if error < 1:
        count += 1

# adalam = read_data("Adalam_matched.txt")
# true_pos = read_data("Left_TP.txt")
# true_neg = read_data("Left_TN.txt")
# threshold = 0.2
# n_tp = 0
# n_tn = 0



# for coord in adalam:
#     for tp_coord in true_pos:
#         np.linalg.norm(np.array(coord)-np.array(tp_coord))
#         if np.linalg.norm(np.array(coord)-np.array(tp_coord)) < threshold:
#             n_tp += 1
#             break
        
#     for tp_coord in true_neg:
#         np.linalg.norm(np.array(coord)-np.array(tp_coord))
#         if np.linalg.norm(np.array(coord)-np.array(tp_coord)) < threshold:
#             n_tn += 1
#             break