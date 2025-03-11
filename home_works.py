# print(*res
#n=int(input())
# res=[f"{i}**2={i**2}" for i in range(1,n+1) ]
# print(res)
# res=[f'{n}*{i}={n*i}' for i in range(1,11) if n<10]
# print(res)
# res=[i for i in range(1,int(input())+1) if i%2==0]
# print(res)
res=[i for i in range(1,int(input())+1) if i%3==0 and i%5==0]
print(*res)


