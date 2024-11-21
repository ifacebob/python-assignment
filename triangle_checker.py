""""
This program will check the type of triangle that we have
By collecting three inputs from the user which are for the three (3) sides
"""
top = float(input("Enter value of the First Side: "))
left_side = float(input("Enter value of the Second Side: "))
Right_side = float(input("Enter value of the Third Side: "))

if top + left_side <= Right_side or top + Right_side <= left_side or left_side + Right_side <= top:
  print('This is not a Valid Triangle')
  
elif top == left_side and left_side == Right_side:
  print("Equilateral Triangle: This is a Valid because their sizes are equal")

elif top == left_side or left_side == Right_side or top == Right_side:
  print("Isosceles Triangle: Two sides are equal ")

elif top != left_side or left_side != Right_side and top != Right_side:
  print('Scalene Triangle: Not valid because All sides different')
