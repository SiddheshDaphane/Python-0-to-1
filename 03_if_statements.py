'''
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

'''

a = 97
b = 55
if a<b:
    print(b)

a = 93
b= 27
if a >= b:
    print(a)

a = 27
b= 93
if a >= b:
    print(a)
else:
    print(b)

a = 27
b= 93
if a <= b:
    print("a is less than or equal to b")
elif a== b:
    print("a is equal to b")

a = 27
b = 27
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

a = 16
b = 25
c = 27

if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")
    else:
        print("a is greater than b and less than c")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")