﻿# Тест на проверку, что по треку заказа можно получить данные о заказе в Яндекс Самокате с помощью API.
- Для запуска теста должны быть установлены пакеты pytest и requests.
- Запуск теста выполняется командой pytest.

## Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получение заказа по треку заказа.
4. Проверить, что код ответа равен 200. 
