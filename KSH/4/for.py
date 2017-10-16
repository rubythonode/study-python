# python "/Users/gimseonghun/Desktop/study-python/KSH/4/for.py"

words = ['cat', 'window', 'defenestrate']
for w in words:                 # w = words[i..len(w)]
    print(w, len(w))
for w in words[:]:              # Loop over a slice copy of the entire list.
    if len(w) > 6:              # String w length > 6
        words.insert(0, w)      # Insert w in words
print(words)                    # ['defenestrate', 'cat', 'window', 'defenestrate']

print
for i in range(5):              # [0..5-1]
    print(i)
print
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)): # 
    print(i, a[i])
print
for n in range(2, 10): # 2..10-1
    for x in range(2, n): # 2..n-1
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: # for x in if else
        print(n, 'is a prime number')