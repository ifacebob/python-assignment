# '''
# Assignment:

# Question: Tax and Discount Calculator

# Create a Python program that calculates the final amount a customer needs to pay after applying a discount and tax. The program should meet the following requirements:

# 	1.	The program should prompt the user to input the purchase amount.
# 	2.	Based on the purchase amount, apply the following discounts:
# 	•	If the amount is less than $100, no discount.
# 	•	If the amount is between $100 and $500 (inclusive), a 10% discount.
# 	•	If the amount is greater than $500, a 20% discount.
# 	3.	After applying the discount, calculate the tax:
# 	•	If the discounted amount is less than $200, apply 5% tax.
# 	•	Otherwise, apply 8% tax.
# 	4.	Display the following:
# 	•	The original purchase amount.
# 	•	The discount applied.
# 	•	The tax applied.
# 	•	The final amount the customer needs to pay.'''


 
item_price = int(input("Kindly enter Price for the Items Purchased "))

if item_price < 100:
  discount = 0
  # print(f"The sum of {discount} was given to you as discount")

elif item_price >= 100:
  discount = 100 * 10 / 100
  # print(f"The sum of {discount} was given to you as discount")
  
else:
  discount = 500 * 20 / 100
  # print(f"The sum of {discount} was given to you as discount")
  
# dicount_given = amount_to_pay - discount
  # The is for the Tax
  
  
if discount < 200:
    tax = item_price * 5 / 100
else:
  tax = item_price * 8 /100

# The Total amount to Pay

expenses = discount + tax
amount_to_pay = item_price - expenses

# Displacing the following:
# 	•	The original purchase amount.
# 	•	The discount applied.
# 	•	The tax applied.
# 	•	The final amount the customer needs to pay.''
print(f"The Original purchase amount is: ${item_price}")
print(f"The discount value given to you is: ${discount}")
print(f"You're to pay: ${tax} as VAT fee")
print(f"You're to Pay the Total ${amount_to_pay}")
  