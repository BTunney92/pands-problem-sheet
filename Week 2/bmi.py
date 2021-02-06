# This program will calculate the user's BMI 
# Author: Brendan Tunney

# Height (CM) & Weight (KG)
Height = float(input ('enter height:' ))
Weight = float(input ('enter weight:'))

# Height Conversion 
metresquared = ((Height/100) **2)

# BMI Calculation - Weight divided by their height in metres squared
BMI = round(Weight/metresquared,  2)

print ('Your BMI is {}' .format (BMI))
