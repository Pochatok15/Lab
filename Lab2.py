class Human:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def introduce(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років, я {self.gender}, моя вага {self.weight} кг, а мій зріст {self.height} см.")

person1 = Human("Максим", 23, "чоловік", 180, 75)
person2 = Human("Настя", 32, "жінка", 165, 60)

person1.introduce()
person2.introduce()
