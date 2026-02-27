# Введення даних
text = input("Введіть текст:\n")
target = input("Введіть слово для пошуку:\n")

# Видалення зайвих пробілів, якщо користувач ввів " word "
target = target.strip()

# Розширений список роздільників (окрім коми та крапки)
separators = ".,!?;:\"()-"
for char in separators:
    text = text.replace(char, " ")

# Розбиття тексту на слова
words_list = text.split()

total_words = len(words_list)
count = 0

# Використання .lower() для порівняння без урахування регістру
for word in words_list:
    if word.lower() == target.lower():
        count = count + 1

# Виведення результату
print("\nЗвіт про виконання:")
if total_words > 0:
    percentage = (count / total_words) * 100
    print("\tШукане слово:\t\"" + target + "\"")
    print("\tВсього слів:\t", total_words)
    print("\tЗнайдено:\t", count)
    print("\tВідсоток:\t", round(percentage, 2), "%")
else:
    print("\tПомилка: Текст не містить слів.")