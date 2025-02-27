import json
class Person:
    def __init__(self, first_name, last_name, street_address, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.email = email
        self.age = age
    def to_dict(self):
        return{
            "first_name": self.first_name,
            "last_name": self.last_name,
            "street_address": self.street_address,
            "email": self.email,
            "age": self.age
        }
data = []

class Student(Person):
    def __init__(self, first_name, last_name, street_address, email, age, student_id):
        super().__init__(first_name, last_name, street_address, email, age)
        self.Student_id = Student_id
    def to_dict(self):
        person_dict = super().to_dict()
        person_dict["Student_id"] = self.Student_id
        return person_dict
def save_to_json(data, filename='json.dump.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
def display_json(filename='json.dump.json'):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=4))
person1 = Person(
    first_name="mike",
    last_name="ross",
    street_address="674 robbin hood suite 200",
    email="mikeross@bobmail.com",
    age="20 february 2000"
)

data.append(person1.to_dict())

Student1 = Student(
    first_name="harvey",
    last_name="spector",
    street_address="674 batman suite 200",
    email="harveyspector@bobmail.com",
    age="27 february 1995",
    Student_id=12345678
)
data.append(Student1.to_dict())
print (data)
save_to_json(data, filename='json.dump.json')

print("JSON File Content:")
display_json(filename='json.dump.json')
