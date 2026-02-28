# Звіт до лабораторної роботи №5
**Тема:** Основні парадигми ООП у Python.
**Мета роботи:** Навчитися реалізовувати інкапсуляцію, наслідування, поліморфізм та абстракцію.

## Виконання роботи
1. **Абстракція:** Створено базовий клас `Item` з абстрактним методом `attack`.
2. **Наслідування:** Класи `Sword`, `Axe` та `Bow` успадковують властивості `Item`.
3. **Інкапсуляція:** Потужність атаки `__attack_power` прихована всередині класів.
4. **Поліморфізм:** Метод `attack` працює по-різному для кожного виду зброї.

## Код програми
Реалізовано покрокову гру, де гравець обирає дію. Додано нові класи зброї згідно з індивідуальним завданням.
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
## Результат
Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 48. У Чорний лицар HP: 452
Ворог атакує! Меч Чорний лицар завдає 32 шкоди! У Довгий лук HP: 468

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 55. У Чорний лицар HP: 397
Ворог атакує! Меч Чорний лицар завдає 38 шкоди! У Довгий лук HP: 430

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 50. У Чорний лицар HP: 347
Ворог атакує! Меч Чорний лицар завдає 37 шкоди! У Довгий лук HP: 393

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 49. У Чорний лицар HP: 298
Ворог атакує! Меч Чорний лицар завдає 40 шкоди! У Довгий лук HP: 353

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 51. У Чорний лицар HP: 247
Ворог атакує! Меч Чорний лицар завдає 40 шкоди! У Довгий лук HP: 313

Твій хід: 1 - Атака, 2 - Покращити зброю: 11
Ворог атакує! Меч Чорний лицар завдає 36 шкоди! У Довгий лук HP: 277

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 53. У Чорний лицар HP: 194
Ворог атакує! Меч Чорний лицар завдає 39 шкоди! У Довгий лук HP: 238

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 54. У Чорний лицар HP: 140
Ворог атакує! Меч Чорний лицар завдає 36 шкоди! У Довгий лук HP: 202

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 46. У Чорний лицар HP: 94
Ворог атакує! Меч Чорний лицар завдає 33 шкоди! У Довгий лук HP: 169

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 50. У Чорний лицар HP: 44
Ворог атакує! Меч Чорний лицар завдає 40 шкоди! У Довгий лук HP: 129

Твій хід: 1 - Атака, 2 - Покращити зброю: 1
Лук Довгий лук стріляє! Шкода: 49. У Чорний лицар HP: 0

--- ГРУ ЗАВЕРШЕНО ---
ТИ ПЕРЕМІГ!


## Висновок
У ході роботи було опановано практичне застосування парадигм ООП. Мети роботи досягнуто. Формат здачі через GitHub є зручним та професійним.