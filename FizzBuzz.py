m,n=[int(x) for x in input("Enter starting and ending range: ").split(' ')]
for i in range(m,n+1):
   if i%3==0 and i%5==0:
      print(i,"FizzBuzz")
   elif i%3==0:
      print(i,"Fizz")
   elif i%5==0:
      print(i,"Buzz")
   else:
      print(i)
