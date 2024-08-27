with open('write.txt','w') as f:
    for i in range(10):
        f.write("hello world"+str(i)+'\n')
    f.close()