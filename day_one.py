import asyncio
# a = [{"name": "ok", "age": 30},{"name": "ok1", "age": 33} ]
# a.remove({"name": "ok", "age": 30})
# print(a)

# num_list = [1,234,51314,123,41,1,234,51561] 
# num_list.sort(reverse=True)
# print(num_list)


# new_array = []

# for x in range(1,20):
#     if x%2 == 0:
#         new_array.append(x)

# print("Even number", new_array)
# new_array.sort(reverse=True)
# print("Sorted Array", new_array)


# stringArray= ["ram", "shyam", "hari", "kaka", "kaki", "pustakalaya"]
# print(len(stringArray))

# evenArray = []

# for x in range(len(stringArray)):
#     if   x%2 == 0:
#         evenArray.append(x)

# print(evenArray, "this is even array")

# print(stringArray)
# stringArray.insert(2,'test')
# print(stringArray)

# for index,value in enumerate(stringArray):

#     print(f"This is {index} index and value is {value}")

# WAP to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in 
# celsius and f = temperature in fahrenheit ]
    
    # let celsius value = 60C  answer 140F

    # formula f = (celsius * 9/5) + 32

# celsius = 60
# f = (celsius * 9/5) + 32

# print("Celsius to Fahrenheit:" ,f)
# def getCelciusFromUser():
#     print('i am function')

# getCelciusFromUser()

# ok = lambda x, y: x+y


# def sum(x,y):
#     return x + y
# printSUm  = sum(4,5)
# print(printSUm)
# print(ok(4,5))


# def outerFunction(x):
#     a = 2
#     def innerFunction(y):
#         return x+y+a
#     return innerFunction

# closure_instance = outerFunction(4)

# result = closure_instance(5)

# print("Result" , result)

# def divisionFunction(a,b):
#     try:
#         result = a/b
#         return result
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed")
#         return None
#     except Exception as e:
#         print(f"This is an error: {e}" )

# take a user input and pass it to the function parameters
        # to take input use input() function

# value_a = int(input('Enter the number to be divided :'))
# value_b = int(input('Enter the divident number:'))

# print(divisionFunction(value_a,value_b))





# WAP to find to and form celsius and farenheit 
# using function and input from user
# create both function celsiusToFarenheit and farenheitToCelsius
# formula f = (celsius * 9/5) + 32 
# formula c = (fahrenheit - 32) * 5/9

# def celsiusToFarenheit(celsius):
#      f = (celsius * 9/5) + 32 
#      return f

# def farenheitToCelsius(f):
#      c = (f - 32) * 5/9
#      return c

# choice  = bool(input("Choose Ture for celsius to farenheit and none for farenheit to celsius:"))

# if choice == True:
#     ferenheit =  celsiusToFarenheit(int(input("Enter the value of celsius:")))
#     print(ferenheit)
# else:
#     celsius = farenheitToCelsius(int(input("Enter the value of farenheit:")))
#     print(celsius)

async def getData():
    print("loading.")
    print("loading..")

    await asyncio.sleep(2)
    print('i am here after 2 second')

asyncio.run(getData())
print('la bhai le vaneko print')