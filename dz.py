# words = "carrot, potato, onion, tomato, carrot, cucumber"

#1
# words = words.replace(" ", "")
# list = words.split(",")
# print(list)

#2
# lowregistr = words.lower()
# print(lowregistr)

#3
# letters = set()
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         letters.add(list[i][j])
# print(len(letters))

# #4
# maxcount = 0
# for i in range(len(list)):
#     if list[i].count("o") > maxcount:
#         maxcount = list[i].count("o")
# max_o = []
# for i in range(len(list)):
#     if list[i].count("o") == maxcount:
#         max_o.append(list[i])
# print(max_o)
  
# #5 и 6
# vegetables_dict = {

# }
# for i in range(len(list)):
#     vowels = list[i].count("i") + list[i].count("o") + list[i].count("a") + list[i].count("e") + list[i].count("u") + list[i].count("y")
#     vegetables_dict.update({list[i]: vowels})

# print(vegetables_dict)
# print(max(vegetables_dict, key = vegetables_dict.get))   

# # 7
# words_nocommo = words.replace(",", "")
# mid_value = len(words_nocommo) / len(list)
# list_max_value = []
# for i in range(len(list)):
#     if len(list[i]) >= mid_value:
#         list_max_value.append(i)
# print(list_max_value)

# # 8
# tuple_list = tuple(list[::-1])
# print(tuple_list)


#дз на 25.09.25

import csv
import os
library = {
    "Война и мир": {
        "author": "Л. Толстой", 
        "year": 1869, 
        "ratings": [5, 4, 5]
    },
    "Преступление и наказание": {
        "author": "Ф. Достоевский", 
        "year": 1866, 
        "ratings": [5, 5, 4]
    }
}

def show_menu():
    print("="*50)
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
    print("="*50)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Книги, выпущенные после определённого года")
    print("7. Книги с рейтингом выше определенного порога")
    print("8. Экспортировать книги в CSV")
    print("9. Импортировать книги из CSV")
    print("0. Выход")


def add_book():
    try:
        title = input("Введите название книги: ").strip()
        if not title:
            print("Ошибка: название книги не может быть пустым!")
            return 
        if title in library:
            print("Книга с таким названием уже существует!")
            return    
        author = input("Введите автора книги: ").strip()
        if not author:
            print("Ошибка: имя автора не может быть пустым!")
            return
        year = int(input("Введите год издания: "))
        if year < 0 or year > 2025:
            print("Ошибка: некорректный год")
            return     
        ratings_input = input("Введите оценки через запятую (макс. 5): ").strip()
        ratings = []
        if ratings_input:
            ratings_list = ratings_input.split(',')
            for rating in ratings_list:
                rating_num = int(rating.strip())
                if rating_num < 1 or rating_num > 5:
                    print("Ошибка: оценка должна быть от 1 до 5!")
                    return
                ratings.append(rating_num)
        
        library[title] = {
            "author": author,
            "year": year,
            "ratings": ratings
        }
        print(f"Книга '{title}' успешно добавлена!")

    except ValueError:
        print("Ошибка: некорректный формат числа!")

def show_all_books():
    if not library:
        print("Библиотека пуста!")
        return
    print("\n" + "-"*80)
    print(f"{'Название':<30} {'Автор':<20} {'Год':<6} {'Рейтинг':<8} {'Кол-во оценок':<12}")
    print("-"*80)
    
    for title, info in library.items():
        author = info["author"]
        year = info["year"]
        ratings = info["ratings"]
        
        if ratings:
            avg_rating = sum(ratings) / len(ratings)
            ratings_count = len(ratings)
        else:
            avg_rating = 0
            ratings_count = 0
        
        print(f"{title:<30} {author:<20} {year:<6} {avg_rating:<8.1f} {ratings_count:<12}")
    print("-"*80)

def find_book_by_title():
    search_title = input("Введите название книги для поиска: ").strip().lower()
    found_books = []
    for title, info in library.items():
        if search_title in title.lower():
            found_books.append((title, info))
    
    if found_books:
        print(f"\nНайдено книг: {len(found_books)}")
        print("-"*60)
        for title, info in found_books:
            ratings = info["ratings"]
            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            print(f"Название: {title}")
            print(f"Автор: {info['author']}")
            print(f"Год: {info['year']}")
            print(f"Рейтинг: {avg_rating:.1f}")
            print(f"Оценки: {ratings}")
            print("-"*60)
    else:
        print("Книги с таким названием не найдены")

