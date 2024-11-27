# Return True or False if a value is a Palindrome
def is_palindrome(item):
  if item == item[::-1]:
    return True
  else:
    return False
    # print(False)
  
# Enter the item
item = input("Enter item: ").lower()

print(is_palindrome(item))


