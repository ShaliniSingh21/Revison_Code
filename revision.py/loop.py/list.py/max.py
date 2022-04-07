numbers = [50, 40, 23, 70, 56, 12, 550, 10, 7]
max=0
i=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print(max)
        
# 
# 
num=[50,40,23,70,56,12,5,10,7]
i=0  
max1=0
max2=0
while i<len(num):

    if num[i]>max1:
        max1=num[i]
       
    elif max1>num[i] and max2<num[i]:
        max2=num[i]
        num[i]=max2
    i=i+1
print(max2)


n=[50,40,23,70,56,12,5,10,7]
i=0
max=0
smax=0
tmax=0
while i<len(n):
	if n[i]>max:
		max=n[i]
	j=0
	while j<len(n):
		if max>n[j] and smax<n[j]:
			smax=n[j]
	
		elif smax>n[j] and tmax<n[j]:
			tmax=n[j]
		j+=1
	i=i+1
print(tmax)


