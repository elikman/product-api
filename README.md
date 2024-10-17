# Product API

## Описание

Это REST API для управления продуктами на торговой площадке. API позволяет добавлять, обновлять, удалять и получать информацию о продуктах и категориях.

## Стек технологий

- FastAPI
- SQLAlchemy
- SQLite
- Docker

## Запуск приложения

### Требования

- Docker
- Docker Compose

### Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/elikman/ptoduct_api

2. Запустите приложение с помощью Docker Compose:

    ```bash
    docker-compose up --build

3.  API будет доступен по адресу:
    
    ```bash
    http://localhost:8000
    http://localhost:8000/docs

### Эндпоинты

1. Продукты:
    ## Создать продукт:

        POST /products/
    
    ## Тело запроса:

        ```json
        {
            "name": "Product Name",
            "category_id": 1
        }

2. Получить список продуктов:

    ```GET /products/?skip=0&limit=10```

3. Получить продукт по ID:

    ```GET /products/{id}``

4. Обновить продукт по ID:

    ```PUT /products/{id}```

5. Тело запроса:
    
    ```json
    {
        "name": "Updated Product Name",
        "category_id": 1
    }

6. Удалить продукт по ID:

    ```DELETE /products/{id}```
7. Создать категорию:

    ```POST /categories/```

    Тело запроса:

    ```json
    {
        "name": "Category Name"
    }   
Получить список категорий:
    
    GET /categories/
