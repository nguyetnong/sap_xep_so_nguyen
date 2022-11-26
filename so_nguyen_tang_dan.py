
def sap_xep(num1,num2,num3):#3 8 5
    temp=0
    if num2<num1 and num2<num3:
        temp=num1
        num1=num2
        num2=temp
    elif num3<num1 and num3<num2:
        temp=num1
        num1=num3
        num3=temp
    elif num3<num2:
        temp=num2
        num2=num3
        num3=temp
        
    return (num1, num2, num3)
x = int(input("nhap so thu nhat: "))
y = int(input("nhap so thu hai: "))
z = int(input("nhap so thu ba: "))

num1,num2,num3 = sap_xep(x,y,z)
print(num1,num2,num3)