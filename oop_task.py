
# class Vehicle(object):
#     def __init__(self, name, mileage, capacity):
        
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity


# class Collage(object):
#     def __init__(self, name, id):

#         self.collage_name = name
#         self.collage_id = id


# class Bus(Vehicle, Collage):
#     def __init__(self, name, mileage, capacity, collage_name, collage_id):
#         Vehicle.__init__(Vehicle, name, mileage, capacity)
#         Collage.__init__(Collage, collage_name, collage_id)


# School_bus = Bus("School Volvo", 12, 45, "mist", 56)
# School_bus2 = Bus("School curser", 18, 40,"pilot",78)
# print(list(Bus.__subclasses__()))

from ast import Constant


print(5//3)