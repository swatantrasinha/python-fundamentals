# age= input("how old are you \n")
# decades= age/10  
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# age= int (input("how old are you \n")) # type 34
# decades= age/10  
# print("you are " + str(decades) + " decades old.") 
# output - you are 3.4 decades old.

## Note: But we we want output like "3 decades and 4 years old" then we need quotient and remainder values

user_age= int (input("how old are you \n")) # type 34
user_decades= user_age // 10
user_years=   user_age % 10
print("you are " + str(user_decades) + " decades and " + str(user_years) + " years old") 
# output - you are 3 decades and 4 years old