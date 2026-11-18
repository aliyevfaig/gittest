s=0
for i in range(1,10):
    if i%2==1:
        s+=1
        if i%3==0:
            s+=3
    else:
        s+=2
    s+=1
print(s)
