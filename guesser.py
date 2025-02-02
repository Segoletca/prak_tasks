from random import randint

shadow_int: int = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input("Какое число загадано?\n-> "))
    if guess == shadow_int:
        print('Отличная интуиция! Вы угадали число :)')
        break
    elif guess < shadow_int:
        print('Ваше число меньше того, что загадано')
    else:
        print('Ваше число больше того, что загадано')


def fun():
    pass
