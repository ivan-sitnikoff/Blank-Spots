array = ['a', 'b', 'c', 'd']
gen_obj = (x for x in array)

print(type(gen_obj))

for val in gen_obj:
    print(val)
