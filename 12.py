print("goverment of tamilnadu")
print("electricity")
print("--------------")
print("bill recipt")
print("----------")
no=int(input("Enter the EB NO:"))
na=str(input("Entert the name:"))
pu=int(input("Enter the previous unit:"))
cu=int(input("Enter the current unit:"))
u=cu-pu
print("total unit:",u)
if(unit>=1000):
    amount=unit*10/100
    print("amount to be paid",amount)
elif(unit>=500):
    amt=unit*5
    print("amount to be paid",amount)
elif(unit>=100):
    amount=unit*2
    print("amount to be paid",amount)
else:
    print("amount to be paid:nill")
