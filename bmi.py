weight = float(input("Enter your Weight: "))
height =float(input("Enter your Height: "))



print(f"Your Height is: {weight}kg and Your Height is: {height}m")

# Normal to measure weight is by kilogram 
# you can collect ur height in feet and convert to meters  (height * 0.3048) will give you height in meters but to bypass this 

bmi = weight / (height ** 2)
print("Your BMI number: {bmi:.2f}")


if bmi < 18.5:
  print("Your BMI is: Underweight")

elif bmi < 25:
  print("Your BMI is: Normal")

elif bmi < 30:
  print('Your BMI is: Overweight')

else:
  print("Your BMI status: Obesity")

  
