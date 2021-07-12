"""Args and kwargs about."""

def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

if __name__ == "__main__":
    sum = addition(2, 5, 1, 9)
    print(sum)

    sum = addition(5)
    print(sum)

    sum = addition(5, 4, 0.5, 1.5, 9, 2)
    print(sum)

###### args in *args is just a name

def addition(*cupos):
    result = 0
    for cupo in cupos:
        result += cupo
    return result

if __name__ == "__main__":
    sum = addition(2, 5, 1, 9)
    print(sum)

###### args in *args is a tuple

def addition(*numbers):
    print(type(numbers))

if __name__ == "__main__":
    addition(2, 5, 1, 9)

###### *args with other parameters

def calculator(operation, *numbers):
    if operation == "add":
        result = 0
        for num in numbers:
            result += num
        return result

    if operation == "product":
        result = 1
        for num in numbers:
            result *= num
        return result

if __name__ == "__main__":
    x = calculator("add", 2, 5, 1, 9)
    print(x)
    x = calculator("product", 3, 5, 2)
    print(x)

###### *args with **kwargs

def myFunction(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__ == "__main__":
    myFunction("hello", "mars", a = 24, b = 87, c = 3, d = 46)

######
