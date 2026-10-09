# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"


# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity)


# bus = Bus("bus", 120, 15)
# print(bus.seating_capacity())


# 5 (2 б). Определите атрибут класса «color» со значением по умолчанию «white». То есть каждое транспортное средство должно быть белым.

# class Vehicle:
#     color='white'
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100


# class Bus(Vehicle):
#     def fare(self):
#         base_fare = super().fare()       
#         return base_fare + base_fare * 0.10   


# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())


# class SuperClass:
#     def __init__(self, num=1):  
#         self.num = num

#     def get_num(self):
#         print(self.num)


# class SubClass(SuperClass):
#     def __init__(self, num=1):
#         super().__init__(num)   
#         print('Экземпляр создан!')


# obj_1 = SubClass()
# print(obj_1.num)

# obj_2 = SubClass(5)
# obj_1.get_num()
# obj_2.get_num() 


import random

class Card:
    # Общие атрибуты класса
    NumsList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    MastList = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, num_index, mast_index):
        self.value = Card.NumsList[num_index]  
        self.suit = Card.MastList[mast_index]  

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.deck = [Card(num, mast) for mast in range(4) for num in range(13)]

    def shuffle(self):
        random.shuffle(self.deck)
        print("Deck shuffled!")

    def draw_card(self, index):
        if index < 1 or index > len(self.deck):
            print(f"Deck has only {len(self.deck)} cards")
        else:
            card = self.deck[index - 1] 
            print(f"Card #{index}: {card}")




deck = DeckOfCards()  
deck.shuffle()        

while True:
    try:
        user_input = int(input("Enter card number to draw (0 to exit): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if user_input == 0:
        print("Exiting...")
        break

    deck.draw_card(user_input)