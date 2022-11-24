'''
Find number of vowels and Consonants in the string
entered by user.

a,e,i,o,u,A,E,I,O,U
'''


str = input ("enter string ")
v=0
c=0
for x in str:
    if x in ('a','e','i','o','u','A','E','I','O','U'):
        v +=1
    else:
        c +=1


print ('vowels:',v)
print ('C:',c)
