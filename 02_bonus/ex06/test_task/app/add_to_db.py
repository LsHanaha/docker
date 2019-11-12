from app import app
from .check_data import check_name, check_url
import asyncpg


async def add_track(income):
    name = income.get('name')
    url = income.get('url')
    async with app.pool.acquire() as connection:
        if check_url(url) and check_name(name):
            ack = f"""Write url \"{url}\" and name \"{name}\""""
            try:
                await connection.execute("""INSERT INTO "Track"
                    (name, url) VALUES ($1, $2)""", name, url)
            except asyncpg.exceptions.UniqueViolationError:
                ack = f"Трек \"{name}\" уже есть в базе."
        else:
            ack = f'Wrong url \"{url}\" or name \"{name}\"'
    return ack


async def add_playlist(income):

    name = income.get('name')
    if check_name(name):
        async with app.pool.acquire() as connection:
            try:
                ack = f"""Write playlist name \"{name}\""""
                await connection.execute("""INSERT INTO "Playlist"
                    (name) VALUES ($1)""", name)
            except asyncpg.exceptions.UniqueViolationError:
                ack = f"Плейлист \"{name}\" уже есть в базе."
    else:
        ack = f'Wrong url \"{url}\" or name \"{name}\"'
    return ack
