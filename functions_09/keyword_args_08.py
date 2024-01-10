# example : Variable length keyword argument
# *kwargs in Python (non Keyword Arguments)

def shopping_func(**shopping_kwargs):
    for key, value in shopping_kwargs.items():
        print(key, value)


shopping_func(Tea= 30.0, eggs=120.0, bread='10.0')