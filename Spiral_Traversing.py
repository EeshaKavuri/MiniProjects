import turtle
from random import randint 
turtle.bgcolor('black')
seurat = turtle.Turtle()

dot_distance = 25
seurat.penup() 
list_color=['white','yellow','brown','red','blue','green','orange','pink','violet','grey']
seurat.setpos(-250,250)

def spiral(m,n):
    k,l,f=0,0,0
    seurat.color('white')
    """
    k=index of starting row
    m=ending row index
    l=index of starting colomn
    n=ending colomn index
    i=iterator
    """
    col = randint(0,9)
    seurat.color(list_color[col])
    while k<m and l<n:
        col = randint(0,9)
        seurat.color(list_color[col])
        if f==1:
            seurat.right(90)
        #Printing the first row from the remaining rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i],end=' ')
        k+=1
        f=1
        seurat.right(90)
        col = randint(0,9)
        seurat.color(list_color[col])
        
        #printing the last colomn from the remaning colomn
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=' ')
        n-=1
        seurat.right(90)
        col = randint(0,9)
        seurat.color(list_color[col])

        if k<m:
            #printing the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=' ')
            m-=1
        seurat.right(90)
        col = randint(0,9)
        seurat.color(list_color[col])
        if l<n:
            #printing the first colomn from the remaining colomns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=' ')
            l+=1

spiral(5,5)
turtle.done
"""
a = []
count = 1
for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
            
spiral(4,4,a)
"""

'''
tur = turtle.Turtle()
for i in range(4):
    tur.forward(50)
    tur.right(90)
#turtle.done()

for i in range(5):
    tur.forward(50)
    tur.right(144)
turtle.done()
'''
