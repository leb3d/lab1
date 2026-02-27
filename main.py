import lab5
import lab6
import lab7

def main():
    while True:
        action = input("lab5 / lab6 / lab7 / exit: ").strip().lower()
        
        if action == "lab5":
            c1 = ["Нетверезий стан водія", "Перевищення швидкості", "Порушення правил обгону", "Порушення пішоходами переходу", "Інші причини"]
            d1 = [2882, 3860, 1853, 372, 10999]
            lab5.analyze_1d(c1, d1)
            
            c2 = ["Порушення правил дорожнього руху водіями", "Несправність транспортних засобів", "Порушення правил дорожнього руху пішоходами", "Поганий стан доріг"]
            d2 = [
                [49120, 285486, 5594, 295369],
                [1205, 6783, 1027, 5393],
                [10779, 68600, 11370, 66874],
                [6817, 39197, 7083, 7844]
            ]
            lab5.analyze_2d(c2, d2)
            
        elif action == "lab6":
            lab6.execute()
            
        elif action == "lab7":
            lab7.execute()
            
        elif action == "exit":
            break
        else:
            print("Некоректний ввід. Доступні: lab5, lab6, lab7, exit.")

if __name__ == "__main__":
    main()
