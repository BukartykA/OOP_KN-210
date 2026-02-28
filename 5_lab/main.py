from abc import ABC, abstractmethod
from random import randint, choice

# 1. АБСТРАКЦІЯ
class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self, enemy):
        pass

# 2. НАСЛІДУВАННЯ ТА ІНКАПСУЛЯЦІЯ
class Sword(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power  # Приватний атрибут
        self._sharp = 0                     # Захищений атрибут

    def attack(self, enemy):
        damage = self.__attack_power + self._sharp + randint(0, 10)
        enemy.health -= damage
        return f"Меч {self.name} завдає {damage} шкоди! У {enemy.name} HP: {max(0, enemy.health)}"

    def sharpening(self):
        self._sharp += 5
        return "Меч наточено! Шкода зросла."

class Axe(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power

    def attack(self, enemy):
        damage = self.__attack_power + randint(0, 20) # Більший розкид шкоди
        enemy.health -= damage
        return f"Сокира {self.name} розбиває броню! Шкода: {damage}. У {enemy.name} HP: {max(0, enemy.health)}"

class Bow(Item):
    def __init__(self, name, attack_power, range_power):
        super().__init__(name)
        self.__attack_power = attack_power
        self.__range_power = range_power

    def attack(self, enemy):
        damage = self.__attack_power + randint(5, 15) + self.__range_power
        enemy.health -= damage
        return f"Лук {self.name} стріляє! Шкода: {damage}. У {enemy.name} HP: {max(0, enemy.health)}"

    def reload(self):
        self.__range_power += 2
        return "Дальність пострілу збільшена!"

# 3. ПОЛІМОРФІЗМ ТА ІГРОВИЙ ЦИКЛ
weapons = [
    Sword("Ескалібур", 35), 
    Bow("Довгий лук", 30, 10),
    Axe("Громовержець", 40)
]

player = choice(weapons)
enemy = Sword("Чорний лицар", 30)

print(f"--- Твоя зброя: {player.name} (HP: {player.health}) ---")

while player.health > 0 and enemy.health > 0:
    action = input("\nТвій хід: 1 - Атака, 2 - Покращити зброю: ")
    
    if action == "1":
        print(player.attack(enemy))
    elif action == "2":
        if isinstance(player, Sword): print(player.sharpening())
        elif isinstance(player, Bow): print(player.reload())
        else: print("Сокиру неможливо покращити в бою!")
    
    if enemy.health > 0:
        print(f"Ворог атакує! {enemy.attack(player)}")

print("\n--- ГРУ ЗАВЕРШЕНО ---")
if player.health > 0: print("ТИ ПЕРЕМІГ!")
else: print("ТЕБЕ ПЕРЕМОЖЕНО.")