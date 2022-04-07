list=[23,5,15,6,84,25,8,3,7]
count=0
i=0
while i<len(list):
    if list[i]%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime no hai")     
else:
    print("composite no")     
