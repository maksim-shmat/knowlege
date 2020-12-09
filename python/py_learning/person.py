class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def tax(self):
        return self.pay * 0.25

    def info(self):
        return self.name, self.job, self.pay, self.tax()

# save data for persons
>from person import Person
>bob = Person('bob', 'psychologist', 70000)
emily = Person('email', 'teacher', 40000)
>
>import shelve
>dbase = shelve.open('cast')
>for obj in (bob, emily):
    dbase[obj.name] = obj
>dbase.close()


>>import shelve
>>dbase = shelve.open('cast')

>>list(dbase.keys())
>>print(dbase['emily'])
>>print(dbase['bob'].tax())
