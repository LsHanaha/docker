from sanic import Sanic
from asyncpg import create_pool
import os


DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'user': os.environ['POSTGRES_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'port': os.environ['POSTGRES_PORT'],
    'database': os.environ['POSTGRES_DATABASE']
}

app = Sanic()


@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=100)
