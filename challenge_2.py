


class Calculator:

    def __init__(self,Num1,Num2):
        self.Num1=Num1
        self.Num2=Num2

    def add(self):
         return self.Num1+self.Num2
    def subtract(self):
        return self.Num1-self.Num2
    def multiply(self):
        return self.Num1*self.Num2
    def divide(self):
        return self.Num1/self.Num2

Calculator_obj=Calculator(Num1=10,Num2=5)
print(Calculator_obj.add() )
print(Calculator_obj.subtract())
print(Calculator_obj.multiply())
print(Calculator_obj.divide())