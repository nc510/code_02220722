import time

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,i*j),end=" ")
        time.sleep(0.2)
    print()