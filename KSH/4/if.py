# python "/Users/gimseonghun/Desktop/study-python/KSH/4/if.py"

# elif = else if
x = int(input("Please enter an integer: "))
if x < 0: # 0 보다 작을 때
    x = 0 # x를 0 으로 설정
    print('Negative changed to zero')
elif x == 0: # 0일 때
    print('Zero')
elif x == 1: # 1일 때
    print('Single')
else: # 1보다 큰 수
    print('More')