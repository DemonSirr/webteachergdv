def diskr(a, b, c):
       d = (b**2) - (4*a*c)
    if d < 0:
        print("Дискриминант < 0, корней нет.")
        return
    elif d == 0:
        x = (-b) / (2*a)
        print("Корень уравнения x =", x)
        return
    else:
        x1 = ((-b) + (d**0.5)) / (2*a)
        x2 = ((-b) - (d**0.5)) / (2*a)
        print("Корни уравнения x1 =", x1, "x2 =", x2)
        return

def viet(b, c, limit=1000):
    for x1 in range(-limit, limit + 1):
        for x2 in range(-limit, limit + 1):
            if x1 + x2 == -b and x1 * x2 == c:
                print("Корни уравнения x1 =", x1, "x2 =", x2)
                return x1, x2
    print("Корни не найдены в заданном диапазоне.")
    return None
  
while True:
    print("\n Вычисление квадратного уравнения: введите коэффициенты a, b, c:")
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
    except ValueError:
        print("Пожалуйста, вводите целые числа.")
        continue

    if a == 0:
        print("Коэффициент 'a' не может быть равен 0 (это не квадратное уравнение).")
        continue

    command = int(input("Метод решения: 1 - через дискриминант, 2 - через теорему Виета: "))

    if command == 1:
        diskr(a, b, c)
    elif command == 2:
        viet(b, c)
    else:
        print("Неверная команда")
    
    cont = input("Продолжить? (да/нет): ")
    if cont.lower() != 'да':
        break
