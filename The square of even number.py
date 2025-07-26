num_list=input('Enter the list of numbers with comma:').split(',')
result=[]
for i in num_list:
    i=int(i)  # transform str to int
    if i%2==0:
        result.append(i**2)
print('Result=',result)