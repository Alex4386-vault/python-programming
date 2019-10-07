tu = ('apple', [7,5,6], (1,2,3))
print("original : tu =", tu)

# convert the tuple 'tu' to a list 'li'
li = list(tu)
print("casting : li =", li)

# convert the list 'li' to a new tuple 'tu2'
tu2 = tuple(li)
print("converted tuple :", tu2)

# change the value of convertible tu2[1][1] to 20
tu2[1][1] = 20
print("tu2[1][1]=20, result :", tu2)

# Compute the sum of the first two element of 'tu2' and assign it to 'tu2[1][2]'
tu2[1][2] = sum(tu2[1][0:2])
print("sum(tu2[1][0:2]), result :", tu2)