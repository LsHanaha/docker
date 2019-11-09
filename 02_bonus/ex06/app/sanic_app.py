from sanic import response
from asyncpg import create_pool, connect
from sanic import Sanic
from sanic.exceptions import NotFound
import os
import asyncio

app = Sanic(__name__)


def jsonify(records):
    return [dict(r.items()) for r in records]


@app.route("/")
async def test(request):
    return response.json({"hello": "world"})


@app.route("/tracks")
async def handle_request(request):
    return response.json({"Tracks": ["qwe", "asd"]})


@app.route("/playlists")
async def redirected(request):
    return response.json({"playlists": ["asd", "fgh"]})


@app.listener('before_server_start')
async def register_db(app, loop):
    conn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
        user='username', password='password', host='192.168.99.102',
        port=5432, database='Cashwagon'
    )
    app.pool = await create_pool(
        dsn=conn,
        min_size=10, #in bytes,
        max_size=10, #in bytes,
        max_queries=50000,
        max_inactive_connection_lifetime=300,
        loop=loop)
    print('Connection created successfully')
    async with app.pool.acquire() as connection:
        await connection.execute('DROP TABLE IF EXISTS music.sanic_post')
        await connection.execute(connection.execute(
                            """CREATE TABLE music.sanic_post (
                                id serial primary key,
                                content varchar(50),
                                post_date timestamp);
                            """))
        for i in range(0, 1000):
            await connection.execute(f"""INSERT INTO music.sanic_post
                (id, content, post_date) VALUES ({i}, {i}, now())""")


@app.get('/test_db')
async def root_get(request):
    async with app.pool.acquire() as connection:
        results = await connection.fetch('SELECT * FROM music.sanic_post')
        return request.json({'posts': jsonify(results)})


def sanic_error_handlers(status):
    async def custom_error_handler(request, exception):
        return response.json({"success": False, "error": str(exception)}, status=status)
    return custom_error_handler


app.error_handler.add(NotFound, sanic_error_handlers(404))
app.error_handler.add(Exception, sanic_error_handlers(500))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

