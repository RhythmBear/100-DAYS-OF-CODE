# ----------------------------- First Class Functions --------------------------------------------#
# First class functions allows us to treat functions like any  other object i.e we can pass functioins as arguments
# return functions as outputs and we can assign functions as variables


# def my_app(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#
#     return result
#
#
# def square(x):
#     return x * x
#
#
# def cube(x):
#     return x * x * x
#
#
# test_list = [1, 2, 3, 4, 5]
#
# result_list = my_app(square, test_list)
# print(result_list)

# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#
#     return log_message
#
#
# log_hi = logger("hi!")
# log_hi()


# -------------------------------------------------- Closures ------------------------------------ #
# A Closure is a record storing a function a together with an environment: a mapping associating each free variable
# of the  function with the value or storage location to which the name was bound when the closure was crated.
# A closure, unlike a plain function, allows the function to access the captured variables through the closure's
# reference to them, even  when the function is invoked outside their scope

# def outer_function(msg):
#     message = msg
#
#     def inner_function():
#         print(message)
#
#     return inner_function
#
#
# hi_func = outer_function('hi')
# hello_func = outer_function('hello')

#
# import logging
# logging.basicConfig(filename='example.log', level=logging.INFO)
#
#
# def logger(func):
#
#     def log_func(*args):
#         logging.info('Running "{}" with arguments {}'.format(func, __name__, args))
#         print(func(*args))
#
#     return log_func
#
#
# def add(x, y):
#     return x+y
#
#
# def sub(x, y):
#     return x-y
#
#
# add_logger = logger(add)
# sub_logger = logger(sub)
#
# add_logger(3, 3)
# add_logger(4, 5)
#
# sub_logger(10, 5)
# sub_logger(20, 10)

# ------------------------------------ Python Decorators ------------------------------------------------ #
# A decorator is a function that takes another function as an argument adds an extra functionality to
# the function and returns another function without altering the original source code of the original function passed in


def decorator_function(original_func):

    def wrapper_function(*args, **kwargs):
        return original_func(*args, **kwargs)

    return wrapper_function


@decorator_function
def display(name, age):
    print(f"Display ran with arguments {name} and {age}")


display("sham", '31')
