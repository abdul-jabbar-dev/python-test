""" import abc


class person(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def set_gender(self):
        return 0

    @property
    @abc.abstractmethod
    def get_gender(self):
        return self.gender
 """

class teacher:

    def __init__(self, gender) -> None:
        self.gender = gender

    def gender(self, gender):
        self.gender = gender




abdul = teacher('male')
print(abdul)


"""  
def a (self):
    #it have class ->instance object(self), works in object instance not in class """

""" 
@classmethod 
def a (class):
    #it have main class , works in class not object instance"""

""" 
@staticmethod 
def a ():
    #it's nothing normal methods no self,class. it's work like a simple function"""

""" @property
def a(self):
    #this method behavior like a property """
