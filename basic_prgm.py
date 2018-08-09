class employee:
    'common base class for all employees'
    empcnt=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcnt +=1

    def displaycnt(self):
        print("total employee %d:" % employee.empcnt)

    def displayemployee(self):
        print("Name:",self.name,"salary:",self.salary)


"first object of employee class"
emp1=employee("ARAVIND",20000)
"second object"
emp2=employee("jaya",25000)
emp1.displayemployee()
emp2.displayemployee()

print("total employee %d:" % employee.empcnt)


print("employee.__doc__",employee.__doc__)
print("employee.__name__",employee.__name__)
print("employee.__module__",employee.__dict__)
print("employee.__bases__",employee.__bases__)
print("employee.__dict__",employee.__dict__)
