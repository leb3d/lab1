# База даних продуктів (Вкладені словники)
products = {
    "T_001": {"category": "Хліб", "name": "Бородинський", "vendor": "Київхліб"},
    "T_200": {"category": "Кондитерські вироби", "name": "Цукерки Метеорит", "vendor": "Рошен"},
    "T_005": {"category": "Молочні продукти", "name": "Молоко 2.5%", "vendor": "Яготинське"},
    "T_002": {"category": "Хліб", "name": "Батон нарізний", "vendor": "Кулиничі"},
}

print(" База товарів ")
for id_code, p in products.items():
    # Звертаємося за ключами ['category'], ['name'] та ['vendor']
    print(f"ID: {id_code} | Категорія: {p['category']} | Назва: {p['name']} | Постачальник: {p['vendor']}")

# ПОШУК ЗА ID 
print("\n Пошук за ID ")
input_id = input("Введіть ID (наприклад T_001): ").strip().upper()

if input_id in products:
    p = products[input_id]
    print(f"[ЗНАЙДЕНО] Категорія: {p['category']}, Назва: {p['name']}, Постачальник: {p['vendor']}")
else:
    print(f"[ПОМИЛКА] Продукт з ID '{input_id}' не знайдено.")

# ПОШУК ЗА КАТЕГОРІЄЮ
print("\nПошук за категорією")
input_category = input("Введіть категорію (наприклад Хліб): ").strip().lower()

if not input_category:
    print("[ПОМИЛКА] Категорія не може бути порожньою.")
else:
    print("Результати пошуку:")
    found = False
    for p in products.values():
        if p["category"].lower() == input_category:
            print(f" - {p['name']} (Постачальник: {p['vendor']})")
            found = True

    if not found:
        print("Товарів такої категорії не знайдено.")