# Tutorial link:
# https://medium.com/the-renaissance-developer/learning-python-from-zero-to-hero-8ceed48486d5


# ---- basics ----

# comment 
myFirstVar = "hello world" 
myCondition = 3

# if statement
if myCondition == 1:
    print("if " + myFirstVar) 
elif myCondition == 2:
    print("elif " + myFirstVar)
else:
    print("else " + myFirstVar) 

# while loop
num = 1
print("while loop")
while num <= 10:
    print(num)
    num += 1

# for loop
print("for loop")
for i in range(1, 11):
    print(i)

# array
arr = [1, 2, 3, 4, 5]
arr.append("a")
arr.append("b")
arr.append("c")

# iterate over array
print("\narr:")
for i in arr:
    print(i)

# dictionary key-value data structure
dict_ex = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

print("dictionary by key: " + dict_ex["key2"]);

# iterating over data structures
print("\dictionary:")
for key in dict_ex:
    print("%s --> %s" %(key, dict_ex[key]))

for attribute, value in dict_ex.items():
    print("My %s is %s" %(attribute, value))



# ---- objectoriented ----

print("\n\nobjectoriented:")

class Vehicle:
    def __init__(self, wheelCnt, tankType, capacity, maxVol): 
        self.wheelCnt = wheelCnt
        self.tankType = tankType
        self.capacity = capacity
        self.maxVol = maxVol

    @property
    def wheelCnt(self):
        return seelf.wheelCnt

    @wheelCnt.setter
    def setWheelCnt(self, num):
        self.wheelCnt = num

    def makeNoise(self):
        print('VRUUUMMM')

car = Vehicle(4, 'electric', 5, 250)
print(car) # <__main__.Vehicle instance at xxxxxxx>
print("wheelCnt:")
car.wheelCnt = 2
print(car.wheelCnt)

# make noise
car.makeNoise()

##################################################
# Disclaimer: No private vars / methods possible #
# Convention: use a dash "_" as name prefix      #
##################################################

class Person:
    def __init__(self, first_name, email, age):
        self.first_name = first_name
        self._email = email # private var
        self_age = age

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

    def show_age(self):
        return self._age

# update non-public variables
print("person")
tk = Person('TK', 'tk@mail.com', 25)
print(tk.email())
tk.update_email('new@mail.com')
print(tk.email())

# inheritance: apply parent class to child class as parameter
class ElectricCar(Vehicle):
    def __init__(self, wheelCnt, tankType, capacity, maxVol):
        Vehicle. __init__(self, wheelCnt, tankType, capacity, maxVol)

electricCar = ElectricCar(4, 'electric', 5, 250)
print(electricCar.wheelCnt)
print(electricCar.capacity)
print(electricCar.maxVol)

