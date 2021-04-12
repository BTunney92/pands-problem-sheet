# Program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author: Brendan Tunney

# Newton's method - √N = 1/2 (N/X + X)

def newton_method(number, number_iters = 1):
    x = float(number)

    for i in range(number_iters):
       number = 0.5 * (number + x / number)

    return number

x=float(input("Please insert a positive integer :"))

print("Hi, the square root is :", newton_method(x))

#References - https://www.school-for-champions.com/algebra/square_root_approx.htm
            # https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method








    



  


