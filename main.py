from bank_operations.bank import credit, debit, transfer



class Fruits:
    def  __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def say_color(self):
        print("My color is", self.color)

class Apple(Fruits):
    def my_type(self):
        print("I am an apple..")

    def say_color(self):
        print("I am red in color")  


a = Apple("Apple1", "red")

print(a.color)