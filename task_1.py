class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def feed(self, child):
        if child in self.children:
            if not child.hunger_status:
                print(f'{child.name} был покормлен.')
            else:
                print(f'{child.name} не голодный.')
        else:
            print(f'{child.name} не Ваш ребенок. Попросите его родителей его покормить.')

    def calm(self, child):
        if child in self.children:
            if not child.calm_status:
                print(f'Вы успокоили {child.name}.')
            else:
                print(f'{child.name} и так спокойный, не нужно его еще успокаивать.')
        else:
            print(f'{child.name} не Ваш ребенок. Попросите его родителей его успокоить.')

    def get_children(self):
        if self.children:
            for child in self.children:
                print (f' - {child}')
        else:
            print(f'У Вас нет детей. Стоит задуматься об этом')


    def add_child(self, child):
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name},так как разница в возрасте слишком мала.")

    def info_self(self):
        return f'Меня зовут {self.name} и мне {self.age} лет!'


class Child:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_status = False
        self.hunger_status = True

    def get_status(self):
        calm_status = "Не спокоен" if self.calm_status else "спокоен"
        hungry_status = "Сыт" if self.hunger_status else "голоден"
        print(f'{self.name} - {calm_status} и {hungry_status}')

    def __str__(self):
        """Представление объекта ребёнка в виде строки"""

        return f"Ребёнок {self.name}, {self.age} лет"


parent1 = Parent('Michel', 27)
child1 = Child('Hans', 2)
child2 = Child('Franz', 20)
child3 = Child('Manns', 10)

for child in [child1, child2, child3]:
    parent1.add_child(child)

parent1.info_self()
parent1.get_children()

for child in parent1.children:
    parent1.feed(child)
    parent1.calm(child)
    child.get_status()
