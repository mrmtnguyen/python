import sys

def collatz(number):
    if ((number % 2)== 0):
        return number//2
    else:
        return 3*number+1

print('Please enter value')
try:
    value=int(input())
except:
    print("Please enter an integer")
while (value != 1):
    value = collatz(value)
    print(value)
