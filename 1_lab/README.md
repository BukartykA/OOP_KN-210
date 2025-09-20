# Вступні заняття: налаштування середовища, Python та Markdown

**Група:** [КН-210]  
**Прізвище, ім'я:** Букартик Андрій  
**Дата:** [20.09.2025]

## Мета
Налаштувати VS Code, створити репозиторій, написати першу програму на Python та звіт у Markdown.

## Файли
- `my_first_app.py` — перша програма (запущено)
- `my_first_app.ipynb` — ноутбук (код + Markdown)
- `chatgpt_suggestion.py` — програма, запропонована ChatGPT
- скріншоти: `screenshots/` (додав)

## Виконання
(1. Встановлено Python 3.13 та необхідні плагіни VS Code: Python, Jupyter, GitHub Copilot.  
2. Створено репозиторій `OOP_KN-210` на GitHub та інтегровано його з VS Code.  
3. Створено папку `1_lab/` для виконання роботи.  
4. Створено файл `my_first_app.py` та написано програму:)

## Вивід програми
(Андрій start programming at 2025-09-20 11:44:01.339684. Lviv is the best city!
)
`![output](screenshots/output1.png)`

## Відповідь від ChatGPT (приклад програми та пояснення)

```python
def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    print("Temperature converter")
    mode = input("Convert (1) C -> F or (2) F -> C? ")
    if mode.strip() == "1":
        c = float(input("Celsius: "))
        print(f"{c}°C = {c_to_f(c):.2f}°F")
    elif mode.strip() == "2":
        f = float(input("Fahrenheit: "))
        print(f"{f}°F = {f_to_c(f):.2f}°C")
    else:
        print("Wrong input")

if __name__ == "__main__":
    main()


## Висновок
(У роботі налаштовано VS Code, створено та запущено першу програму на Python.
Перевірено роботу коду у терміналі, ознайомленося з Markdown для оформлення звіту.
Мета роботи досягнута, нові знання отримано, всі завдання виконані успішно.)
