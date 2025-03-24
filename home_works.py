import random
def quess_number():
    number_to_quess=random.randint(1,100)
    max_attempts=10
    for attempts in range(max_attempts):
        user=input(f"Введте число от 1 до 100(осталось попыток{max_attempts-attempts})")

        if not user.isdigit():
            print("Пожалуйста ведите число")
            continue
        user_quess=int(user)

        if user_quess<number_to_quess:
            print("Загаданное число больще")
        elif user_quess>number_to_quess:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляем вы угадали")
            break
    else:
        print(f'Вы не угадалиюЗагаданнще число было{ number_to_quess}.Пщпробуйте снова')

quess_number()












