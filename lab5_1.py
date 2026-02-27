# --- Завдання 1 (1D масив) ---
causes_1d = ["Нетверезий стан водія", "Перевищення швидкості", "Порушення правил обгону", "Порушення пішоходами переходу", "Інші причини"]
data_1d = [2882, 3860, 1853, 372, 10999]

# Обчислення сумарної кількості ДТП
total_accidents = 0
for count in data_1d:
    total_accidents = total_accidents + count

# Пошук причини з найбільшою кількістю ДТП
max_accidents = data_1d[0]
max_cause_1d = causes_1d[0]
for i in range(1, len(data_1d)):
    if data_1d[i] > max_accidents:
        max_accidents = data_1d[i]
        max_cause_1d = causes_1d[i]

# Обчислення відсотків
percentages = []
for count in data_1d:
    percent = (count / total_accidents) * 100
    percentages.append(percent)

# Виведення результатів Завдання 1
print("\n--- Завдання 1 (1D масив) ---")
print(f"Сумарна кількість ДТП: {total_accidents}")
print(f"Найбільше число ДТП: {max_cause_1d} ({max_accidents})")
print("Відсоток ДТП з кожної причини:")
for i in range(len(causes_1d)):
    print(f"- {causes_1d[i]}: {percentages[i]:.2f}%")
