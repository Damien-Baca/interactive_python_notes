# def f(a, *b, **c):
#     print(f'a={a}')
#     if len(b):
#         print(f'b:')
#         for arg in b:
#             print(arg)
#     if len(c):
#         for kw in c:
#             print(kw, ":", c[kw])


# def bar(a: str, /, *b: str) -> str:
#     """A test function"""
#     print(a)
#     for arg in b:
#         print(arg)
#     return 'Noob'


# bar('Dog', 'Sam')


# def pick(*, dog=None, cat=None, snake=None):
#     if dog:
#         print(f'{dog} is such a good boy!')
#     if cat:
#         print(f'{cat} is such a good kitty!')
#     if snake:
#         print(f'{snake} is such a precious danger noodle!')


# pick(cat='Sebastian', snake='Amy')


# def foo(name, **kwds):
#     return 'name' in kwds


# # def concat(*args, sep='/'):
# #     return sep.join(args)

# def make_func(n):
#     return lambda x: x + n


# print(make_func(10)(10))


# vec = [[1, 2, 3], [4, 5, 6]]
# print([x for elem in vec for x in elem])

# cart = dict(fruit='strawberry', pasta='elbow', bread='french')
# for a, b in cart.items():
#     print(a)
#     print(b)

# order = ['snake', 'cat', 'dog']
# print(list(enumerate(order)))
# print(dict(enumerate(order)))


# str1, str2, str3 = 'Dog', 'Cat', 'Snake'
# non_null = str1 and str2 and str3
# print(non_null)

# fp = open('iterate.txt')
# while chunk := fp.read(200):
#     print(chunk)
