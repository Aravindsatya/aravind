class parent:  #define parent class
    parentattr=100

    def __init__(self):
        print("calling parent constructor")

    def parentmethod(self):
        print('calling parent method')

    def setattr(self,attr):
        parent.parentattr=attr

    def getattr(self,attr):
        parent.parentattr=attr

    def getattr(self):
        print('parent attribute"',parent.parentattr)

class child(parent): #define child class
    def __init__(self):
        print("calling child constructor")
    def childmethod(self):
        print('calling child method')
c=child() #instance of child
c.childmethod()
c.parentmethod()
c.setattr(200)
c.getattr()
