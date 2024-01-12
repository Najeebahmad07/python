a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
op=input("Enter Operator(+.-,*,/)")
print("---------------------------------------")

if op=="+":
    print(a+b)

elif op=="-":
    print(a-b)

elif op == "*":
    print(a * b)

elif op == "/":
    print(a / b)

else:
    print("choose correct operator")

