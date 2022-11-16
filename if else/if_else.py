'''
Num = int(input("enter a number:"))
if (Num%2) == 0:
    print("even number")
else:
    print("Odd number")
'''

'''
Num = int(input("enter a number:"))
if Num > 0:
    print("Positive number")
else:
    print("Negative number")
'''

'''
num = int(input("enter a number:"))
a = num % 10
b = num // 10
c = b %10
d = b // 10
sum = a **3 + c **3 + d ** 3
if sum == num:
 print("Number is armstrong")
else :
    print("It is not armstrong")
'''

Num = int(input("enter a number:"))
if Num == 0:
    print("Number is neither negative or positive")
else:

    if Num > 0:
        print("Positive number")
    else:
        print("Negative number")
