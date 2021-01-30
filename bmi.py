# This program will calculate the user's BMI 
# Author: Brendan Tunney

# Height (CM) & Weight (KG)
Height = int(input ('enter height:' ))
Weight = int(input ('enter weight:'))

# Height Conversion 
metresquared = ((Height/100) **2)

# BMI Calculation - Weight divided by their height in metres squared
BMI = int(Weight/metresquared)

print ('Your BMI is {}' .format (BMI))
