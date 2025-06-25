CREATE TABLE IF NOT EXISTS articles (
    title TEXT,
    content TEXT,
    full_text TEXT,
    views INTEGER,
    aytor TEXT
);

INSERT INTO articles VALUES
('Пример статьи 1', 'Описание', 'Полный текст 1', 12, 'Автор A'),
('Пример статьи 2', 'Кратко', 'Полный текст 2', 34, 'Автор B');
