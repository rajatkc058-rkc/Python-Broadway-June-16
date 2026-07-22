# # #multiple class
# # #multilevel
# # class A():
# #     a = 2
# # class B(A):
# #     a = 3
# # class C(A,B):
# #     c = 10
# # print(C.__mro__)

# # obj = C()
# # print(obj.a())


# #multiple level
# class A():
#     a = 1
#     def__init(self):
#         pass
# class B():
#     a =2
#     def__init__(self):
#         pass 
# class C(A,B):
#     super().__init__()
#     B.__init__()
#     c = 10

#     obj = C()
#     print(obj.a)



class Person():
    name = "Hari"
    age = 30
    phone = 9863402156
    address = "KTM"
class Vehicle():
    vehicle_num = "Ba -02 - Pa - 9963"
    vehicle_model = "Honda"
    vehicle_type = "Bike"
    license_plate = "Bagmati123"
class Driver(Person,Vehicle):
    driver_id = 256314
    rides_completed = 125
    earning_per_ride = 80
    def calc_earnings(self):
        return self.rides_completed * self.earning_per_ride
    def driver_profile(self):
        return f'''
        driver_id : {self.driver_id}
        name : {self.name}
        age : {self.age}
        phone :{self.phone}
        address:{self.address}
        vehicle_num :{self.vehicle_num}
        vehicle_model:{self.vehicle_model}
        vehicle_type :{self.vehicle_type}
        license_plate :{self.license_plate}
        rides_completed :{self.rides_completed}
        earnings :{self.earning_per_ride}
        total_earnings :{self.calc_earnings()}'''

obj = Driver()
print(obj.calc_earnings())
print(obj.driver_profile())
