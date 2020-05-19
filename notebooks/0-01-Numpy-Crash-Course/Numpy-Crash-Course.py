import numpy as np

mylist = [1,2,3,4]

arr = np.array(mylist)

#Exploring numpy functions

#1a: arange with a step size of 1
a = np.arange(0,10)
print(a)

#1b: arange with a step size of 2
a = np.arange(0,10,2)
print(a)

#2: zeros --> matrix of zeros of given dimension
b = np.zeros((5,5))
print(b)

b = np.zeros((1,10))
print(b)

#3: ones --> matrix of ones of given dimension
c = np.ones((2,3))
print(c)

#4: random.randint --> random integer within given range
d = np.random.randint(0,100)
print(d)

d = np.random.randint(0,100,(5,5))
print(d)

#5: linspace
e = np.linspace(0,10,7)
print(e)

#6: seed
np.random.seed(100)
f = np.random.randint(0, 100, 10)
print(f)

#7: max, min --> max and min values of an array
print(f.max())
print(f.min())

#8: mean
print(f.mean())

#9: argmax, argmin --> index values of max and min values
print(f.argmax(), f.argmin())

#10: reshape
arr = np.random.randint(1,100,(2,10))
print(arr)
print(arr.reshape(5,4))

#11: indexing
mat = np.arange(0,100).reshape(10,10)
print(mat)
print(mat[5,2])

#Give me every single row from a particular column
print(mat[:,7])

#Give me every singe column from a particular row
print(mat[0,:])

#Give me all the values greater than a particular number
print(mat[mat > 50])
