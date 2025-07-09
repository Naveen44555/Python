# n=49
# sq=n**(1/2)
# print(int(sq))

# v=8
# sq=v**0.5
# print(sq)

num=int(input("enter a number: "))
if num==num**0.5:
    print(num)
else:
    print("it is not square number")
# for i in range(0,10):
#     print(i)

# #even numbers  start with 0
# for i in range(0,10,2):
#     print(i)

# for i in range(0,10,1):
#     print(i)

# odd numbers start with 1
# for i in range(1,10,2):
#     print(i)

# list
# a=[1,2,3,4,5]
# for i in a:
#     print(i)

# # string  
# b="python life"
# for k in b:
#     print(k)
    
# # string  - print Lo b isthe "python life 11 times print ayiddi."
# b="python life"
# for k in b:
#     print(b)

# for i in range(0,10):
#    print("hi",i)
    

# #while loop
# while True:
#     print("hi")

# see difference
# k=10
# while (k<20):
#     print("hii",k)

# k=10
# while (k<20):
#     print("hii",k)
#     k+=1

# nested for
# for i in range(0,10):
#     for j in range (0,6):
#         print(j)
        
# for i in range(0,10):
#     for j in range(0,100):
#         print(i+j)

# days=('m','t','w','th','f','sat','s')
# today_index=0
# future_index=(today_index + 278) % 7
# print(days[future_index])

# days=['m','t','w','th','f','sat','s']

# today_index=6
# future_index=(today_index + 365) % 7
# print(days[future_index])


# jenny-    Loops 
# for-loop

# for var_name in range():
#     statement(s)

# # we can give tuple,dictionary,set
# names=('jenni','ravi','raju','reethu')
# for name in names:
#     print(name)

# names=['jenni','ravi','raju','reethu']
# for name in names:
#     print(name)
    
# names={'jenni','ravi','raju','reethu'}
# for name in names:
#     print(name)
    
# #string - kinda naveen vastundi
# name="veerashankar","naveen"
# for i in name:
#     print(i)
    
# name="veerashankar","jjkk"
# for i in name:
#     print(i,end=" ")

# names=['jenni','ravi','raju','reethu']
# for i in names:
#     print(i)
#     if i=='jenni':
#        print("hey it's me")

# names=['jenni','ravi','raju','reethu']
# for k in names:
#     print(k)
#     if k=='ravi':
#         print("hey nenu ravi nii")

# #square of numbers in list, tuple, dictionary set

# numbers=[2,3,4,-5,6]
# for i in numbers:
#     square=i**2
#     print(square)
    
# numbers={2,3,4,-6,7}
# for g in numbers:
#     squares=g**2
#     print(squares)

# only list lo mathrame vasthadii set, dict tuple lo ravuu
# num=(2,4,5,6,-8)
# squares=[]
# for i in num:
#     square=i**2
#     squares.append(square)
# print(squares)

## else block using in for loop
# numbers=[1,2,3,5,-7,8]
# for i in numbers:
#     print(i)
# else:
#     print("else also block is executed")
# print("last print also executed")

# method 2
# numbers=[1,2,3,5,-6,8]
# for i in numbers:
#     print(i)
#     if i==-6:
#         break
# else:
#     print("else block succesfulley executed")

# num=[1,2,3,4,5,-7,-8,9]
# for i in num:
#     # print(i)
#     if i%6==0:
#         print("divisible by 6")
#     else:
#         print("not divisible by 6")
    
# num=[1,2,3,4,5,6,-7,-8,9]
# for i in num:
#     if i%6==0:
#         print(i)
#         break
#     else:
#         print("not divisible by 6")

number=int(input('enter a number: '))
number.split()