N1=float(input("enter the first grade"))
while   N1<0 or N1>20  :
    N1=float(input("this score is incorrect ,please enter the correct grade"))
N2=float(input("enter the  second grade"))
while   N2<0 or N2>20  :
    N2=float(input("this score is incorrect ,please enter the correct grade"))
N3=float(input("enter the third grade"))
while   N3<0 or N3>20  :
    N3=float(input("this score is incorrect,please enter the correct grade"))
M=(N1+N2+N3)/3
print("your total score is:",M)
if M>=16:
    print("with highest honour")
elif M<16 and M>=14:
    print("with high honours")
elif M<14 and M>=12:
    print("with honors")
elif  M<12 and M>=10:
    print("with standard pass")
else:
    print("insufficient")

