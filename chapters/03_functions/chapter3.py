def cristiano():
    print("Full of ego!")

cristiano()


def greet(name):
    print("Hello " + name + "!")

greet("Cristiano")


def repeat(word,n):
    print(word *n)

repeat("Cristiano ", 3)

for i in range (5):
    print("Cristiano ")

for i in range (5):
    repeat("Cristiano ", 3)

#3.11.1
def repeat(text, number):
    for i in range(number):
        print(text)

repeat("Hello", 3)

# same but wihtout for loop
def repeat(text, number):
    print((text + "\n") * number, end="")

repeat("Hello", 3)

#3.11.2
def print_right(text):
    spaces = 40 - len(text)
    print(" " * spaces + text)

print_right("Hello")

#3.11.3
def triangle(text, height):
    for level in range(1, height + 1):
        print(text * level)

triangle("L", 5)

#3.11.4
def rectangle(text, width, height):
    for row in range(height):
        print(text * width)

rectangle("H", 5, 4)

#3.11.5
def bottle_line(number, ending):
    print(number, "bottles of beer" + ending)

def bottle_verse(number):
    bottle_line(number, " on the wall")
    bottle_line(number, "")
    print("Take one down, pass it around")
    bottle_line(number - 1, " on the wall")

bottle_verse(99)