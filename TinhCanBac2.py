import math

#Hàm main chú thích 
'''
Đây là chú thích trên nhiều dòng
dong1 
dong2 
dong3
'''
a = 16
kq = math.sqrt(a)

print("Căn bậc 2 của "  + str(a) + " = " + str(kq)) 
print("Căn bậc 2 của " , a ,"=" , kq) 

b = 16
mu = math.pow(b, 2 )

print(b,"mũ 2 là: ", mu)

# chu vi và diện tích hình chữ nhật
cd = 6
cr = 4
cv = (cd + cr)*2
dt = cd * cr
print("Chu vi và diện tích hình chữ nhật lần lượt là:",cv,dt)
print(type(cd))