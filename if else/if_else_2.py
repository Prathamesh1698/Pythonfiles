'''
a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
c = int(input("Enter a third number:"))

if a > b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")

else:
    if b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")
'''
'''
a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
c = int(input("Enter a third number:"))

if a > b and a > c:
    print(a,"is greater")
if b > a and b > c:
    print(b,"is greater")
if c > a and c > b:
    print(c,"is greater")
'''

a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))
c = int(input("Enter a third number:"))

if a > b and a > c:
    print(a,"is greater")
elif b > a and b > c:
    print(b,"is greater")
elif c > a and c > b:
    print(c,"is greater")
