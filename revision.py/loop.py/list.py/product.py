list = [6,1,3,5,6,3,1]
l=[]
i=0
while i<len(list):
    if list[i]  not in l:
        l.append(list[i])
        product=l*i
    i=i+1
print(product)        



