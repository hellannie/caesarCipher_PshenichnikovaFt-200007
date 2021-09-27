import sys
import msvcrt as m

cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
latin_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
latin_lower = 'abcdefghijklmnopqrstuvwxyz'
programOutput = str()
otherProgramOutput = str()

def caesarCipher(my_str, n, alphabet_upper, alphabet_lower, defOutput):
    for i in range(len(my_str)):
        if my_str[i].isupper():
            for j in range(len(alphabet_upper)):
                if my_str[i] == alphabet_upper[j]:
                    defOutput += alphabet_upper[(j + n) % len(alphabet_upper)]
        elif my_str[i].islower():
            for j in range(len(alphabet_lower)):
                if my_str[i] == alphabet_lower[j]:
                    defOutput += alphabet_lower[(j + n) % len(alphabet_lower)]
        elif not my_str[i].isalpha():
            defOutput += my_str[i]
    return defOutput

userInput = input("Введите исходную строку:")
n = input("Введите шаг сдвига, выраженное целым числом:")
try:
    n = int(n)
except Exception:
    print("Невозможно выполнить программу")
    m.getch()
    sys.exit()
if n == 0:
    print("Преобразованная строка равна исходной, так как шаг сдвига равен нулю.")
    m.getch()
    sys.exit()
lang_pref = int(input("Выберите язык строки: 1 - Русский, 2 - Английский: "))
try:
    lang_pref = int(lang_pref)
except Exception:
    print("Невозможно выполнить программу")
    m.getch()
    sys.exit()
if (lang_pref == 1) or (lang_pref == 2):
    if (lang_pref == 1):
        programOutput = caesarCipher(userInput,n,cyrillic_upper,cyrillic_lower,programOutput)
    elif (lang_pref == 2):
        programOutput = caesarCipher(userInput,n,latin_upper,latin_lower,programOutput)
    if len(programOutput) != len(userInput):
        print("Язык выбран некорректно")
        if (lang_pref == 1):
            otherProgramOutput = caesarCipher(userInput,n,latin_upper,latin_lower,otherProgramOutput)
        elif (lang_pref == 2):
            otherProgramOutput = caesarCipher(userInput,n,cyrillic_upper,cyrillic_lower,otherProgramOutput)
        print("Преобразованная строка:", otherProgramOutput)
        m.getch()
        sys.exit()
    else:
        print("Преобразованная строка:", programOutput)
        m.getch()
        sys.exit()
else:
    print("Неправильный выбор языка, перезапустите программу")
    m.getch()
    sys.exit()
