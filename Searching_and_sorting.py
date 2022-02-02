def bubble_sort(a):
    #a : array
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

def linear_sort(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    flag = 0
    for i in element:
        if i==x:
            print('Yes! I foung my number at position:'+str(i))
            flag = 1
    if flag==0:
        print('Number is not found!')

def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    #flag=0 mean that the element has not be found yet
    flag = 0
    count = 0
    while first_pos<=last_pos and flag==0:
        count+=1
        mid = (first_pos+last_pos)//2
        if x==a[mid]:
            flag=1
            print('Element is present at position: '+str(mid))
            print('The number of iterations are: '+str(count))
            return
        else:
            if x<a[mid]:
                last_pos = mid-1
            else:
                first_pos = mid+1
    print('The number is not present!')
