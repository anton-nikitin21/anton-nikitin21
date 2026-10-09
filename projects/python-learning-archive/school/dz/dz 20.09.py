# from tkinter import*

# root = Tk()

# root['bg'] = '#fafafa'
# root.title('ToxaC')
# root.wm_attributes('-alpha',1)
# root.geometry('300x250')

# root.resizable(width=False, height=0)

# canvas = Canvas(root, height=300, width=250)
# canvas.pack()



# root.mainloop()




# print('s')

# import pandas as pd

# all_data = [1.7, 0.5, None]
# data_sum = pd.Series(all_data).sum(skipna=None)
# print(data_sum)

# i = 5 
# k=0
# while i <= 11: 
#     k+=1
#     print('Python awesome!')
#     print(k)
#     i += 1

# a=[]
# for n in range(500):
#     for k in range(500):
#         for m in range(500):
#             if 28*n+30*k+31*m==365:
#                a.append(n*k*m) 
#                print(max(a),n, k, m)



# solution=[]
# for bulls in range(0,11):
#     for cows in range(0,21):
#         calves = 100 - bulls - cows
#         if 10*bulls+5*cows+0.5*calves == 100:
#             product= bulls*cows*calves
#             solution.append(product)
#             print(product,bulls,cows,calves)




# for a in range(1,160):
#     a=a**5
#     for b in range(1,165):
#         b=b**5
#         for c in range(1,165):
#             c=c**5
#             for d in range(1,165):
#                 d=d**5
#                 for e in range(1,165):
#                     e=e**5
#                     if a+b+c+d==e:
#                         print(a+b+c+d+e)
#                         print('daun')


# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# print('ввод закончен-')
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# y=int(input())

# for i in range(0,x)

# a = 7
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#     p = (a + b) * (a + b)
# print(p)

# a = input()
# if '@' in a and '.' in a:
#     print("YES")
# else:
#     print("NO")
# k=0
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# # for i in s:
# #     k+=1
# #     if k%7==0:
# #         print(i)
# # print(s[::7])
# print(s[::-1])

# a = input()
# if a.istitle():
#     print('YES')
# else:  
#     print('NO')

# s = input()                  
# k = 0                        
# for i in range(len(s)):      
#     ???
#         k+=1              
# print(k) 

# n=input()
# k=0
# k=n.count(' ')+1
# print(k)
# n = input()
# a=n.split()
# print(a[1])

# s = input()
   
# print(s[:(s.find('h'))] + s[(s.rfind('h'))+1:])  


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
# print(primes[-1])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# a=max(numbers)
# b=min(numbers)
# print(a,b,a+b)
# print(max(numbers)+min(numbers))

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(sum(evens)/len(evens))

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[rainbow.index('Green')]='Зеленый'
# print(rainbow)

# n = int(input())
# sd = []
# for _ in range(n):
#     sd.append(_**3)
# print(sd)
# sum=0
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for i in numbers:
#     sum+= i**2
#     print(sum)

# names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur', 'Dima', 'Paul', 'Dima']
# print(names.count(input()))

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(d) for d in keywords]
# print(lengths)


# print(*[i**2 for i in range(1,int(input())+1)], sep='\n')

# from itertools import*

# digits = '123456789'
# operators = ['+', '-', '']  # возможные "операторы" между цифрами
# count = 0  # счетчик выражений, дающих 100

# # Перебираем все комбинации из 8 мест
# for ops in product(operators, repeat=8):
#     x = ''.join(d + o for d, o in zip(digits, ops + ('',)))  # формируем выражение
#     if eval(x) == 100:  # вычисляем выражение
#         count += 1

# print(count)


# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# n=input()
# print(len(n.split(' ')))


# a = (1, 2, 3, 4, 5)
# print(a)


# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# languages = ('Python', 'C++', 'Java')
# print(*numbers)
# print(*languages, sep='\n')


# import datetime
# today=datetime.datetime.today()

#     print( today.strftime("%H.%M.%S"))