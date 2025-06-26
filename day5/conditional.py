# #statements-----> 1. normal statemnt
#  #                2. control statement
#  #control statements---->1.conditional and Looping

# '''conditional statement are used for decision making purpose.
# 1.simple if 
# 2.if-else
# 3.nested if 
# 4.nested elif
# 5.terinary operator'''

#simple_if
condition=True
if (True):
    print("you win")
print("this is if statemnt")

#if_else
No_water_in_tank =True
if(False):
    print("yes there is no water in tank")
else:
    print("water is fully in tank")
    
#enter your age while you are eligible for vote
age=int(input("enter your age: "))
if age>=18:
    print (f"your age is {age} you are eligible to vote")
else:
    print (f"your age is {age} you are minor not eligible for vote")

number=int(input("enter a number to check it is even or odd:"))
if(number%2==0):
    print("it is even number")
else :
    print("it is odd number")
print("bye....")

# nested_if
if True:
    print('nenu naveen')
    if True: 
       print ("nenu kuda naveen") 
    else:
        print("iam naveen")
else:
    print("jj")
        
# nested if
if True:
    print("you are naveen")
    if False:
        print("you naveen")
else:
     print("naveen")   
        
#elif        
if True:
  print ("iam if")
elif True:
    print("iam elif")
elif False:
    print("nenu elif naveen")
else:
    print ("iam else")       
      
num=123335
if(num & 1==0):
    print("even")
else:
    print("odd")
    
    num=1
if(num & 1==0):
    print("even")
else:
    print("even")
    
#convert
seq="02468"
ip=125701
cnvrt=str(ip)
if(cnvrt[-1] in seq):
  print("even")
else:
    print("odd")
    
seq=[0,2,4,6,8]
ip=1123
cnvrt=str(ip)
if(int(cnvrt[-1])in seq):
    print("even")
else:
    print("odd")
 
