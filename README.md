# Курсова робота з дисципліни "Бази данних"

# SigmaTasking: Система управління проєктами

## Мета проєкту

Розробка сучасної, масштабованої системи управління проєктами з інтуїтивним RESTful API. Проєкт спрямований на створення потужного інструменту для ефективної організації командної роботи, що поєднує простоту використання з широкими можливостями для розширення та інтеграції.

## Технічний стек

### Серверна частина (Backend)
- **Python 3.x**: Потужна мова програмування з багатою екосистемою для розробки корпоративних додатків
- **FastAPI**: Сучасний високопродуктивний веб-фреймворк для створення API з автоматичною валідацією даних та генерацією документації
- **SQLModel**: Бібліотека для роботи з SQL базами даних, що поєднує переваги SQLAlchemy та Pydantic
- **Pydantic**: Бібліотека для валідації даних та керування налаштуваннями з підтримкою типів Python

### База даних
- **MySQL**: Надійна реляційна база даних з підтримкою транзакцій та складних запитів
- **SQLModel**: Потужний ORM з широкими можливостями для моделювання даних та оптимізації запитів

### Документація та тестування
- **Swagger UI**: Інтерактивна документація API з можливістю тестування endpoints
- **ReDoc**: Альтернативний інтерфейс для перегляду документації API

## Ключові особливості

### Архітектурні рішення
- Модульна архітектура з чітким розділенням відповідальності
- RESTful API з повною підтримкою CRUD операцій
- Асинхронна обробка запитів для високої продуктивності
- Автоматична валідація вхідних даних
- Система міграцій для керування схемою бази даних

### Безпека
- Захищена автентифікація користувачів
- Система ролей та дозволів
- Захист від поширених веб-вразливостей
- Безпечне зберігання паролів з використанням хешування

### Продуктивність
- Connection pooling для оптимізації роботи з базою даних
- Кешування для зменшення навантаження
- Оптимізовані SQL-запити
- Ефективна обробка паралельних запитів

### Масштабованість
- Горизонтальне масштабування сервісів
- Підготовка до контейнеризації
- Можливість легкого розширення функціоналу
- API-first підхід для простої інтеграції

## Перспективи розвитку

- Впровадження WebSocket для real-time комунікації
- Розширення можливостей API
- Додавання системи сповіщень
- Інтеграція з популярними сервісами (GitHub, Gitlab, Bitbucket)
- Розробка мобільного додатку
- Впровадження аналітичних інструментів

## Очікувані результати

- Створення надійної та масштабованої системи управління проєктами
- Забезпечення високої продуктивності та безпеки
- Надання зручного API для інтеграції з іншими системами
- Спрощення процесу управління проєктами для команд різного розміру