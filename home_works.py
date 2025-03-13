n=[i for i in range(1,21) if i%2==0]
print(*n)
m=[i**2 for i in range(1,11)]
print(*m)
b=[5,12,7,18,3,10,8]
res=(i for i in b if i>7)
print(*res)
#word=["apple","banana","cherry"]
#print(word.upper()
print("polojitelnoe" if int(input())>0 else "otrisatelnoe")
print("jup" if int(input())%2==0 else "tak")
a=[4.-1,7,-3,0,9]
b=[i if i>=0 else 0 for i in a]
print(*b)


