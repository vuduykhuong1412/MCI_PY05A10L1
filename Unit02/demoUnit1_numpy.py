import numpy as np

# Khai bao mang 1 chieu
arr1 = np.array([1, 3, 5, 7, 9])
print(arr1)

arr2 = np.array([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [10, 11, 12, 13, 14]])
print(arr2)

# Kich thuoc cua mang
print(arr2.shape)

# mang 2 chieu
arr3 = np.array([[4, 5, 6], [1, 2, 3]], dtype=float)
print(arr3)
print(arr3.shape)

# mang 3 chieu
arr4 = np.array([[[2, 4, 0, 6], [4, 7, 5, 6]],
                 [[0, 3, 2, 1],[9, 4, 5, 6]],
                 [[5, 8, 6, 4], [1, 4, 6, 8]]], dtype=int)
print(arr4)
print(arr4.shape)

#zeros
arr5 = np.zeros((3, 4), dtype=int)
print(arr5)

#ones
arr6 = np.ones((2, 3), dtype=int)
print(arr6)

#arrange
arr7 = np.arange(1,7,1)
print(arr7)

#full
arr8 = np.full((2, 3), 5)
print(arr8)

# eye
arr9 = np.eye(4, dtype=int)
print(arr9)

#random
arr10 = np.random.random((2,3))
print(arr10)

# lay kieu du lieu
print(arr10.dtype)

print("-----------------")

# thay doi kich thuoc
# arr2.reshape([5, 3])
# print(arr2)

# thay doi kieu du lieu
arr2.astype(np.float32)
print(arr2)

# truy cap phan tu cua mang
print(arr1[3])
print(arr2[1, 3])
print(arr2[2][1])

#slice mang
print(arr1[1:5])
print(arr2[:, 1:3])

#ARRAY MATH
x = np.array([[1, 2, 6], [3, 4, 8]], dtype=float)
y = np.array([[5, 6, 9], [7, 8, 7]], dtype=float)
z = np.array([[5, 6, 9], [7, 8, 7]], dtype=float)
print(x+y)
print(x-y)
print(x.shape)
print(z.shape)
print(np.multiply(x, z))    #print(x * z)
print(np.divide(x, z))      #print(x/z)

print("------------------")
#sorting
print(z.sort())

print("---------//---------")
print(x)
# luu ma tran vao file
np.save('arr_save.npy', x)

arr11 = np.load('arr_save.npy')
print(arr11)

# Doc ghi ma tran file text
arr12 = np.loadtxt('array.txt', delimiter=',')
print(arr12)
np.savetxt('array.txt', arr11, delimiter=',')

