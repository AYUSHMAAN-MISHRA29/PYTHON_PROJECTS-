# Hello visitors this is my program for calculating BMI(Body Mass Index)
import math
mass=float(input("to calculate your body mass index first enter your mass in kg"))
height=float(input("enter your height in metres"))
bmi=mass/math.pow(height,2)
if bmi>0 and bmi<18.5:
    print("You are underweight.Take proper deit")
elif bmi>=18.5 and bmi<25:
    print("You have good weight ")
elif bmi>=25 and bmi<30:
    print("you are overweight")
elif bmi >=30:
    print("You have obesity. See a doctor")
else:
    print("You enter invalid Numbers")
# Example Output:
# to calculate your body mass index first enter your mass in kg: 68
# enter your height in metres: 1.75
# You have good weight
# thanks for giving your precious time
