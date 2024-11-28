import pandas as pd
import numpy as np


# step 1 import Dataset
df = pd.read_csv("chipotle.tsv", sep = "\t")
print(df.head(5))  # in ra 5 dòng đầu
print("-----------------------------------------------------")

# step 2 Dataset Overview
print(df.shape)  # in ra số dòng và cột
print(df.info())  # in thông tin các cột
print(list(df.columns))  # in ra tên của cột theo list
print(df.index) # in ra bắt đầu cho đến kết thúc và có bị ngắt quãng không (start=0, stop=4622, step=1)
print(df.describe()) # thông kê các cột có kdl là number
print(df.describe(include = "all")) # thông kê các cột với tất cả kdl

# location và index location # lọc dữ liệu
# --------------------------------- location 
print(df.loc[df.quantity == 15]) # in ra vị trí có quantity == 15
print(df.loc[df.quantity == 15]) # in ra vị trí có quantity == 15
print(df.loc[(df.quantity == 15) | (df.item_name == "Nantucket Nectar")]) # in ra vị trí có quantity == 15 hoặc có item_name ==  "Nantucket Nectar"
print(df.loc[(df.quantity == 2) & (df.item_name == "Nantucket Nectar")]) # in ra vị trí có quantity == 2 và có item_name ==  "Nantucket Nectar"
print(df.loc[(df.quantity == 2) & (df.item_name == "Nantucket Nectar"), ['order_id', 'quantity' ,'item_name']]) # in ra vị trí có quantity == 2 và có item_name ==  "Nantucket Nectar" và chỉ lấy 3 cột trên

# ---------------------------------- index location
print(df.iloc[[9]]) # in ra dòng thứ 9
print(df.iloc[3:11]) # in ra dòng từ 3 đến 10
print(df.iloc[3:5, 0:5]) # bên trái là dòng ,bên phải là cột 

# Data Manipulation : thao tác với dữ liệu
print(df.item_price.dtype) # cho ra kdl của cột
print(df.item_price.apply(lambda x : float( x.replace('$', '' )))) # chuyển item_price từ kiểu object sang kiểu float nhưng ko lưu
df.item_price = df.item_price.apply(lambda x : float( x.replace('$', '' ))) # chuyển item_price từ kiểu object sang kiểu float và lưu
df["total_price"] = df["quantity"]*df["item_price"] # tạo thêm cột total_price = quantity*item_price
revenue = df["total_price"].sum() # tính tổng cột total_price

# group by
most_order = df.groupby("item_name")["quantity"].sum() # nhóm order lại và tính tổng theo từng loại
most_order_sorted = most_order.sort_values(ascending=False) # sắp xếp tăng dần - nếu muốn giảm dần thì thêm (ascending=False)
print(df.item_name.value_counts()) # đếm các item_nam khác nhau
print(df.item_name.value_counts().count()) # tính tổng các sản phẩm
print(df.item_name.nunique()) # c2 tính tổng các sản phẩm
