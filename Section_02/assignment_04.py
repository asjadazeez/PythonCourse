# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


# Your Code Below:


# mylistintuple =  my_list[2][0]
# print(mylistintuple)
# mylistintuple[3] = 'x'
#
# mythirdtupel = my_list[2]
# mythirdtuplelist = list(my_list[2])
# print(mythirdtuplelist)
# mythirdtuplenew =  tuple(mythirdtuplelist)
# print(mythirdtuplenew)
# my_list[3] = 'Television'
# my_list[2] = mythirdtuplenew
# print(my_list)


my_list[2][0][3]='x'
my_list[3] = 'Television'
print(my_list)
print((my_list[2][0]).append(['h','p']))
print(my_list)



def welcome_bot():
    # Step 1: Create a list of size 6
    my_list = ["Hello", "world,", "I", "am", "learning" "Python!"]
    # Step 2: Store each word of the message "Hello world, I am learning Python!" into the list
    # Step 3: Print only the first 3 words ("Hello" , "world," , "I")
    print(my_list[0] + my_list[1] + my_list[2])

    # Step 4: Reassign the list to a new size of 10 (filled with None)

    my_list.append('None')
    my_list.append('None')
    my_list.append('None')
    my_list.append('None')
    # Step 5: Try printing words[0] again and observe what happens
    print(my_list[0])

welcome_bot()
# Solution:
# my_list[2][0][3] = 'x'
# my_list[3] = 'Television'
# print(my_list)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']


# Print the list
print (fruits)
# Add a new fruit to the end
fruits.append('fig')
# Remove the first fruit
fruits.pop(5)
# Print the updated list
print(fruits)


