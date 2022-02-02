'''
R E C U R S I O N
'''

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
    return product


#Binary search using recursion
#l: list  x:search key
def binary_search(l,x,start,end):
    #base case: 1 element
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        #dicide the array into halves
        mid = int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            #left half
            return binary_search(l,x,start,mid-1)
        else:
            #right half
            return binary_search(l,x,mid+1,end)
            

#To finf the nth Fibinacci number
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


n = int(input('Enter a non-negative number: '))
print('Fibonacci number at position',n,'is',fibonacci(n))

        
'''
l = [20,45,60,70,90]
x = int(input('Enter seach key: '))
index = binary_search(l,x,0,len(l)-1)
if index==-1:
    print(x,'not found')
else:
    print(x,'is found at position',index+1)
#iterative method

def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

n = int(input('Enter a non-negative number: '))
if n<0:
    print('Factorial is not defined on a negative number')
else:
    f = factorial(n)
    print('Factorial',n,'!',f)
'''
