#Функция декоратор (is_prime), которая распечатывает
# "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.

def is_prime(func):
    def is_simple(*args):
        number = func(*args)
        for num in range(2,number-1):
            if number % num == 0:
                print('Составное')
                return number

        print('Простое')
        return number
    return is_simple

# Функция, которая складывает 3 числа (sum_three)
@is_prime
def sum_three(*args):
    result = 0
    for arg in args:
        result += arg
    return result

result = sum_three(2, 3, 6)
print(result)