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
#lambda аргумен: выражения
# lambda a,b :a+b
# def add(a,b):
#     return a+b
# squera=lambda a,b: a+b
# print(squera(3,5))
#
# string_func=lambda a: a
# print(string_func("hello word"))
#
# greating= lambda: "hello"
# print(greating())
#
# numbers=[1,2,3,4,5]
# squared=list(map(lambda x: x**2,numbers))
# print(squared)
#
# numbers_1=[23,45,67]
# summ=list(map(lambda x: x+1,numbers_1 ))
# print(summ)

# numbers=[10,15,20,25]
# filtered=list(filter(lambda x: x%2==0,numbers))
# print(filtered)


# length= lambda a :len(a)
# print(length("python"))
# numbers=[1,2,3,4,5]
# result=list(map(lambda x: x*3,numbers))
# print(result)


# words=["work","different","antony"]
# filtered_words=list(filter(lambda a: len(a)>5,words ))
# print(filtered_words)
# words=["apple","ananas","banan",]
# sorted_word=sorted(words,key=lambda a: len(a))
# print(sorted_word)




