def countDown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
        
print(type(countDown(10)))

for val in countDown(10):
    print(val)