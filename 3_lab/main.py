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
        return f"Меч {self.name} січе! Шкода: {damage}. У ворога HP: {max(0, enemy.health)}"

    def sharpening(self):
        self._sharp += 5
        return "Ви наточили меч! Бонус до атаки зріс."

class Bow(Item):
    def __init__(self, name, attack_power, range_power):
        super().__init__(name)
        self.__attack_power = attack_power
        self.__range_power = range_power

    def attack(self, enemy):
        damage = self.__attack_power + randint(5, 15) + self.__range_power
        enemy.health -= damage
        return f"Лук {self.name} стріляє! Шкода: {damage}. У ворога HP: {max(0, enemy.health)}"

    def reload(self):
        self.__range_power += 2
        return "Ви прицілилися краще! Дальність (range_power) збільшена."

# 3. ПОЛІМОРФІЗМ У ДІЇ
weapons = [Sword("Ескалібур", 35), Bow("Довгий лук", 30, 10)]
player_weapon = choice(weapons)
enemy_weapon = Sword("Чорний меч", 30)

print(f"--- ГРА ПОЧАЛАСЯ! Твоя зброя: {player_weapon.name} ---")

while player_weapon.health > 0 and enemy_weapon.health > 0:
    print(f"\nТвоє здоров'я: {player_weapon.health}")
    action = input("Вибери дію: 1 - Атака, 2 - Покращення: ")
    
    if action == "1":
        print(player_weapon.attack(enemy_weapon))
    elif action == "2":
        if isinstance(player_weapon, Sword): print(player_weapon.sharpening())
        if isinstance(player_weapon, Bow): print(player_weapon.reload())
    
    if enemy_weapon.health > 0:
        print(f"Ворог атакує! {enemy_weapon.attack(player_weapon)}")

print("\nГра завершена!")
# Додай цей клас до інших
class Axe(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power

    def attack(self, enemy):
        # Сокира має більший розкид випадкової шкоди (randint(0, 20))
        damage = self.__attack_power + randint(0, 20)
        enemy.health -= damage
        return f"Сокира {self.name} розбиває броню! Шкода: {damage}. У ворога HP: {max(0, enemy.health)}"
    
    # Тепер тут три види зброї
weapons = [
    Sword("Ескалібур", 35), 
    Bow("Довгий лук", 30, 10),
    Axe("Громовержець", 40)
]
player_weapon = choice(weapons)