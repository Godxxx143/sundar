print("Sundar international [p] ltd.")
print("NO.15,villupuram dist,TamilNadu")
print("*******************************")
print("Employee payroll system")
print("*******************************")
ID =int(input("Enter the Employee:"))
name =(input("Enter the name:"))
salary=int(input("Enter the salary:"))
print("*INCOME*")
bonus=salary*20/100
print("bouns (20% percentage):",bonus)
ot=salary*10/100
print("overtime (10% percentage):",ot)
TA=salary*5/100
print("travalr allowence (5* percentage):",TA)
gp=salary+bonus+ot+TA
print("Grosspay in rupees:",gp)

