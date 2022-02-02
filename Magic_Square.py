'''
Created on TUES Oct 10 14:14:27
@author: eesha.kavuri
'''

'''
1. 1 is located at position (n/2,n-1)
2. position of 1 is (n/2,n-1)=(p,q) next number at (p-1,q+1)
3. calculated position already exists, (p+1,q-2) increment row by one, decrement colomn by 2
4. row position becomes -1 and colomn becomes n then (0,n-2)
'''

def magic_square(n):
    magicSquare = [[0 for i in range(n)] for j in range(n)]
    i, j = n//2, n-1
    num = n*n
    count = 1
    while(count<=num):
        if i==-1 and j==n:
            j = n-2
            i = 0
        else:
            if j == n:
                j = 0
            if i<0:
                i = n-1
        if magicSquare[i][j]!=0:
            j -= 2
            i += 1
            continue
        else:
            magicSquare[i][j] = count
            count+=1
        i -= 1
        j += 1
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=' ')
        print()
    print('The sum of row/colomn/diagonal is: ' + str(n*(n**2+1)/2))
magic_square(3)
