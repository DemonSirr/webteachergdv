"""
print("Hello World!")

a = "Hello World!"

print(a)

b = 54
c = 46

d = b + c

print(d)

f = 5.5
print(f)

print(type(a))
print(type(d))
print(type(f))

e = True
print(e, type(e))
"""
arr = [1, 2, 3, 4, 5]
print(arr, type(arr))

print(arr[0] + arr[1])

arr[4] = 6
print(arr)

arr.append(7)
print (arr)

print(len(arr))

for i in arr:
    print(f"число:{i}")

n = 10
#n = n + 1
n =+ 1
print(n)

#n = 0
#while n < 10:
#    n += 1
#    print (f'number:{n}')

"""
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    i += 1
    j = 1
    print("\n")
"""
"""
c1 = "ab"
c2 = "cd"
for c in c1:
    for s in c2:
        print(f'{c}{s}')
"""

for i in [1,2,3,4]:
    if i == 3:
        continue
    
    print(f'number: {i}')
