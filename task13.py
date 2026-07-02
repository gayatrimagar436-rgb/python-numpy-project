#q1
"""import numpy as np
arr1=np.array([10,20,30,40,50])
print(arr1)
arr2= np.array([[23,45,67],[56,78,90]])
print(arr2)"""

#q2
"""import numpy as np 
arr1=np.zeros(8)
print(arr1)
arr2=np.ones((4,4))
print(arr2)
arr3=np.zeros((3,3))
print(arr3)"""

#q3
"""import numpy as np
arr1=np.arange(0,20,1)
print(arr1)
arr2=np.arange(10,50,2)
print(arr2)
arr3=np.arange([5,100,5])
print(arr3)"""

#q4
"""import numpy as np
arr1=np.linspace(0,5,10)
print(arr1)
print("length :",arr1.size)
arr2=np.linspace(-10,10,15)
print(arr2)
print("length:",arr2.size)"""

#q5
"""import numpy as np 
arr1=np.random.rand(10)
print(arr1)
arr2=np.random.randn(3,3)
arr3=np.random.randint(10,51,size=(4,5))
print(arr3)"""

#q6
"""import numpy as np
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])
print("additon of vector:",v1+v2)
print("subtraction  of vector:",v1-v2)
print("multiplication  of vector:",v1*v2)
print("dot product:",np.dot(v1,v2))"""

#q7
"""
import numpy as np
A = np.array([ [1,2,3],[4,5,6],[7,8,9]])
B = np.array([[ 9,8,7],[6,5,4],[3,2,1]])
print("additoin:\n",A+B)
print("dot product:\n",np.dot(A,B))
print("multiplication :\n",A*B)"""

#q8
"""import numpy as np
arr=np.random.randint(1,100,size=(4,4))
print(arr)
print("size of  matrix:",arr.shape)
print("dimension of matrix:",arr.ndim)
print("no. of element:",arr.size)
print("data type of matrix:",arr.dtype)"""

#q9
import numpy as np
arr=np.random.randint(1,51,20)
print(arr)
matrix=arr.reshape(4,5)
print(matrix)
print("sum:",np.sum(matrix))
print("mean :",np.mean(matrix))
print("standard deviation :",np.std(matrix))
print("maximum value:",np.max(matrix,axis=1))


#10
import numpy as np 
try :
    n= int (input("how many numbers do you  want to generate "))
    arr=np.random.randint(10,101,n)
    print("generated array :",arr) 
    print("mean:",np.mean(arr))
    print("median:",np.median(arr))
    print("standard deviation :",np.std(arr))
    print("mininum :",np.min(arr))
    print("maximum: ",np.max(arr))

    rows = int (input("enter number of rows for reshaping :"))
    if n%rows ==0:
        matrix=arr.reshape(rows,n//rows )
        print("\n2D array:",matrix )
        print("\n row wise sum ")
        print(np.sum(matrix,axis=1))

    else:
      print("reshape not possible :")
except valueError:
 print("please enter valid integer values ")
except Exception as e: 
 print("error:",e)
finally:
 print("always executed ")







