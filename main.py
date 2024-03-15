def calculation(x, y, operator):
    try:

        if operator == '+':
            total = x + y
            return total
        elif operator =='-':
            total = x - y
            return total
        elif operator == 'x':
            total = x * y
            return total
        elif operator == '/':
            total = x / y
            return total
    except ZeroDivisionError:
        print("You cannot divide by zero...")


num1 = float(input("Please enter your first number:  ")) 
num2 = float(input("Please enter your second number: "))  

ops = ['+', '-', '/', 'x']
while True:
    operator = input("Enter the math symbol you would want to use in your calculation: ")
    if operator not in ops:
        print('''Your selected symbol is not valid.
             Please use one of the following symbols:
            +(addition), - (subtraction), / (division), x(multiplication)
          ''')
        continue
    else:
        print('Calculating...')
        break
calc = calculation(num1, num2, operator)
print(calc)


