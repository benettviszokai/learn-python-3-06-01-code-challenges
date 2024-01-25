# I. Control Flow (Basic)

# 1. Not Sum to Ten

# You are given two numbers stored in num1 and num2. 
#If the sum of num1 and num2 is NOT equal to 10, then store True into a variable called not_ten, otherwise store False in not_ten.

num1 = 6
num2 = 3

if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False 

print("Does the sum of the numbers equal 10? " + str(not_ten))

##########################################################################################################

# 2. Over Budget

# You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget!
  # First, store the total of all expenses into a variable called total.
  # Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, otherwise store False in over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))

##########################################################################################################

# 3. Large Power

# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False
    
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

##########################################################################################################

# 4. Twice As Large

# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1, num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False

print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

##########################################################################################################

# 5. Divisible by Ten

# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
