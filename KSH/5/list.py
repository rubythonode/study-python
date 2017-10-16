# python "/Users/gimseonghun/Desktop/study-python/KSH/5/list.py"
list = ['a', 'b', 'c']
list[len(list):] = list # list.append(list child)
print(list) # ['a', 'b', 'c', 'a', 'b', 'c']
# list[len(list):] = iterable = list.extend(iterable)
print
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple')) # 2
print(fruits.index('banana', 4)) # 6 starting point 4

fruits.reverse()
print(fruits) # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.sort() # order by asc
print(fruits) # ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

fruits.pop()
print(fruits) # ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange']