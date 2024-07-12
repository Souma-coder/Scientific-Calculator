# this is the origin file, from here everything starts

import valueOperations as vo
import mainOperations as mo

print("Welcome to python calculator")
print(" __________________________")
print("| ------------------------ |")
print("| |                      | |")
print("| ------------------------ |")
print("|                          |")
print("|  | 1 |   | 2 |   | 3 |   |")
print("|                          |")
print("|  | 4 |   | 5 |   | 6 |   |")
print("|                          |")
print("|  | 7 |   | 8 |   | 9 |   |")
print("|                          |")
print("|  | . |   | 0 |   | + |   |")
print("|                          |")
print("|  | - |   | x |   | / |   |")
print("|                          |")
print(" --------------------------")

n1 = vo.takeInput()

mo.mainFunction(n1)
