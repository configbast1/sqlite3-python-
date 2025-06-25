import sqlite3

db = sqlite3.connect("itstep.db")
c = db.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            title TEXT,
            content TEXT,
            full_text TEXT,
            views INTEGER,
            aytor TEXT
        )
    ''')
    db.commit()

def insert_article():
    title = input("Заголовок: ")
    content = input("Краткое описание: ")
    full_text = input("Полный текст: ")
    views = int(input("Количество просмотров: "))
    aytor = input("Автор: ")
    c.execute("INSERT INTO articles VALUES (?, ?, ?, ?, ?)", (title, content, full_text, views, aytor))
    db.commit()
    print("✅ Статья добавлена.")

def show_articles():
    c.execute("SELECT rowid, title, aytor FROM articles")
    rows = c.fetchall()
    if not rows:
        print("📭 Нет статей.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Название: {row[1]} | Автор: {row[2]}")

def main():
    create_table()
    while True:
        print("\n📚 Меню:")
        print("1. Добавить статью")
        print("2. Показать все статьи")
        print("3. Выход")
        choice = input("Выбор: ")

        if choice == '1':
            insert_article()
        elif choice == '2':
            show_articles()
        elif choice == '3':
            break
        else:
            print("❌ Неверный выбор.")

    db.close()
    print("🔒 Соединение с базой закрыто.")

if __name__ == "__main__":
    main()