def delete_book():
    title = input("Введите название книги для удаления: ").strip()
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена!")
    else:
        print("Книга не найдена")

def add_rating():
    title = input("Введите название книги: ").strip()
    current_title = title
    while current_title not in library:
        print("Книга не найдена!")
        current_title = input("Введите название книги: ").strip()
    else:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if rating < 1 or rating > 5:
                print("Ошибка: оценка должна быть от 1 до 5!")
                return           
            library[current_title]["ratings"].append(rating)
            print(f"Оценка {rating} добавлена книге '{current_title}'")
        except ValueError:
            print("Ошибка: некорректный формат оценки!")

def books_after_year():
    try:
        year_filter = int(input("Введите год: "))        
        filtered_books = []
        for title, info in library.items():
            if info["year"] > year_filter:
                filtered_books.append((title, info))      
        if filtered_books:
            print(f"\nКниги, выпущенные после {year_filter} года:")
            print("-"*50)
            for title, info in sorted(filtered_books, key=lambda x: x[1]["year"]):
                print(f"Название: {title}")
                print(f"Автор: {info['author']}")
                print(f"Год: {info['year']}")
                print("-"*50)
        else:
            print(f"Книг, выпущенных после {year_filter} года, не найдено.")            
    except ValueError:
        print("Ошибка: некорректный формат года!")

def books_above_rating():
    try:
        min_rating = float(input("Введите минимальный рейтинг (0-5): "))
        if min_rating < 0 or min_rating > 5:
            print("Ошибка: рейтинг должен быть от 0 до 5!")
            return        
        filtered_books = []
        for title, info in library.items():
            ratings = info["ratings"]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating >= min_rating:
                    filtered_books.append((title, info, avg_rating))        
        if filtered_books:
            print(f"\nКниги с рейтингом выше {min_rating}:")
            print("-"*60)
            for title, info, rating in sorted(filtered_books, key=lambda x: x[2], reverse=True):
                print(f"Название: {title}")
                print(f"Автор: {info['author']}")
                print(f"Год: {info['year']}")
                print(f"Рейтинг: {rating:.2f}")
                print("-"*60)
        else:
            print(f"Книг с рейтингом выше {min_rating} не найдено.")            
    except ValueError:
        print("Ошибка: некорректный формат рейтинга!")

def export_to_csv():
    filename = input("Введите имя файла для экспорта (например: library.csv): ").strip()
    if not filename.endswith('.csv'):
        filename += '.csv'    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Автор', 'Год', 'Оценки'])            
        for title, info in library.items():
            ratings_str = ','.join(map(str, info['ratings']))
            writer.writerow([title, info['author'], info['year'], ratings_str])       
    print(f"Данные успешно экспортированы в файл {filename}")        


def import_from_csv():
    filename = input("Введите имя файла для импорта: ").strip()  
    if not os.path.exists(filename):
        print("Файл не существует!")
        return  
    try:
        imported_count = 0
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)     
            for row in reader:
                if len(row) == 4:
                    title, author, year, ratings_str = row
                    try:
                        year = int(year)
                        ratings = []
                        if ratings_str:
                            ratings = [int(r) for r in ratings_str.split(',') if r.strip()]
                        valid_ratings = True
                        for rating in ratings:
                            if rating < 1 or rating > 5:
                                valid_ratings = False
                                break                        
                        if valid_ratings:
                            library[title] = {
                                "author": author,
                                "year": year,
                                "ratings": ratings
                            }
                            imported_count += 1
                        else:
                            print(f"Пропущена книга '{title}': некорректные оценки")       
                    except ValueError:
                        print(f"Пропущена книга '{title}': некорректные данные")        
        print(f"Успешно импортировано {imported_count} книг")        
    except FileNotFoundError:
        print("Файл не найден!")
    else:
        print("Импорт завершен успешно!")
    finally:
        print("Операция импорта завершена.")

def main():
    print("Добро пожаловать в систему управления библиотекой!")  
    while True:
        show_menu()     
        try:
            choice = input("Выберите действие (0-9): ").strip()         
            if choice == '0':
                print("Выход из программы!")
                break
            elif choice == '1':
                add_book()
            elif choice == '2':
                show_all_books()
            elif choice == '3':
                find_book_by_title()
            elif choice == '4':
                delete_book()
            elif choice == '5':
                add_rating()
            elif choice == '6':
                books_after_year()
            elif choice == '7':
                books_above_rating()
            elif choice == '8':
                export_to_csv()
            elif choice == '9':
                import_from_csv()
            else:
                print("Неверный выбор!")        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break

main()