a=int(input("enter the first angle: "))
b=int(input("enter the second angle : "))
c=int(input("enter the third angle : "))
if a==90 or b==90 or c==90:
    print("this is a right angle triangle")
elif a>90 or b>90 or c>90:
    print("this is a obtuse angle triangle")
else:
    print("this is a acute angle")