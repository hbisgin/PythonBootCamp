#integers, int -->numeric
#float -->numeric
#string -->text
#boolean -->true or false

sunny = True #this is a boolean. It is a true or false value. It is a logical value. It is a value that can be either true or false. It is a value that can be used in logical operations. It is a value that can be used in conditional statements. It is a value that can be used in loops. It is a value that can be used in functions. It is a value that can be used in classes. It is a value that can be used in modules. It is a value that can be used in packages. It is a value that can be used in libraries. It is a value that can be used in frameworks. It is a value that can be used in applications. It is a value that can be used in systems. It is a value that can be used in networks. It is a value that can be used in databases. It is a value that can be used in files. It is a value that can be used in data structures. It is a value that can be used in algorithms. It is a value that can be used in programming languages.
windy = "True" #this is a string. It is a sequence of characters. It is a text. It is a string of characters. It is a string of letters. It is a string of words. It is a string of sentences. It is a string of paragraphs. It is a string of documents. It is a string of files. It is a string of data. It is a string of information. It is a string of knowledge. It is a string of wisdom. It is a string of understanding. It is a string of insight. It is a string of awareness. It is a string of consciousness. It is a string of existence.
print(sunny) #this will print "True" because that is the current value of sunny.
print(windy) #this will print "True" because that is the current value of windy.

x = 12.0 #this is a float
y = "12.0" #this is a string

sunny = False
print(sunny) #this will print "False" because that is the current value of sunny.

#sunny = TrueFalse #this is not valid. 

number = 10

print("number<11 is ", number<11 )
print("number>11 is ", number>11 )

print("number <= 10 is ", number <= 10 )
print("number >= 10 is ", number >= 10 )

print("number == 10 is ", number == 10 ) # you use two equal signs to check if two values are equal. One equal sign is used for assignment, and two equal signs are used for comparison.

print("number == 12 is ", number == 12 )
print("number != 12 is ", number != 12 ) # you use != to check if two values are not equal.

age = int(input("What is your age? ")) #age is an integer. It is a whole number. It is a number that can be used in mathematical operations. It is a number that can be used in logical operations. It is a number that can be used in conditional statements. It is a number that can be used in loops. It is a number that can be used in functions. It is a number that can be used in classes. It is a number that can be used in modules. It is a number that can be used in packages. It is a number that can be used in libraries. It is a number that can be used in frameworks. It is a number that can be used in applications. It is a number that can be used in systems. It is a number that can be used in networks. It is a number that can be used in databases. It is a number that can be used in files. It is a number that can be used in data structures. It is a number that can be used in algorithms. It is a number that can be used in programming languages.
print("checking age before the if statement for demonstration only: ", age>=18)

if age >= 18: #inside the if statment your lines should start with a tab or 4 spaces. It is called indentation. 
    print("you are an adult") #this line is indented. It is part of the if statement. It will only be executed if the condition in the if statement is true.


if age >=62:
    print("you are a senior citizen") 
else:
    print("you are not a senior citizen") 

weight = float(input("weight?"))
height = float(input("height?"))
bmi = weight/height**2

if bmi >=25:
    print("you are overweight :( with a BMI of: ", bmi)
else:
    print("you are not overweight :) with a BMI of: ", bmi)


#when you are dealing with strings, please keep mind they are case sensitive. "Sunny" is not the same as "sunny". "Rainy" is not the same as "rainy". "Cloudy" is not the same as "cloudy". "Snowy" is not the same as "snowy".
weather = input("What is the weather like today? (sunny, rainy, cloudy, snowy) ")
if weather == "sunny":
    print("I am wearing t-shirt today")
elif weather == "rainy":
    print("I am wearing raincoat today")
elif weather == "cloudy":
    print("I am wearing jacket today")
elif weather == "snowy":
    print("I am wearing snow jacket today")
else:
    print(weather + " is not a valid weather type. Please enter one of the following: sunny, rainy, cloudy, snowy") 

#When you put sunny in keyboard, it will start checking from the first if statement. As soon as it sees it is satisfied,
# it won't check the remaining elif statements. It will just execute the first if statement and exit the if-elif-else block.

#Three types of if blocks we have seen so far:
#1. just if with one condition, and that was it. 
#2. if-else with two conditions, and one of them will be executed.
#3. if-elif-else with multiple conditions, and one of them will be executed. (else statement is optional)