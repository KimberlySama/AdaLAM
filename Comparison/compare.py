file1 = open('Left_TP.txt', 'r') 
count = 0
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline() 
    
    # if line is empty 
    # end of file is reached 
    if not line: 
        break
    print("Line{}: {}".format(count, line.strip())) 
print("Lines number is: ", count-1)
  
file1.close()