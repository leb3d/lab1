text = ""
target = ""
total_words = 0
count = 0
percentage = 0.0

def execute():
    global text, target, total_words, count, percentage
    
    print()
    text = input("Введіть текст: ")
    target = input("Введіть слово для пошуку: ").strip()
    
    if not text or not target:
        print("Помилка: порожній ввід.")
        return

    temp_text = text
    separators = ".,!?;:\"()-"
    for char in separators:
        temp_text = temp_text.replace(char, " ")
        
    words = temp_text.split()
    total_words = len(words)
    
    count = 0
    for w in words:
        if w.lower() == target.lower():
            count = count + 1
            
    if total_words > 0:
        percentage = (count / total_words) * 100
    else:
        percentage = 0.0

    print("\nЗвіт про виконання:")
    print(f"\tШукане слово: \"{target}\"")
    print(f"\tВсього слів: {total_words}")
    print(f"\tЗнайдено: {count}")
    print(f"\tВідсоток: {percentage:.2f}%\n")
