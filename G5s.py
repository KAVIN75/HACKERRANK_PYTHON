# program 1
'''
reverse each space seperated strings
input:
hello hola bye adios
output:
olleh aloh eyb soida
'''
n=input().split() #hello hola bye adios -> ['hello','hola','bye','adios']
rev=[x[::-1] for x in n] #['olleh','aloh','eyb','soida']
print(' '.join(rev)) #olleh aloh eyb soida

#______________________________________________________________________________________

# program 2
'''
return addition of biggest numbers as a string
input:
23 565 1213 32
output:
1833
'''
n=list(map(int,input().split())) # 23 565 1213 32 -> [23,565,1213,32]
print(str(sum(n))) # 10(type of string)

#______________________________________________________________________________________

# program 3
'''
return 24 if 1,2 and 3 is in our input. else return the sum of the numbers.
input1:
1 2 3 4 5
output1:
24
input2:
10 20 30 40
output2:
100
'''
n=list(map(int,input().split()))
if  (x  in n and y in n and z in n):
    print("24")
else:
    print(sum(n))

#______________________________________________________________________________________

# progarm 4
'''
interchange the position of an array/list based on  last k values w.r.to n value i.e) start from (n-k)th position and rest.
input:
5 # n
3 # k
1 2 3 4 5
output: 
3 4 5 1 2
'''
n=int(input()) # 5
k=int(input()) # 3
x=list(map(str,input().split())) # ['1','2','3','4','5']
if(len(x)==n): # 5
    m=''.join(x) # 12345(joining w/o space for slicing the string whitespaces lead to wrong results)
    a=m[n-k:n]+m[0:n-k] # 34512
    for i in a:
        print(i,end=" ") # 3 4 5 1 2 (after the end of all loop)
        
#______________________________________________________________________________________

# program 5
'''
email id verification.
'''
    
    







