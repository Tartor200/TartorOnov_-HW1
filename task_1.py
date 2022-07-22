
#collecting the inputs and storing them in variables num1, num2 and num3 
num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
num3=int(input("Enter Third Number"))
# for maximum number.
if (num1> num2 and num1> num3):
    print("The maximum number is", num1)
elif (num2 > num1 and num2> num3):
    print ("The maximum number is", num2)
else:
    print ("The maximum number is", num3)
    #for minimum number.
if (num1< num2 and num1< num3):
    print ("The minimum number is", num1)
elif (num2 < num1 and num2 < num3):
     print ("The minimum number is", num2)
else:
    print ("The minimum number is", num3)       
 #for remaining number.
if (num1 >num2 and num1< num3):
    print ("The remaining number is", num1)
elif (num2 >num1 and num2 < num3):
    print ("The remaining number is", num2)
else:
    print ("The remaining number is", num3)
 