import math
# Multiplication : Question 1
a= 5
b= 10
c= 7

a += 3
b *= 2
c %= 4
print ( a , b ,c )

# varaibles 
square = a**2 + b**2 + c**2

#variable
square_root = math.sqrt (square) 
rounded = round(square_root, 2)

print(rounded)

# Question 2: Complex Conditional Evaluation

#integars
x = 5
y = 7
z = 20

#Conditions
is_even = x %2== 0
is_positive = y>0
is_in_range = z > 10 and z < 50 

final_condition =  is_even and is_positive and is_in_range
print(final_condition)


# Question 3: Grading with Adjustments

user_score = 70
bonus_points = 5
late_penalty = -10
final_score = 100 < 0

score = max(0 , min(final_score,165))

if score >= 60:
    grade = "a"

elif score >= 75:
    grade = "b"

elif score >= 45:
    grade = "c"

elif  score >= 10:
    grade = "d"


else : 
    score >= 15 
    grade = "f"

print("Final score:", score)
print("Grade:", grade)

# Question 4: Advanced Calculator
num1 = 15
num2 = 0
input_operation = input("Choose an operation (+, -, *, /, %, **): ")

try : 

    if input_operation == "+" :
        result = num1 + num2 
    elif input_operation == "-" :
        result = num1 - num2
    elif input_operation == "*" :
        result = num1 * num2
    elif input_operation == "/" :
        result = num1 / num2
    elif input_operation == "%" :
        if num2 != 0:
            result = num1 % num2
        else:
            raise(ZeroDivisionError("cannot divide by zero"))
        
    elif input_operation == "**" :
        result = num1 ** num2
    else : 
        print("invalid operation!")
        result = None
    if result is not None :
        print("result:" , result)  
except ZeroDivisionError as e:
    print(e)  