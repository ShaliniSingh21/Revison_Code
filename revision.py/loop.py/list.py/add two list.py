# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# i=0
# list=[]
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         if list1[i] not in list2[j]:
#             list.append(list1[i])
#             # list.append(list2[j])  
#         j=i+1
#     i=i+1    
# print(list)    

# a=[1,2,3,4]
# b=[7,2,9,3]
# i=0
# l=[]
# while i<len(a):
# 	l.append (a[i])
# 	l.append(b[i])
# 	i=i+1
# print(l)


num=int(input('enter the number'))
i=1
while i<=10:
  product=num*i
  print(num,'x',i,'=', product)
  i=i+1