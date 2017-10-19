basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('asdfasdf' in basket)
a = set('aaaasdfssdfsdfsdfzzxcvzxcv')
b = set('asdfasdfasdfs')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b) # letters in a or b but not both
print
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
