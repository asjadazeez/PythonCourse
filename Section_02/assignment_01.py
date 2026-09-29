# Assignment 1:
"""
Print Bill's salary from the my_list object shown below.

my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]

"""
from urllib.robotparser import merge_entries

# your code below:
my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
print("bills salary: ", my_list[0].get('Bill'))


dict1 = {'a':1,'b':2}
dict2 = {'x':6,'b':4}
#
# print(merge_entries(dict1,dict2))
# def merge_dicts(dict1, dict2):
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)


    # return dict3




































# Solution
# print(my_list[0].get('Bill'))
