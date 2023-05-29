'''
class is user define data structure that binds datamemebr and methods into a single unite 
class is blue print or code templet  of the object
using a class we can create multimle object as we want 
Objects : 
    object is an instance of the class 
    obj is collection attributes variables and methods 
    Each Obj Have 2 charatersticks states and behaviour 
    every obj has following property :
        identity
        state
        behaviour
    every obj must be uniqualy identiy
    State:
        it reflects a property of an objects 

__init__()
    a constructer is difine by init method 
    init is reseve methods which is used to insislize the data member of a pyhton class 
    self Variable:
        self represent the object of the class it self 
        self is always passed for in class methods 
        The word self is used to represent the instance of the class 
        by using self keyword we can access the attributes and methods of a python class 
    Class Variables :
        Instance Variable :
            Bound To The Object
            Declare in the __init__()  
            only Owns object can Share not share by all objects
        Class Variable :
            bound to the class 
            Declare In The Class But Out Side Of Any Method 
            Shared By All The Object 


'''

class persion:
    def __init__(self,name,age) -> None:
            self.name = name
            self.age = age 
    def Print_Obj(self):
          return print(f"The Name Is {self.name} And Age Is {self.age}")
        
# a = persion("Nikhil",69)

# a.Print_Obj()

class Calculater :
    def __init__(self,number1,number2) -> None:
            self.number1 = number1
            self.number2 = number2
    def Add(self):
          return self.number1+self.number2
    
    def Sub(self):
          return self.number1-self.number2
    def Mul(self):
          return self.number1 * self.number2

    def Show (self):
          return self.Add() ,self.Mul() , self.Sub()

# obj = Calculater(5,6)

# print(obj.Show())
class Show(Calculater):
    def __init__(self, number1, number2) -> None:
          super().__init__(number1, number2) 
    
    def Divide(self):
          return self.number1 /self.number2
    
obj = Show(15,20)

print(obj.Divide(),obj.Show())





