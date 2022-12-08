def add(no1,no2):
    res=no1+no2
    print(f"Addition:{res}")
    
def sub(no1,no2):
    res=no1-no2
    print(f"Substraction:{res}")
    
def mul(no1,no2):
    res=no1*no2
    print(f"Multiplication:{res}")

def div(no1,no2):
    res=no1/no2
    print(f"Division:{res}")


print(f"1.Addition ")
print(f"2.Substraction")
print(f"3.Division")
print(f"4.Division")
print(f"5.Exit")
ch=int(input("Enter choice:"))
if ch == 1:
    no1=int(input("Enter no1:"))
    no2=int(input("Enter no2:"))
    add(no1,no2)
elif ch == 2:
    no1=int(input("Enter no1:"))
    no2=int(input("Enter no2:"))
    sub(no1,no2)
elif ch == 3:
    no1=int(input("Enter no1:"))
    no2=int(input("Enter no2:"))
    mul(no1,no2)
elif ch == 4:
    no1=int(input("Enter no1:"))
    no2=int(input("Enter no2:"))
    div(no1,no2)
elif ch == 5:
    exit
    