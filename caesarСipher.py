import sys
import msvcrt as m


def containsDecimal(my_str):
    decimal = False
    for i in range(len(my_str)):
        if my_str[i].isdecimal():
            decimal = True
    return decimal


alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
programOutput = ""
userInput = input("Введите исходную строку:")
if containsDecimal(userInput):
    print("Строка содержит числа, перезапустите программу")
    m.getch()
    sys.exit()
n = input("Введите шаг сдвига:")
try:
    n = int(n)
except Exception:
    print("Невозможно выполнить программу")
    m.getch()
    sys.exit()
for i in range(len(userInput)):
    if userInput[i].isupper():
        for j in range(len(alphabet_upper)):
            if userInput[i] == alphabet_upper[j]:
                programOutput += alphabet_upper[(j + n) % 33]
    elif userInput[i].islower():
        for j in range(len(alphabet_lower)):
            if userInput[i] == alphabet_lower[j]:
                programOutput += alphabet_lower[(j + n) % 33]
    elif userInput[i].isspace():
        programOutput += ' '
print("Преобразованная строка:", programOutput)
m.getch()
sys.exit()