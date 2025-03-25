# import random
# def quess_number():
#     number_to_quess=random.randint(1,100)
#     max_attempts=10
#     for attempts in range(max_attempts):
#         user=input(f"Введте число от 1 до 100(осталось попыток{max_attempts-attempts})")
#
#         if not user.isdigit():
#             print("Пожалуйста ведите число")
#             continue
#         user_quess=int(user)
#
#         if user_quess<number_to_quess:
#             print("Загаданное число больще")
#         elif user_quess>number_to_quess:
#             print("Загаданное число меньше")
#         else:
#             print(f"Поздравляем вы угадали")
#             break
#     else:
#         print(f'Вы не угадалиюЗагаданнще число было{ number_to_quess}.Пщпробуйте снова')
#
# quess_number()
'''
[выражения for element in cсписок if условия]
выражентя=что делать с каждым елементом


'''

# numbers=[x for x in range(5)]
# print(numbers)
# numbers=[]
# for x in range(5):
#     numbers.append(x)
# print(numbers)
#
# even_numbers=[x for x in range(10) if x%2==0]
# print(even_numbers)
# words=["apple","cherry","ananas","lemon"]
# short_words=[word.capitalize() for word in words]
# print(short_words)
# numbers=[x for x in range(100) if x%2==1]
# print(numbers)
# numbers=[x for x in range()]
# print(numbers)
words=["apple","elephant","tiger"]










