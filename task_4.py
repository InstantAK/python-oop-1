class Animal:

    def __init__(self, name):
        self.name = name


class Bird(Animal):

    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

    def __str__(self):
        return f"{self.name} is a Bird with a wing length of {self.wing_length()}"


class Fish(Animal):

    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def depth_(self):
        if self.depth < 10:
            return "Мелководная рыба"
        elif self.depth > 100:
            return "Глубоководная рыба"
        return "Средневодная рыба"

    def __str__(self):
        return f"{self.name} is a {self.depth_()}"


class Mammal(Animal):

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        return "Обычный"

    def __str__(self):
        return f"{self.name} is a {self.category()} Mammal"


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:

        animal_classes = {
            'Bird': Bird,
            'Fish': Fish,
            'Mammal': Mammal
        }

        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


dog = AnimalFactory.create_animal('Mammal', 'Buddy', 6)
cat = AnimalFactory.create_animal('Mammal', 'Lara', 10)
fish = AnimalFactory.create_animal('Fish', 'Nemo', 50)
print(dog) # Вывод: Dog named Buddy of breed Golden Retriever
print(cat) # Вывод: Cat named Whiskers with color Black
print(fish)

