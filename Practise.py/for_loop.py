# #break
# for i in range(1,10):
#     print(i)
#     if i==5:
#         break

# for x in range(1,10):
#     if x==5:
#         break
#     print(x)

# for x in range(1,10):
#     print(x)
#     if x==6:
#         print("here 6")
        
#continue
# for x in range(1,10): #here we give print firstly
#     print(x)
#     if x==6:
#         continue

# for i in range(1,10):
#     if i==6:
#         continue
#     print(i)

# stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
# for i in stops:
#     if i=="ameerpet":
#         continue
#     print(i)    #end=" "

'''Loop Starts: The for loop goes through each item in the list one by one.
First: x = "kphb"
Then: x = "srnagar"
Then: x = "ameerpet"
Condition Check:
When x == "ameerpet", the condition becomes True.
Break:
The break stops the loop immediately. So the loop ends at "ameerpet".
Print:
After the loop, print(x) runs.
Since x is "ameerpet" at the time of break, it prints:'''

# see diffference
# stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
# for x in stops :
#    if x=="ameerpet":     
#        break 
# print(x)   
   
# stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
# for x in stops :
#    if x=="ameerpet":     
#        break 
#    print(x) 

# stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
# for x in stops :
#    print(x) 
#    if x=="ameerpet":     
#        break
#    print(x)

# while loop

        
# # reverse print
# x="ollom"
# op=""
# for chr in range(len(x)-1,-1,-1):
#     op+=x[chr]
# print(op)


# if (op==x):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# str="hello"
# op=""
# for i in range(len(str)-1,-1,-1):
#     op+=str[i]
# print(op)


# naveen="yadav"
# op=""
# for x in range(len(naveen)-1,-1,-1):
#     op+=naveen[x]
# print(op)

# str="2345"
# op=""
# for i in range(len(str)-1,-1,-1):
#     op+=str[i]
# print(op)

# x=input("enter a string")
# str=""
# y=len(x)-1
# while y>=0:
#     str+=x[y]
#     y=1