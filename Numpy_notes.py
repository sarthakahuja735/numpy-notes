# Numpy practice and notes ----- Sarthak Ahuja-----

# ----------INDEX OF NOTES---------- 
# 1 creating array
# 2 numpy array attributes
# 3 array initiallisation methods
# 4 array indexation and slicing
# 5 array reshaping and flattening
# 6 array stacking and splitting
# 7 mathematical operations on array
# 8 statistical functions
# 9 array comparision
# 10 broadcasting
# 11 handling nan (null) & infinite values

import numpy as np
print(np.__version__)

# 1) creating array - 1 dimensional array ----------
arr_list = np.array([1,2,3])
print(arr_list)
print(arr_list.ndim)


# create 2 dimensional array
arrlist1 = [1, 2, 3]
arrlist2 = [4, 5, 6]

dim_arr2 = np.array([arrlist1, arrlist2])
print(dim_arr2)
print(dim_arr2.ndim)


# create 3 dimensional array
arr_list1 = [1, 2, 3]
arr_list2 = [4, 5, 6]
arr_list3 = [7, 8, 9]

dim_arr3 =np.array([[arr_list1, arr_list2, arr_list3]])
print(dim_arr3)
print(dim_arr3.ndim)


# 2) numpy array attributes ----------
data_list1 = [1, 2, 3]
data_list2 = [4, 5, 6]
data_list3 = [7, 8, 9]

att_list = np.array([[data_list1, data_list2, data_list3]])

print("shape", att_list.shape) #showing shape of our array by just write ".shape"
print("size", att_list.size)  #showing size of our array by just write ".size"
print("Datatype", att_list.dtype)  #showing datatype of our array by just write ".dtype"


# 3) array initiallisation methods ----------

# a) zeros array
zeros = np.zeros((2,3)) #create zeros array list by just passing row and columns in paranthesis
print(zeros)

# b) one array
ones = np.ones((1,3)) #create ones array list by just passing row and columns in paranthesis like zeros
print(ones)

# c) full array
full = np.full((3, 2), 7) #create full array list by just passing row and columns in paranthesis and add number which we want to, after passing comma 
print(full)

# d) identity matrix
array = np.eye(3)
print(array)

# e) empty array
empty_arr = np.empty(5) #create empty array list but it's not fully empty
print(empty_arr)

# f) evenly spaced array
space_array = np.arange(1, 10, 2) #(start, stop, step) [1, 3, 5, 7, 9]
print(space_array)

# g) random float values array
rand_array = np.random.rand(3, 2) #create random float array list by passing numbers of rows and column
print(rand_array)

# h) random int value array
int_rand = np.random.randint(1, 10, (3, 3)) #create random int array list by passing (start, stop, (shape)) 
print(rand_array) 
print(int_rand)


# 4) array indexation and slicing ----------

# 1 dimensional
a = np.array([1, 2, 3, 4, 5, 6 , 7, 8])
print(a[5]) #accessing values by passing index number in square bracket
print(a[1:5]) #slicing by indexation, stop values not included

# 2 dimensional
b = np.array ([[1, 2, 3,] , [4, 5, 6]])
print(b[1, 0]) #array_name[rows, column]
print(b[1:]) #automatically provide all columns of selected rows


# 5) array reshaping and flattening ----------
c = np.array ([1, 2, 3, 4, 5, 6])
reshape = c.reshape((2, 3))   # change array structure or dimensions by passing ".reshape" and number of columns and rows
print(reshape)

original = c.flatten() # it converts multi dimensional or high dimentinal array to one dimensional array
print(original)


# 6) array stacking and splitting  ----------
# stacking
x = np.array([1, 2, 3])
y = np.array ([4, 5, 6])

print(np.vstack((x, y))) # verticle stack -- row wise, also it chances the dimention of array
print(np.hstack((x, y))) # horizontal stacking -- column wise

#splitting
xarray = np.array([[1, 2, 3], [4, 5, 6]])
print(np.hsplit(xarray, 3)) #horizontal split
print(np.vsplit(xarray,2)) # verticle split


# 7) mathematical operations on array ----------

d = np.array([20, 30, -40, 50])

print("add", (d + 10)) # addition in array
print("subtract", (d - 20)) # subtraction in array
print("multiply", (d * 2))  # multiplication in array
print("division", (d / 5))  # division in array
print("square", np.square(d)) # square in array
print("sum", np.sum(d)) # for sum of array

e = np.array([1, 4, 9])

print("square root", np.sqrt(e)) #square root on array
print("sin", np.sin(e)) # sin on array
print("cos", np.cos(e)) # cos on array
print("tan", np.tan(e)) # tan on array

f = np.array([[1, 2, 3],
             [4, 5, 6]])
print(f.T) # TRANSPOSE is use for to interchange the rows into columns or columns into rows


# 8) statistical functions ----------
ab = np.array([[1, 2, 3],
              [4, 5, 6]])

print("mean", np.mean(ab)) # for mean
print("median", np.median(ab)) # for median
print("standard devaition", np.std(ab)) # for standard devaition
print("minimum", np.min(ab)) # for minimum
print("maximum", np.max(ab)) # for maximum


# 9) array comparision  ----------

xx = [4, 2, 3]
yy = [4, 5, 6]

print(xx == yy) # comparing each element
print(np.array_equal(xx, yy)) # comparing complete array


# 10) broadcasting = Broadcasting is a feature in NumPy that allows you to perform operations on arrays of different shapes  ----------

a1 = np.array([1, 2, 3])
b1 = 2
print(a1 + b1)

# 11) handling nan (null) & infinite values  ----------

data1 = np.array([1, 2, np.nan, 4, np.inf]) # nan = null, inf = infinite
print(data1)
print(np.isnan(data1)) #for finding null values as True
print(np.nan_to_num(data1)) # convert null values into 0