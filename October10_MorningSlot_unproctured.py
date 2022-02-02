'''

Given a string and width, write a program to convert the given string into different strings of given width separated by newline.

Input Format:
The first line contains a string.
The second line contains the width.

Output Format:
Print the text wrapped paragraph.

Sample Input 0:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''
string = input()
width = int(input())
string = list(string)
iterations = len(string)//width + (1 if len(string)%width!=0 else 0)
a,b=0,width
for i in range(iterations):
  to_print = ''.join(string[a:b])
  a,b=b,b+width
  print(to_print,end='')
  if i!=(iterations-1):
    print()
