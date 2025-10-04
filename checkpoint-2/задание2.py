#a = int(input("Какой у вас год рождения?"))
#a = 2024 - a
#print("Вам сейчас:", a)
#print("Через 10 лет вам будет:", a + 10)

#a = int(input())
#b = a % 2
#if b == 1:
#    print("Щит неактивен")
#else:
#    print("Щит активен")

#a = int(input())
#b = 2
#d = 1
#c = a << b
#e = a >> d
#print("Исходные координаты:", a)
#print("Исходное число", a)
#print("Побитовый  сдвиг вправо на 2 (a<<2)", c)
#print("Побитовый  сдвиг влево на 1 (a>>1)", e)

registervalue = int(input("Введите значение системного регистра: "))  
   
bitnumber = int(input("Введите номер бита для проверки: "))  
  
n = 1 << bitnumber

if registervalue & n:
    print(f"Бит {bitnumber} установлен (1)") 
else:  
    print(f"Бит {bitnumber} сброшен (0)")
