with open('./test.txt', 'r') as f:
    for line in range(1,100):
        if f.readline()=="":
            print("over")
            break
        else:
            print(f.readline())
            print(line)