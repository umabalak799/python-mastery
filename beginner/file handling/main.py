f = open('myfile.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = (line.split(",")[0])
    m2 = (line.split(",")[1])
    m3 = (line.split(",")[2]) 
    print(f"Marks of the student{i} in English is : {m1}")
    print(f"Marks of the student{i} in Maths is : {m2}")
    print(f"Marks of the student{i} in Science is : {m3}")

    print(line)
        
    