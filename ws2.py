# ws 2

class Pet():
    def __init__(self, name, animaltype, age):
        self.__Name = name
        self.__Animal = animaltype
        self.__Age = age

    def __str__(self) -> str:
        return "Pet name: {}, Animal type: {}, Age: {}".format(self.__name, self.__animaltype, self.__age)

    def set_name(self, name):
        self.name = name

    def set_animaltype(self, animaltype):
        self.animaltype = animaltype

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.__name

    def get_animaltype(self):
        return self.__animaltype

    def get_name(self):
        return self.__age

def main():
    name = input("Enter your pet's name: ")
    animaltype = input("Enter the type of pet: ")
    age = input("Enter the age of your pet: ")

    pet = Pet(name, animaltype, age)
    print(name,"\n",animaltype,"\n", age)

main()
