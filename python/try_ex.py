"""Use try about."""

#1

def try_syntax(numenator, denominator):
    try:
        print(f'In the try block: {numenator}/{denominator}')
        result = numenator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')

print(try_syntax(12, 4))
print(try_syntax(11, 0))


In the try block: 12/4
The result is: 3.0
Exiting
3.0
In the try block: 11/0
division by zero
Exiting
None
