def analyze_1d(causes, data):
    total_accidents = 0
    for count in data:
        total_accidents = total_accidents + count

    max_accidents = data[0]
    max_cause = causes[0]
    for i in range(1, len(data)):
        if data[i] > max_accidents:
            max_accidents = data[i]
            max_cause = causes[i]

    percentages = []
    if total_accidents > 0:
        for count in data:
            percent = (count / total_accidents) * 100
            percentages.append(percent)

    print("\n--- Завдання 1 (1D масив) ---")
    print(f"Сумарна кількість ДТП: {total_accidents}")
    print(f"Найбільше число ДТП: {max_cause} ({max_accidents})")
    print("Відсоток ДТП з кожної причини:")
    for i in range(len(causes)):
        print(f"- {causes[i]}: {percentages[i]:.2f}%")
    print()

def analyze_2d(causes, data):
    max_deaths = data[0][0] + data[0][2]
    max_deaths_cause = causes[0]

    max_injured = data[0][1] + data[0][3]
    max_injured_cause = causes[0]

    for i in range(1, len(causes)):
        current_deaths = data[i][0] + data[i][2]
        current_injured = data[i][1] + data[i][3]
        
        if current_deaths > max_deaths:
            max_deaths = current_deaths
            max_deaths_cause = causes[i]
            
        if current_injured > max_injured:
            max_injured = current_injured
            max_injured_cause = causes[i]

    print("\n--- Завдання 2 (2D масив) ---")
    print(f"Найбільше загиблих: {max_deaths_cause} ({max_deaths})")
    print(f"Найбільше поранених: {max_injured_cause} ({max_injured})\n")
