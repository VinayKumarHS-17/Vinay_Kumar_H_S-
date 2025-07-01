class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            return self.a / self.b if self.b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"


calc = Calculator(10.5, 2.0)
print(calc.operate('add'))      
print(calc.operate('subtract'))      
print(calc.operate('multiply'))  
print(calc.operate('divide'))  