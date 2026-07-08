# Q1
print("Fathima Rafna K" )
# Q2
from datetime import date
today = date.today()
print("Today's date is:", today)
# Q3
city = "Kochi"
print("I live in", city)
# Q4
length = 20
width = 10
area = length * width
print("Area of Rectangle:",area)
# Q5 
age = int(input("Enter your age: "))
print("Your age is:", age)

# Q6
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print("Sum =", sum_result)

# Q7
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100
print("Simple Interest =", si)

# Q8 
a = 10          # int
b = 3.5         # float
c = "Python"    # string
d = True        # bool

print(a)
print(b)
print(c)
print(d)
# Q9
num = float(input("Enter a decimal number: "))
print("The data type is:", type(num))
#Q10
num = 45
num_float = float(num)

print(num_float)
print(type(num_float))
#Q11
num = 45
num_float = float(num)

print(num_float)
print(type(num_float))
#Q12
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
n5 = float(input("Enter fifth number: "))

average = (n1 + n2 + n3 + n4 + n5) / 5
print("Average =", average)
#Q13
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)
print("Perimeter =", perimeter)
#Q14
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)
#Q15
km = float(input("Enter distance in kilometers: "))

meters = km * 1000
print("Distance in meters =", meters)
#Q16
name = input("Enter your full name: ")
print("Uppercase:", name.upper())
#Q17
word = input("Enter a word: ")
print("First character:", word[0])
#Q18
word = input("Enter a word: ")
print("Last character:", word[-1])
#Q19
a = "Python"
b = "Programming"

sentence = a + " " + b
print(sentence)
#Q20
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#Q21
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

#Q22
mark = int(input("Enter mark: "))

if 90 <= mark <= 100:
    print("Grade A")
elif 80 <= mark <= 89:
    print("Grade B")
elif 70 <= mark <= 79:
    print("Grade C")
else:
    print("Grade D")

#Q23
ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
#Q24         
1
22
333
4444
55555
#Q25
def count_vowels(word):
    count = 0
    for ch in word.lower():
        if ch in "aeiou":
            count += 1
    return count

word = input("Enter a word: ")
print("Number of vowels =", count_vowels(word))
