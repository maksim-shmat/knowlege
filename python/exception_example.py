class MyError(Exception):
    pass

try:
    raise MyError("Some information \
about what went wrong")
except MyError as error:
    print("Situation:", error) 
try:
    raise MyError("Some information", "my_filename", 3)
except MyError as error:
    print("Situation: {0} with file {1}\n error code: {2}".format\
            (error.args[0],error.args[1],error.args[2]))
