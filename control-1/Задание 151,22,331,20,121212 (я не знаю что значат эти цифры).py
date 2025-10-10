#a = int(input("Введите первое число:"))
#b = int(input("Введите второе число:"))
#c = a + b
#d = a - b
#e = a * b
#print("Сумма первого и второго числа = ", c)
#print("Разность первого и второго числа = ", d)
#print("Произведение первого и второго числа = ", e)
#if b == 0:
#    print("Ноу ноу ноу мистер фиш, на ноль делить нельзя")
#else:
#    f = a / b
#    print("Частное первого и второго числа = ", f)


#a = int(input("Введите ваш возраст:"))
#b = input("Есть ли медицинская справка? (да/нет):")
#if a > 18 and b == "да":
#    print("Можно получить права")
#elif a < 18 and b == "да":
#    print("Слишком молод для получения прав")
#elif a > 18 and b == "нет":
#    print("Нужна медицинская справка")
#elif a == 18:
#    print("Приди завтра с медецинской справкой")
#else:
#    print("Нахрен ты сюда пришел если ты не соблюдаешь ни одно из условий")


#n = int(input("Введите целое число: "))  
#  
#
#shift_left = n << 2
#shift_right = n >> 1
#bitwise_and = n & 15  
#bitwise_or = n | 3   
#  
#print("Исходное число:", n, "(", bin(n), ")")
#print("Сдвиг влево на 2 бита:", shift_left, "(", bin(shift_left), ")")  
#print("Сдвиг вправо на 1 бит:", shift_right, "(", bin(shift_right), ")")
#print("Побитовое И с 15:", bitwise_and, "(", bin(bitwise_and), ")") 
#print("Побитовое ИЛИ с 3:", bitwise_or, "(", bin(bitwise_or), ")")

#x = int(input("Введите первое число:")) 
#y = int(input("Введите второе число:")) 
#operation = input("Введите операцию (+, -, *, /, %, //):") 
#if(operation == "+"): 
#    print(x+y) 
#elif(operation == "-"): 
#    print(x-y) 
#elif(operation == "*"): 
#    print(x*y) 
#elif(operation == "/") and y != 0 or x != 0: 
#    print(x/y) 
#elif(operation == "//") and x != float or y != float: 
#    print(x//y)
#elif(operation == "%") and x != float or y != float: 
#    print(x % y)
#else:
#    print("Неизвестная Операция")




def check_password_strength(password):  

    length_ok = len(password) >= 8  
       
    has_digit = any(char.isdigit() for char in password)  
       
    has_upper = any(char.isupper() for char in password)  
        
    has_lower = any(char.islower() for char in password)  
      
    special_chars = "!@#$%^&*"  
    has_special = any(char in special_chars for char in password)  
      
    print("\nПроверка пароля:")  
    print(f"Длина >= 8 символов: {'Да' if length_ok else 'Нет'}")  
    print(f"Содержит цифру: {'Да' if has_digit else 'Нет'}")  
    print(f"Содержит заглавную букву: {'Да' if has_upper else 'Нет'}")  
    print(f"Содержит строчную букву: {'Да' if has_lower else 'Нет'}")  
    print(f"Содержит спецсимвол: {'Да' if has_special else 'Нет'}")  
      
    if length_ok and has_digit and has_upper and has_lower and has_special:  
        print("\nПароль надежен")  
    else:  
        print("\nПароль ненадежен")  
  
  
password = input("Введите пароль для проверки: ")  
check_password_strength(password)
