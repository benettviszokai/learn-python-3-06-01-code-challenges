# 4. Lists (Advanced)

# 1. Every Three Numbers

# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  return list(range(start, 101, 3))
  
print(every_three_nums(88))

##########################################################################################################

# 2. Remove Middle

# Create a function named remove_middle which has three parameters named my_list, start, and end.
# The function should return a list where all elements in my_list with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

def remove_middle(my_list, start, end):
  new_list = my_list[:start] + my_list[end + 1:]
  return new_list

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

##########################################################################################################

# 3. More Frequent Item

# Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in my_list.
# If the two items appear the same number of times, return item1.

def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

##########################################################################################################

# 4. Double Index

# Create a function named double_index that has two parameters: a list named my_list and a single number named index.
# The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

def double_index(my_list, index):
  #  check if the index is valid
  if index >= len(my_list):
    return my_list
  else:
    index_element = my_list.pop(index)
    my_list.insert(index, index_element * 2)
    return my_list

print(double_index([3, 8, -10, 12], 9))

##########################################################################################################

# 5. Middle Item

# Create a function called middle_element that has one parameter named my_list.
# If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(my_list):
  if len(my_list) % 2 != 0:
    return my_list[int(len(my_list)/2)]
  else:
    index1 = int(len(my_list) / 2 - 1)
    index2 = int(len(my_list) / 2)
    newlist = my_list[index1:index2 + 1]
    average = int((newlist[0] + newlist[1]) / 2)
    return average

print(middle_element([5, 2, -10, -4, 4, 20]))
