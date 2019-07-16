"""
Object Oriented Programming Structure(OOPS)
>Object
>Class

   1. Encapsulation
   2. Abstraction
   3. Inheritance
   4. Polymorphism

Real World:
    Object : is anything which can see and touch
             Which is Real -> Real Time Entity

    Class : is Drawing of an object
            is representation how an object will look like

What will you think of first ??
OOPS Principle
1. Think of an Object
2. Draw Object
3. Create Real Object by looking Drawing

Computer Science :
    Object : Multi Value Container
             If we wish to customize MVC we will create Objects

    Class : Is textual representation of an Object

Example : Electronics Store
          All LCD's                                 | Homo
          LCD, LED, Washing Machine, Refrigerator...| Hetro

          User is an Object
          User has lot of data associated with it
           Name
           Phone
           Email
           Gender
           Age
           Address
           ..
           ...
        Identification of Object
        Requirement : User should register in my app.
        User should enter source and destination
        location and book a cab.
        User should be allocated a Driver to complete Ride

        Model View Controller Archietecture
        Model-> Object

        Driver : Name, Phone, email, License, Experience...
        Cab    : Brand, Type, Color, RegNum...
        Ride   : Source, Destination, Cab, Driver, User

        Data Associated with object is attributes

"""
class User:
    pass

class Driver:
    pass

data = []
print(type(data))

# 1. Object Construction Statement
u = User()
v = User()

d = Driver()

print(type(u))
print(type(v))
print(type(d))

# 2. Write Data In Object
u.name = "Joban"
u.phone = "+91 99188 75455"
u.email = "joban@example.com"
u.address = "Redwood Shores"

v.name = "Kia"
v.age = 25
v.salary = 30000

# Reference Copy
w = v

print(w)

d.name = "Jack"
d.phone = "+91 99874 56783"
d.experience = 5
d.license = "PBX4150"

# 3. Upadte Operation In Object
u.name = "Joban Malra"
w.age = 27

# 4. Delete Operation In Object
del u.phone
del d.license

# 5. Read Operation In Object
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)