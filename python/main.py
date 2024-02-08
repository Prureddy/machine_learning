# # # # #int,float, str()
# # # # x = 1
# # # # y = 1.5 
# # # # z = "3"

# # # # a = float(1)
# # # # print(a)

# # # # #implicit typecasting 
# # # # #explicit typecasting


# # # # a = "Darpana"
# # # # b = "Shree"
# # # # c = a +" "+ b

# # # # print(c)

# # # # #python strings
# # # # str_var = "Hello World!" 
# # # # # for x in str_var:
# # # # #     print(x)

# # # # print(str_var[0])
# # # # #built in functions in python 
# # # # print(len(str_var))


# # # # #string Methods
# # # # #uppercase
# # # # #lowercase
# # # # #strip
# # # # #replace
# # # # #split

# # # # a = "PRUTHVI S"
# # # # b = "chintu"
# # # # # print(a.lower())
# # # # # print(b.upper())
# # # # # print(a.strip())
# # # # U = a.replace("S","V")
# # # # print(U)

# # # # a = "Hello,World!"
# # # # print(a.split("Wo"))









# # # # #slicing


# # # #Escape Charecter

# # # # a = "\tHello I am \"pruthvi\" and\n i am studying at \"DSU\" "
# # # # print(a)

# # # # True or False

# # # a = 0
# # # b =" "



# # # # print(bool(False))
# # # # print(bool(True)) 
# # # # print(bool(0)) 
# # # # print(bool(" "))
# # # # print(bool())  


# # # #logical operators
# # # #and , or , not
# # # sslc = 70
# # # puc = 90

# # # a = "Hello world!"

# # # if "h" not in a:
# # #     print("H is not in Hello world")
# # # else:
# # #     print("H is in hello world")
    
# # # if(sslc >= 60 or puc >= 60):
# # #     print("You are eligible")
# # # else:
# # #     print("you are not  eligible")

# # #Lists(Arrays)
# # #Tuples
# # #Dictionaries
# # #Sets
# # a = "hello world 123"
# # a = 343

# # thisList = ["Pruthvi", 123, True,"Shree","Pruthvi","Chintu"] 
# # print(thisList)

# # #Properties of Lists 1.Ordered 2.Changeble(mutable) 3.Allow Duplicates
# # print(len(thisList))
# # print(type(thisList))

# # thisList = list(("Pruthvi", 123, True,"Shree","Pruthvi","Chintu"))


# # #Insert
# # thisList.insert(5,"Gunda")
# # print(thisList)

# # #append
# # thisList.append("Orange")
# # print(thisList)

# # #Extend 
# # fruits=["Apple","Banana","Mango"]
# # cars = ["Ferrari","Lamborgini","Swift"]

# # fruits.extend(cars)
# # print(fruits)



# # # print(thisList[1])
# # # print(thisList[-1])

# # # #slicing
# # # print(thisList[3:])


# # # #string reverse

# # # a = "Hello world!"
# # # print(a[::-1])

# #Tuples
# # thisList = ["gd","jgd"]
# # thisTuple = ("chintu","darpana")
# # print(type(thisTuple))
# # print(thisTuple[1])

# #negetive index
# #slicing [2:5]

# #Tuple Properties - 1.Ordered 2.immutable 3.allow duplicates
# # thisTuple = ("chintu","darpana","Pruthvi",123)
# # y = list(thisTuple)
# # y.append("Pruthvi s")
# # thisTuple = tuple(y)
# # print(type(thisTuple))

# # y = ("Orange",)
# # thisTuple = thisTuple + y
# # print(thisTuple)

# #Unpacking a tuple

# # (x,*y,z)=thisTuple

# # print(y)
# #40 - 60

# # for x in thisTuple:
# #     print(x)
# thisTuple = ("chintu","darpana","Pruthvi",123,635,663)   
# thisTuple1 = thisTuple * 3
# print(thisTuple1)
# # for x in range(1,3):
# #     print(thisTuple[x])



# # for x in range(len(thisTuple)):
# #     print(thisTuple[x])




