import numpy as np

#Zad 1
# a=np.arange(3)
# b=np.arange(3)
#
# print(a*b)

# Zad2
# a=np.arange(9).reshape(3,3)
# b=np.arange(16).reshape(4,4)
# def mala(a):
#     answer = "Najmniejsze wartości w poszczególnych rzędach macierzy to: \n"
#     for x in a:
#         answer+= str(np.amin(x)) + "\n"
#     a = a.T
#     answer+="Najmniejsze wartości w poszczególnych kolumnach macierzy to: \n"
#     for y in a:
#         answer+=str(np.amin(y)) + "\n"
#     return answer
#
# print(mala(a))
# print(mala(b))


# Zad3
# a=np.arange(3)
# b=np.arange(3)
# print(a.dot(b))

# Zad4

# a=np.ones(3, dtype="int32")
# b=np.linspace(0,3.14,3)
# print(a)
# print(b)
# print(a.dot(b))


# Zad5

# a=np.arange(6).reshape(2,3)
# b=np.sin(a)
# print(b)

# Zad6
#
# a=np.arange(6).reshape(2,3)
# b=np.cos(a)
# print(b)

# Zad7

# def dodawanie(a, b):
#     if a.shape == b.shape:
#         sum = np.add(a, b)
#         print(sum)
#     else :
#         print("zle")
#
# a=np.arange(6).reshape(2,3)
# b=np.arange(6).reshape(2,3)
# dodawanie(a,b)

# Zad8
#
# a = np.arange(9).reshape(3,3)
# for x in a:
#     print(x)
#     print(" ")
#
# Zad9
# a = np.arange(9).reshape(3,3)
# for x in a.flat:
#     print(x)
# Zad10
# a=np.arange(81).reshape(9,9)
# print(a)
# # 1x81 oraz 81x1
# print(a.reshape(1,81))
# # 3x27 oraz 27x3
# print(a.reshape(3, 27))
