# importing necessary libraries
import numpy as np
#matrix A
a=np.array([[1,2,3],[4,5,6]]) # array creation
print("array elements are:")
print(a) #displaying the areated matrix/array
print("type of array:",type(a)) # data type of array:type(a)
print("shape of the array:",a.shape)# shape of the array:a.shape
print("size of array:",a.size)#size of array:a.size

#example 1
example_1=np.array([[1,'i',0],[0,'pi',-1]])
print("array elements are:")
print(example_1)
print("type of array:",type(example_1))
print("shape of the array:",example_1.shape)
print("size of array:",example_1.size)

#example 2
example_2=np.array([[1],[0]])
print("array elements are:")
print(example_2)
print("type of array:",type(example_2))
print("shape of the array:",example_2.shape)
print("size of array:",example_2.size)

#example 3
example_3=np.array([1,0])
print("array elements are:")
print(example_3)
print("type of array:",type(example_3))
print("shape of the array:",example_3.shape)
print("size of array:",example_3.size)