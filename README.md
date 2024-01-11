# Asyncopoisk
Это асинхронная обертка для [Kinopoisk API Unofficial](https://kinopoiskapiunofficial.tech/). Создавалась для личного пользования, так как удобной и асинхронной обертки найти не смог. Это был мой первый опыт в написании АПИ обертки, так что PR и Issue приветствуются!

# Особенности
В обертки реализованы все методы, что были описаны в [документации](https://kinopoiskapiunofficial.tech/documentation/api/) на момент *2023.21.12* структура запросов сделана так, чтобы минимально отличаться от [документации](https://kinopoiskapiunofficial.tech/documentation/api/) самой АПИ

# Начало работы
Перед использованием asyncopoisk вам нужно получить токен. Получить его можно на сайте [Kinopoisk API Unofficial](https://kinopoiskapiunofficial.tech/)
Далее создайте экземпляр обертки
```python
from asyncopoisk import KinopoiskAPI
kinopoisk = KinopoiskAPI(token="TOKEN")
```
Теперь с помощью `kinopoisk` вы можете вызывать методы АПИ.

> *ВАЖНО* так как обертка использует асинхронную httpx сессию, вызов всех методов должен происходить асинхронно

# Примеры
**Получить данные о фильме по kinopoisk id**
```python
import asyncio
from asyncopoisk import KinopoiskAPI

async def main(kp_token: str, kp_id: int):
    kinopoisk = KinopoiskAPI(token=kp_token)
    # Получаем фильм по id
    film = await kinopoisk.films.get(kp_id)
```

# Зависимости
- [pydantic 2.3.0](https://github.com/pydantic/pydantic)
- [httpx 0.25.0](https://github.com/encode/httpx)