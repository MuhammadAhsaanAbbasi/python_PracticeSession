class Employee():
    def __init__(self, name: str, age: int, education: str, salary: int) -> None:
        self.name: str = name
        self.age: int = age
        self.education: str = education
        self.salary: int = salary
    def intro(self):
        print(f"Employee name is {self.name} with age {self.age} and education {self.education}")

class Designer(Employee):
    def __init__(self, name: str, age: int, education: str, salary: int) -> None:
        super().__init__(name, age, education, salary)
        self.name: str = name
        self.age: int = age
        self.education: str = education
        self.salary: int = salary
    def job_intro(self,job_title: str):
        print(f"Employee name is {self.name} with age {self.age} and education {self.education} and title {job_title}")

designer1: Designer = Designer("Hijabie", 21, "B.E In Physics", 600000)
designer1.job_intro("Designer")
print(designer1.name)

class Developer(Employee):
    def __init__(self, name: str, age: int, education: str, salary: int) -> None:
        super().__init__(name, age, education, salary)
    def job_intro(self,job_title: str):
        print(f"Employee name is {self.name} with age {self.age} and education {self.education} and title {job_title}")

developer: Developer = Developer("Hijabie", 21, "B.E In Physics", 700000)
developer.job_intro("Generative A.I Developer")
print(f"Developer name is {developer.name}")

class MathOperations():
    counter: int = 0
    org: str = "P.I.A.I.C"
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

res = MathOperations.add(8,9)
print(res)
print(MathOperations.multiply(5,6))
print(MathOperations.org)

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type) -> None:
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name} and Cuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

restaurant: Restaurant = Restaurant("HRK Cuisine", "Pakistani, Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1: Restaurant = Restaurant("HRK Cuisine", "Pakistani, Indian")
restaurant1.describe_restaurant()
restaurant2: Restaurant = Restaurant("Abbasi Cuisine", "Pakistani, Indian, Chinese")
restaurant2.describe_restaurant()
restaurant3: Restaurant = Restaurant("Al Nassar", "Pakistani, Indian, Chinese, Arabian")
restaurant3.describe_restaurant()

from typing import Union, overload

class Student():
    def __init__(self, name: str, age: int, education: str, salary: int) -> None:
        self.name: str = name
        self.age: int = age
        self.education: str = education
        self.salary: int = salary
    @overload
    def calculate(self, a: int, b: int) -> int:
        ...
    @overload
    def calculate(self, a: float, b: float) -> float:
        ...
    @overload
    def calculate(self, a: str, b: str) -> str:
        ...
    def calculate(self, a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, float) and isinstance(b, float):
            return a * b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        else:
            raise TypeError("Invalid type")

student1: Student = Student("Hijabie", 21, "B.E In Physics", 600000)
result1 = student1.calculate(5,6)
result2 = student1.calculate("Hijabie", "Abbasi")
result3 = student1.calculate(5.0,6.0)
print(result1)
print(result2)
print(result3)

class User():
    def __init__(self,first_name: str, last_name: str, age: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.login_attempts: int = 0
    def describe_user(self):
        print(f"First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def incremnet_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1: User = User("HIjabie", "Rabail Khan", 21)
print(user1.login_attempts)
user1.login_attempts = 2
print(user1.login_attempts)
user1.incremnet_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
user1.describe_user()
user1.greet_user()

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: list[str]) -> None:
        super().__init__(first_name, last_name, age)
        self.privileges: list[str] = privileges
    def add_privileges(self, privileges: str):
        self.privileges.append(privileges)
        self.privileges.append(privileges)
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin: Admin = Admin("Hijabie", "Rabail Khan", 21, ["can add post"])
print(admin.privileges)
print(type(admin.privileges))
admin.add_privileges("can delete post")
admin.show_privileges()

class Privileges(Admin):
    def __init__(self, first_name: str, last_name: str, age: int, privileges: list[str]) -> None:
        super().__init__(first_name, last_name, age, privileges)
        self.privileges: list[str] = privileges
    def add_privileges(self, privileges: str):
        self.privileges.append(privileges)

privileage: Privileges = Privileges("Hijabie", "Rabail Khan", 21, ["can add post"])
print(privileage.privileges)
print(type(privileage.privileges))
privileage.add_privileges("can delete post")
privileage.show_privileges()