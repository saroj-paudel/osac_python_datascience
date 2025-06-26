# def hello():
#     print("Hello")

# hello()


# def greet(name):
#     print(f"Hello {name}")

# greet("Saroj")


# def sum(a=5,b=7):
#     return a+b

# print(sum(2,2))
# print(sum())
# sum (a=5)


# lambda function -> anonymous

# f = lambda a:a*a

# x = lambda a :a + 10
# print(x(5))


# x = lambda a,b :a + b
# print(x(5,3))


def outer():
    message = "local"
    def inner():
        nonlocal message
        message = "nonlocal"
        print("Inner",message)
    inner()
    print("Outer",message)

outer()