'''
    swap variables
'''

# with temp var
x = 5
y = 10

print(x,y)
tmp = x
x = y
y = tmp

print(x,y)

# without temp var
x,y = y,x

print(x,y)