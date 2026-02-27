products = {
    "T_001": {"category": "Хліб", "name": "Бородинський", "vendor": "Київхліб"},
    "T_200": {"category": "Кондитерські вироби", "name": "Цукерки Метеорит", "vendor": "Рошен"},
    "T_005": {"category": "Молочні продукти", "name": "Молоко 2.5%", "vendor": "Яготинське"},
    "T_002": {"category": "Хліб", "name": "Батон нарізний", "vendor": "Кулиничі"}
}

def execute():
    global products
    
    while True:
        print("\n1 - Пошук за ID\n2 - Пошук за Категорією\n0 - Назад")
        cmd = input("Вибір: ").strip()
        
        if cmd == "1":
            s_id = input("Введіть ID (наприклад T_001): ").strip().upper()
            if s_id in products:
                p = products[s_id]
                print(f"[ЗНАЙДЕНО] Категорія: {p['category']}, Назва: {p['name']}, Постачальник: {p['vendor']}")
            else:
                print(f"[ПОМИЛКА] Продукт з ID '{s_id}' не знайдено.")
                
        elif cmd == "2":
            cat = input("Введіть категорію (наприклад Хліб): ").strip().lower()
            if not cat:
                print("[ПОМИЛКА] Категорія не може бути порожньою.")
                continue
                
            found = False
            print("Результати пошуку:")
            for p in products.values():
                if p['category'].lower() == cat:
                    print(f"- {p['name']} (Пост.: {p['vendor']})")
                    found = True
            if not found:
                print("Товарів такої категорії не знайдено.")
                
        elif cmd == "0":
            break
        else:
            print("Некоректний вибір.")
