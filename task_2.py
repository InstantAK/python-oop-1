import random


class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def buy_food(self, quantity, price):

        if self.money >= price:
            self.food += quantity
            self.money -= price
            print(f"Купили {quantity} единиц еды за {price} денег.")
        else:
            print("Недостаточно денег для покупки еды!")

    def earn_money(self, salary):

        self.money += salary
        print(f"Заработали {salary} денег.")



class Person:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.hunger = 50

    def eat(self):
        if self.house.food >= 10:
            self.hunger += 10
            self.house.food -= 10
            print(f"{self.name} поел. Сытость увеличилась до {self.hunger}, еда уменьшилась до {self.house.food}.")
        else:
            print(f"{self.name} хотел поесть, но в доме недостаточно еды!")

    def work(self):
        self.hunger -= 10
        self.house.earn_money(50)
        print(f"{self.name} поработал. Сытость уменьшилась до {self.hunger}.")

    def shop_for_food(self):
        self.house.buy_food(15, 50)

    def play(self):
        self.hunger -= 5
        print(f"{self.name} поиграл. Сытость уменьшилась до {self.hunger}.")

    def live_day(self):
        random_num = random.randint(1, 6)
        print(f'Сегодняшний кубик для {self.name}: {random_num}')

        if self.hunger < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop_for_food()
        elif self.house.money < 50:
            self.work()
        elif random_num == 1:
            self.work()
        elif random_num == 2:
            self.eat()
        else:
            self.play()

        if self.hunger <= 0:
            print(f'{self.name} умер от голода :(')
            return False

        return True


house1 = House()

person1 = Person('Michel', house1)
person2 = Person('Marina', house1)


day = 1

while day < 365:
    print(f'День {day}.')
    person1.live_day()
    person2.live_day()
    print('\n\n')
    day += 1