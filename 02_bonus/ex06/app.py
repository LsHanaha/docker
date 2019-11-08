from sanic import Sanic
from sanic.response import json
import asyncio
import asyncpg
from asyncpg import create_pool
import os


app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})


@app.listener('before_server_start')
async def register_db(app, loop):
    conn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
        user='postgres', password='password', host='localhost',
        port=5433, database='test2'
    )
    app.config['pool'] = await create_pool(
        dsn=conn,
        min_size=10, #in bytes,
        max_size=10, #in bytes,
        max_queries=50000,
        max_inactive_connection_lifetime=300,
        loop=loop)
    print('success')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
