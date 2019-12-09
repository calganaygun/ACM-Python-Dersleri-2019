# def merhaba():
#     print("Hosgeldiniz.")
# merhaba()

# a = 5
# def yazdir():
#     global a
#     print(a)
# 
# a = 5
# yazdir()
# def ciftmi(a):
#     if a%2 == 0:
#         print("Evet")
#     else:
#         print("Hayir")
# b=6
# ciftmi(b)

# 
# 
# fibonacci(3)
# 
# 
# 1,1,2


# def fonksiyon(*parametreler):
#     print(parametreler)
# 

# def fibonacci(a):
#     liste = [1,1]
#     for i in range(a-2):
#         liste.append(liste[-1]+liste[-2])
#     for l in liste:
#         print(str(l)+",",end="")
# fibonacci(3)
# def fib(a):
#     liste = [1,1]
#     for i in range(a-2):
#         liste.append(liste[-1]+liste[-2])
# #     for l in liste:
# #         print(str(l),end=",")
#     print(*liste,sep=",")
# fib(3)

def yanyanayazdir(*argumanlar):
    print(*argumanlar,sep="")

yanyanayazdir(1,2,2,5,6,7)








