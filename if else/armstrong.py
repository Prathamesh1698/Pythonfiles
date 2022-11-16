a = int (input("enter a number:"))
b = a % 10  
c = a // 10 
d = c % 10 
e = c // 10 
f = e % 10 
g = e //10 

z = b**4 + d**4 + f**4 + g**4

if a == z:
    print (a, "is armstrong number")
else:
   print (a, "is not an armstrong number")

