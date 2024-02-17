"""6.	Write a program to check Palindrome numbers in a given list"""
lst=int(input("enter any number"))

rev=0
temp=lst
while lst!=0:
    digit=lst % 10
    rev= rev * 10 +digit
    lst//=10
print(f'The reverse of{lst} is ::',rev)

if rev== temp:
    print(f"The number {rev} is pallindrome")
else:
    print(f"the number{rev} is not pallindrome")