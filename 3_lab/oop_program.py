import re
import os

class MyName:
    """Клас для демонстрації ООП з валідацією та додатковими властивостями."""
    total_names = 0 # Class Variable

    def __init__(self, name=None, domain="itcollege.lviv.ua"):

        # 1. Валідація: Ім'я може містити лише літери.
        if name and not re.match(r'^[a-zA-Zа-яА-ЯёЁїЇєЄіІ\s]+$', str(name)):
            raise ValueError("Ім'я може містити лише літери!")

        # 2. Модифікація: Велика літера та Anonymous.
        if name is None:
            processed_name = self.anonymous_user().name
        else:
            processed_name = str(name).capitalize()

        self._name = processed_name
        self._domain = domain 

        MyName.total_names += 1
        self._id = MyName.total_names

    @property
    def name(self):
        return self._name

    @property
    def my_id(self):
        return self._id

    # 3. Модифікація: Функція, що рахує кількість букв імені.
    @property
    def name_length(self):
        return len(self.name)

    # Email використовує змінний домен
    @property
    def my_email(self):
        return f"{self.name}@{self._domain}"

    # 4. Модифікація: Властивість full_name.
    @property
    def full_name(self):
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    # 5. Модифікація: Можливість змінити текст привітання.
    @staticmethod
    def say_hello(message="Hello to everyone!"):
        return f"You say: {message}"

    # 6. Модифікація: Метод збереження у файл (з виправленням шляху).
    def save_to_file(self, filename="users.txt"):
        # Визначаємо шлях до папки, де знаходиться поточний скрипт (для коректного збереження)
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            script_dir = os.getcwd() 

        file_path = os.path.join(script_dir, filename)
        
        record = self.full_name + os.linesep
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(record)
        return f"Запис збережено у {filename}"

# --- ТЕСТУВАННЯ МОДИФІКОВАНОГО КОДУ ---
print("--- Розпочинаємо тестування модифікованого класу ---")

# Очищаємо файл users.txt перед тестом
if os.path.exists("users.txt"):
    os.remove("users.txt")

names_data = [
    ("bohdan", "kpi.ua"),
    (None, "default.net"),
    ("Ірина", "itcollege.lviv.ua")
]

users = []
for name, domain in names_data:
    try:
        users.append(MyName(name, domain=domain))
    except ValueError as e:
        print(f"Помилка валідації '{name}': {e}")

for user in users:
    print("\n" + "="*30)
    print(f"Об'єкт ID: {user.my_id} | Ім'я: {user.name}")
    print(f"Довжина імені: {user.name_length}")
    print(f"Повний опис: {user.full_name}") 
    print(f"Привітання: {user.say_hello('Привіт усім з Notebook!')}") 
    print(f"Збереження: {user.save_to_file()}")

# Тест на помилку (показуємо, що валідація працює)
try:
    print("\n--- Тест помилки валідації ---")
    MyName("User123!", "bad.com")
except ValueError as e:
    print(f"Успішно спіймана помилка: {e}")