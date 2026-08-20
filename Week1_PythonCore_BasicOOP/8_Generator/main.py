##1
# def even_number_list(n):
#     result = []
#     for i in range(n):
#         if i%2 == 0:
#             result.append(i)
#     return result
# if __name__ == "__main__":
#     print(even_number_list(10))


# def even_number(n):
#     print("Bat dau")
#     for i in range(n):
#         if i%2 == 0:
#             print(f"--> chuan bi nha {i}")
#             yield i
# gen = even_number(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))



# # List comprehension: tao NGAY mot list trong RAM
# evens_list = [i for i in range(10) if i % 2 == 0]

# # Generator expression: lazy, khong ton RAM
# evens_gen = (i for i in range(10) if i % 2 == 0)

# print(evens_list)        # [0, 2, 4, 6, 8]
# print(evens_gen)         # <generator object ...>
# print(list(evens_gen))   # [0, 2, 4, 6, 8]


# ##Pipeline mini
# from itertools import islice

# #Source
# def even_infinite():
#     num = 0
#     while True:
#         yield num
#         num += 2

# #Transform
# def square(source):
#     for value in source:
#         yield value * value

# #Load
# pipeline = square(even_infinite())

# print(list(islice(pipeline, 10)))


# def even_number(n):
#     for i in range(n-1):
#         if i%2 == 0:
#             yield i

# print(list(even_number(10)))

experssion = sum(i for i in range(999) if i % 2  == 0 )

print(experssion)