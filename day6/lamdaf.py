# op= lambda :5
# print(op())

# op=lambda : "naveen"
# print(op())

# op=lambda x:x+2
# print(op(5))

# op=lambda X:

#print("even") if True else Print("odd")  #terinary operator

# op=lambda x: "even" if x%2==0 else "odd"
# print(op(4)) 

# op=lambda :"nnn"
# print(op())

# op=lambda:2
# print(op())

# print("even")if True else ("odd")

# op=lambda x: "even" if x%2==0 else "odd"
# print(op(5))

# op=lambda x:"even" if x%2==0 else "odd"

# nn=lambda :"naveen"
# print(nn())

# pp=lambda :7
# print(pp())

# tt=lambda x:x+7
# print(tt(4))

# print("even") if True else print("odd") #terinary operator

# op=lambda x:print("even") if x%2==0 else ("odd")
# print(op(7))

# po=lambda v:"even" if v%2==0 else ("odd")
# print(po(9))

# po=lambda v:"accepted" if True else ("decline")
# print(po())

# pp=lambda x:x+5
# print(pp(5))


# x=10
# def show():
#   x=5
#   print(x)
# show()    
# print(x)  #output is 5 and 10

def outer():   #o/p is 10
    x=10
    def inner():
        print(x)  
    inner()
    
# outer()


# x="global"  #o/p is  outer:outer
# def outer():      #  global: global
#     x="outer"
#     def inner():
#         x="inner"
#     inner()
#     print("outer:",x)
# outer()
# print("global:",x)



