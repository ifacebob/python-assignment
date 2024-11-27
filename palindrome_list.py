my_list = ['mummy', 
    'hannah', 
    'murder for a jar of red rum', 
    'mom', 
    'seagull', 
    'tomato', 
    'no lemon, no melon', 
    'some men interpret nine memos', 
    'madam']

def check_palindrome(my_list):
  for list in my_list:
    if list == list[::-1]:
      print(f"{list} is a palindrome ")
    
    else:
      print(f"{list} is not a palindrome")

check_palindrome(my_list)
  
