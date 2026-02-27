# --- Завдання 2 (2D масив) ---
causes_2d = [
    "Порушення правил дорожнього руху водіями",
    "Несправність транспортних засобів",
    "Порушення правил дорожнього руху пішоходами",
    "Поганий стан доріг"
]
data_2d = [
    [49120, 285486, 5594, 295369],
    [1205, 6783, 1027, 5393],
    [10779, 68600, 11370, 66874],
    [6817, 39197, 7083, 7844]
]

# Ініціалізація (На основі першого елемента)
max_deaths = data_2d[0][0] + data_2d[0][2]
max_deaths_cause = causes_2d[0]

max_injured = data_2d[0][1] + data_2d[0][3]
max_injured_cause = causes_2d[0]

# Обробка 2D списку
for i in range(1, len(causes_2d)):
    current_deaths = data_2d[i][0] + data_2d[i][2]
    current_injured = data_2d[i][1] + data_2d[i][3]
    
    if current_deaths > max_deaths:
        max_deaths = current_deaths
        max_deaths_cause = causes_2d[i]
        
    if current_injured > max_injured:
        max_injured = current_injured
        max_injured_cause = causes_2d[i]

# Виведення результатів Завдання 2
print("\n--- Завдання 2 (2D масив) ---")
print(f"Найбільше загиблих: {max_deaths_cause} ({max_deaths})")
print(f"Найбільше поранених: {max_injured_cause} ({max_injured})\n")