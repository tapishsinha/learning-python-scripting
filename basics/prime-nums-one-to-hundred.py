print('Prime numbers from 1 to 100 are:')
count=0
for i in range(2,101):
    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count == 2:
        print(i)        
    count=0