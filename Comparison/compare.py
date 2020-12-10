class Points:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


file1 = open('Left_TP.txt', 'r') 
count = 0

set_TP = set()
while True: 
    count += 1
  
    # Get next line from file 
    line = file1.readline().strip()
    line = line.replace(",", "")
    
    # pnt = Points(x,y)
    # print(splitLine)
    if line!="" :
        splitLine = line.split()
        pnt = Points()
        set_TP.add(pnt)

    if not line: 
        break
    # print("Line{}: {}".format(count, line.strip())) 
print("Lines number is: ", count-1)
print("set_TP size is: ", len(set_TP))


  
file1.close()