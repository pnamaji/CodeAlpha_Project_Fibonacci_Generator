
num = int(input('Enter the Number: .'))
a = 0
b = 1
for i in range (0,num+1):
    if i==0 or i==1:
        print(i)
        continue
    c = a + b
    a = b
    b = c
    print(c)