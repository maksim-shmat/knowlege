"""Decorate, sort and undecorate."""

students = [
        dict(id=0, credits=dict(math=9, phisics=6, history=7)),
        dict(id=1, credits=dict(math=6, phisics=6, latin=10)),
        dict(id=2, credits=dict(history=8, phisics=9, chemistry=10)),
        dict(id=3, credits=dict(math=5, phisics=5, geography=7)),
]

def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]

students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))

Traceback (most recent call last):
  File "/home/jack/django2/knowlege/python/students_count.py", line 18, in <module>
    students = sorted(map(decorate, students), reverse=True)
TypeError: '<' not supported between instances of 'dict' and 'dict'
