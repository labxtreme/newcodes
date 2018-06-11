class person:

    """This is the person class"""
    
    def __init__(self,name,height,age,weight=None,blood_group=None):
        self.name=name
        self.height=height
        self.age=age
        self.weight=weight
        self.blood_group=blood_group

    def show(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("weight = ",self.weight)
        print("Height = ",self.height)
        print("Blood group = ",self.blood_group)

    def change(self,name):
        self.name = name

person1=person('Lakshaya Bathla',5.10,20,90,'B+')
person2=person('python',8,27)

person1.show()
print()
person2.show()
print()
