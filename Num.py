import numpy as np
import pandas as pd
# Creating Numpy Arrays from Python Lists
 
array = np.array([1.2 , 2, 3, 4, 5]) # chuyển từ dạng list sang dạng array , chuyển kiểu sang kiểu cao hơn
array2 = np.array([[1,2,3], [4,5,6]])
print(type(array2)) # in ra type mảng
print(array2.shape) # in ra số dòng và cột
print(array2.ndim) # in ra số chiểu của mảng (2 mảng = 2 chiều)
print(array2.dtype) # in ra kdl
print(array2.size) # in ra số phần tử trong mảng

# Creating Numpy Arrays from Scratch

print(np.zeros([2,4])) # tạo mảng 2 dòng 4 cột mặc định là float mặc định phần tử là những số 0
print(np.zeros([2,4], dtype = int)) # chuyển từ float sang int
print(np.ones([3,5])) # tạo mảng 3 dòng 5 cột mặc định là float mặc định phần tử là những số 1
print(np.arange(0 ,20 ,2)) # tạo một mảng từ 0 -> 20 và mỗi phần tử cách nhau 2
print(np.full((3, 5), 6.9)) # tạo mảng 3 dòng 5 cột và các phần tử là số 6,9
print(np.linspace(0 ,1, 5)) # tạo ra 1 mảng từ 0 đến 1 và các phần tử trong mảng cách nhau miễn sao đủ 5 phần tử trong khoảng 0->1

# Random
print(np.random.seed(0)) # tạo ngẫu nhiên nhưng cố định ai cũng giống nhau
print(np.random.random((4,4))) # tạo một mảng 4 dòng 4 cột với những phần tử ngẫu nhiên 
print(np.random.rand(4,4)) # giống thằng ở trên
print(np.random.normal(0, 1, (3, 3))) # tạo ra một mảng 3 dòng 3 cột và độ lệch chuẩn từ 0 -> 1
print(np.random.randint(0, 10 , (4,5))) # tạo ra một mảng 4 dòng và 5 cột và phần tử random từ 0 -> 10

# Array indexing & slicing
# one-dimensional subarray : mảng một chiểu
x1 = np.random.randint(20 , size=6) # tạo mảng ngẫu nhiên có 6 phần tử
print(x1)
print(x1[4] , x1[-1]) # in ra phần tử thứ 4, -1 là vị trí cuối

# multi-dimensional subarray 
x2 = np.random.randint(10, size=(3,4))
print(x2)
print(x2[1,2]) # in ra phần tử theo dòng và cột
x2[1,2] = 6 # thay đổi giá trịn theo dòng và cột
print(x2[1,2]) 

# slicing
print(x1)
print(x1[0:3]) # lấy 3 phần tử đầu , không lấy phần tử cuối
print(x1[::2]) # lấy tất cả phần tử cách nhau 2 đơn vị
print(x2)
print(x2[:2,:3]) # lấy 2 dòng 3 cột
print(x2[:,:2]) # lấy hết dòng và 2 cột

# Reshaping of Arrays & Transpose
grid = np.arange(1,10) # tạo 1 mảng tử 1 đến 9 
print(grid) 
print(grid.shape) # grid có 9 dòng 
grid2 = grid.reshape((3,3))
print(grid2) # tạo thành mảng 3 dòng 3 cột

# Transpose
print(grid2.T) # chuyển dòng thành cột và ngược lại

# Array Concatenation and Spliting : nối và cắt array
x = np.array([1,2,3])
y = np.array([3,2,1])
grid = np.array([[1,2,3],[4,5,6]])
grid3 = np.array([[99],[99]])
print(np.concatenate((x, y))) #  nối 2 mảng 1 chiều
print(np.concatenate((grid, grid))) # nối 2 mảng 2 chiều theo trục dọc
print(np.concatenate((grid, grid), axis = 1)) # nối 2 mảng 2 chiều theo trục ngang
print(np.vstack((x , grid))) # nối mảng 1 chiều vào mảng 2 chiều theo trục ngang
print(np.hstack((grid3 , grid))) # nối mảng 2 chiều vào mảng 2 chiều theo trục dọc
 
# Splitting of arrays
z = np.array([1,2,3,99,69,3,2,1]) 
z1,z2,z3 = np.split(z ,[3,5]) # tách mảng làm 3
print(z1,z2,z3)

# BroadCasting
a = np.arange(3) # mặc định tạo mảng là [0,1,2]
print(a+5) # +5 vào các phần tử của mảng

b = np.ones((3,3))
print(b)
print(b+a) # biến a từ mảng 1 chiều thành mảng 2 chiều sau đó cộng lại
print(b*a) # biến a từ mảng 1 chiều thành mảng 2 chiều sau đó nhân lại

c = np.arange(3).reshape((3,1))
print(c)
print(a+c) # broadcast 2 mảng thành 3x3 sau đó mới cộng lại

# Manipulating & Comparing Arrays
print(np.sum(x)) # tính tổng 
print(np.mean(x)) # tính trung bình
print(np.max(x)) # tìm GTLN
print(np.min(x)) # tìm GTNL

# Statistics : Xác suất thống kê
# Standard deviation and Variance : độ lệch chuẩn và Phương sai
dog_height = [600, 470, 170, 430, 300]
dog_height = np.array(dog_height)
print(np.std(dog_height)) # Độ lệch chuẩn
print(np.var(dog_height)) # phương sai
print(np.sqrt(np.var(dog_height))) # căn bậc 2 phương sai sẽ ra độ lệch chuẩn

# Sorting Arrays
x = np.array([2,1,4,3,5])
x2 = np.sort(x)
print(x2) # sắp xếp mảng
print(np.argsort(x2)) # chuyển phần tử sang dạng index 

# Sorting along rows or columns
np.random.seed(42)
MatA = np.random.randint(0, 10, size=(4,6))
print(MatA)
print(np.sort(MatA, axis=0)) # sắp xếp theo chiều dọc
print(np.sort(MatA, axis=1)) # sắp xếp theo chiều ngang

# Linear Algebra : Đại số tuyến tính
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[6,5],
              [4,3],
              [2,1]])

print(A.dot(B)) # cách viết 1 : nhân hàng A với cột B ( tích vô hướng )
print(A @ B) # cách viết 2
print(B.T @ A) # đảo chiều B và nhân với A

# Dot product example

np.random.seed(0)
sales_amount = np.random.randint(20, size = (5,3))
print(sales_amount)
weekly_sales = pd.DataFrame(sales_amount, index = ["Mon", "Tue", "Wed", "Thu", "Fri"], columns = ["fish", "meats" ,"peanut"])
print(weekly_sales)

prices = np.array([10,8,12]).reshape(1,3) # in ra 1 dòng 3 cột
meals_prices = pd.DataFrame(prices, index = ["Price"], columns=["fish", "meats" ,"peanut"]) # chuyển price thành dataframe meals_prices
print(weekly_sales.shape, meals_prices.shape) # lưu ý số cột của bảng này phải bằng số dòng của bảng kia, thằng to cố định

print(meals_prices)

total_price = weekly_sales.dot(meals_prices.T) 
print(total_price)

weekly_sales["Total Price"] = total_price
print(weekly_sales)