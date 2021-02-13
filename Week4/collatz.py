#Program that asks the user to input any positive integer and outputs the successive values of the following calculation
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
#Program ends if the current value is one

#Author: Brendan Tunney

#Input an integer
integer = int(input ("PLease input a number "':'))
x = integer

#Set out parameters if current value is odd or even

while x !=1:
    if x % 2==0:
        x = (x//2)
        print (int(x))
    
    elif x % 2==1:
        x = ((3*x)+1)
        print (int(x))

