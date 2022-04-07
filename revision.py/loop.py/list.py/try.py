# from stringprep import in_table_c12


# a=int(input("enter"))
# i=0
# while i<=a:
#     b=(i)**2
#     print(b)  
#     i+=1     


list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
k=[]
sum=""
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=sum+list[i][j]
        j=j+1
    i=i+1    
k.append(sum)    
print(k)        
        

       