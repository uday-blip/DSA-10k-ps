# find the diagonal and antidiagonal from a nested array
nest=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal=[]
anti_diagonal=[]
for ele in range(0,len(nest),1):
    diagonal.append(nest[ele][ele])
    anti_diagonal.append(nest[ele][len(nest)-1-ele])
print(f'the diagonal is {diagonal}')
print(f'the anti_diagonal is {anti_diagonal}')
# find the largest array in a nested array
num=[
    [1,2,3],
    [4,5,6,7,8], 
    [9,11]
]
largest=[]
for l in range(0,len(num),1):
    if len(num[l])>len(largest):
        largest=num[l]
print(f'the largest sublist is {largest}')
#using list comprehension 
big=[large for large in sorted(num ,key=len)][-1]
print(big)    