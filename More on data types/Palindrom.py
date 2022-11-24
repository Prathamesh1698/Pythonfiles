'''
Check whether string entered by user is palindrome or not.

            N I T I N
            -------->
            <--------

    if original string == reversed string  => It is palindrome
algo
===
step1:start
step2:reversed string entered by user.
step3:check reversed and original string
step4:if both are equal then its palindrome otherwise not.

reversed  ===>  [::-1]
'''

ch1 = input("Enter string:")
ch2 = ch1 [::-1]

if ch1==ch2:
    print("It is palindrome")
else:
    print("It is not a palindrome")
