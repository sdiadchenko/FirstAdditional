import random          #скачала книгу на Project Gutenberg та додала до PyCharm
import string

# 1. Відкрити файл з книгою
with open('pg19033.txt', 'r', encoding='utf-8') as file:    #utf-8 це стандарт для літер для кодування
    book_text = file.read()

# 3. Розділити текст на список токенів (слова та пунктуація)   #тут я перебираю знаки через punctuation, а потім прибераю за допомогою translate
translator = str.maketrans('', '', string.punctuation)     #maketrans відокремлює токен від знаку пунктуації
cleaned_text = book_text.translate(translator)             #punctuation - відокремлює всі знаки пунктцації
token_list = cleaned_text.split()                          #translate - дозволяє щось на щось замінити за таблицею символів ASCI

# 4. Створити словник, де:
# 4.1. Ключі - унікальні токени
# 4.2. Значення - списки слів, що слідують після ключа (одне наступне слово для кожного випадку)
token_dict = {}

# Проходимо по всіх токенах в тексті, крім останнього
for index in range(len(token_list) - 1):                          # -1 щоб не вийти за межі списку
    current_token = token_list[index]  # поточний токен

    next_token = token_list[index + 1]  # наступний токен         # +1 щоб переходити на наступний елемент

    if current_token not in token_dict:
        token_dict[current_token] = []    #якщо поточного слова немає в списку токенів, то ми його додаємо зі значенням у порожній список

    token_dict[current_token].append(next_token)

# 5. Генерація тексту
# 5.1. Програма вибирає перше слово випадково з ключів та друкує його
current_word = random.choice(list(token_dict.keys()))      #random обирає рандомне одне слово зі списку ключів
generated_words = [current_word]

# 5.2. Потім вибирає наступне слово випадково з списку слів після поточного слова
for i in range(199):                                 #199 тому що рахуємо з 0, нам треба 200 разів
    if current_word in token_dict:
        next_word = random.choice(token_dict[current_word])
        generated_words.append(next_word)
        current_word = next_word
    else:
        break                      #якщо слова немає, то зупиняємось, враховуючи, що ми пройшли по всьому токен дікт

# Об'єднуємо згенеровані слова в один текстовий рядок
generated_text = ' '.join(generated_words)

# Виводимо згенерований текст
print(generated_text)