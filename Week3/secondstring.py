#Program that asks user to input a sentence and outputs everty second letter in reverse order
#Author: Brendan Tunney

statement = input("Enter your sentence: ") #Setting input sentence 

print ("Your sentence in reverse order & with every second letter removed is :")
print (statement [::-2]) # Extended slices. Negative sign for reverse order
