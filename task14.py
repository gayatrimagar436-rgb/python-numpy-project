#q1
"""import numpy as np
arr1=np.random.randint(10,101,size=(5,6))
print("array:",arr1)
print("shape of array:",arr1.shape)
print("size :",arr1.size)
print("data types:",arr1.dtype)"""


#q2
"""import numpy as np
arr=np.random.rand(1,51,2)
print(arr)
print("minimum value:",arr.argmin())
print("maximum value:",arr.argmax())
print("sum of array:",arr.sum())
print("mean:",arr.mean())
print("standard deviation :",arr.std())"""

#Q3
"""import numpy as np 
arr =np.random.randint(20,80,size=(4,5))
print(arr)
print("minimum value:",arr.min())
print("maximum value:",arr.max())
print("sum:",arr.sum())
print("mean:",arr.mean())
print("standard deviation:",arr.std())
print("sum of each row:",np.sum(arr,axis=1))
print("sum of each column:",np.sum(arr,axis=0))"""

#q4
"""import numpy as np 
arr=np.arange(24)
print(arr)
reshaped=arr.reshape(4,6)
print("reshape in (4,6):\n",reshaped)
print("reshape in (3,8):\n",arr.reshape(3,8))
print("reshape in (2,3,4,):\n",arr.reshape(2,3,4))"""


#Q5
"""import numpy as np 
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])
print("first row:",arr[0])
print("last column:",arr[:,3])
print("sub array :\n",arr[0:2,1:3])
print("even numbers:",arr[arr%2==0])"""


#q6
"""import numpy as np
arr=np.random.randint(1,101,size=(5,5))
print(arr)
print("diagonal elements:\n",arr[0,0],arr[0,4],"\n",arr[4,0],arr[4,4])
greater= arr[arr>50]
print(greater)
arr[arr<30]=0
print("modified matrix:",arr)"""

#q7
"""import numpy as np 
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print("addition :",a+b)
print("subtraction :",a-b)
print("multiplication  :",a*b)
print("division :",a/b)
print("modulo:",a%b)
print("power:",a**b)"""

#q8
"""
import numpy as np
A = np.array ([(1,2,3),(4,5,6),(7,8,9)])
B = np.array( [(9,8,7),(6,5,4),(3,2,1)])
print("multiplication :\n",A*B)
print("multipication :\n",np.dot(A,B))"""


#q9
"""import numpy as np 
arr=np.random.randn(6,6)
print(arr)
print("shape:",arr.shape)
print("size:",arr.size)
print("datatype:",arr.dtype)
print("index of miximum value :",np.where(arr==np.max(arr)))
print("index of minimum value :",np.where(arr==np.min(arr)))
print(" sub matrix:",arr[:3,:3])
arr[arr<0]=np.abs(arr[arr<0])
print("modified array:",arr)
print("\n mean of modified array :",np.mean(arr))"""

#q10
import numpy as np 
mark= np.random.randint(1,50,size=(10,5))
print(" mark of student:", mark )
print("shape:",mark.shape)
total_mark=np.sum(mark,axis=1)
print("total marks:",total_mark)
average=np.mean(mark,axis=1)
print("average mark:",average)
hightest=np.argmax(total_mark)
lowest=np.argmin(total_mark)
print("student with hightest mark:\n",hightest+1)
print("student with lowest  mark:\n",lowest+1)

print("class mean :\n",np.mean(mark))
print("class standard deviation :\n",np.std(mark))
top3=np.argsort(total_mark)[-3:]
print("top 3 students index:\n",top3)
print("mark of  top 3 students :\n",mark[top3])