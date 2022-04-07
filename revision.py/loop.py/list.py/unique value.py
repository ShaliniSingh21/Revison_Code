list = [1, 2, 2, 5, 8, 4, 4, 8]
l=[]
c=0
i=0
while i<len(list):
    if list[i] not in l:
        l.append(list[i])
        c=c+1
    i=i+1
print(c,l)        
        
        