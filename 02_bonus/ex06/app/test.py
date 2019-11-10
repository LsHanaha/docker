
from asyncpg import connect, create_pool, exceptions

from sanic import Sanic, response
from sanic.response import json
from values_check import check_url, check_name
from values_generator import random_name, random_url
from get_data_from_db import get_tracks, get_playlists, get_tracks_in_playlist
import random
import os

DB_CONFIG = {
    'host': '192.168.99.102',
    'user': 'username',
    'password': 'password',
    'port': '5432',
    'database': 'postgres'
}


def jsonify(records):
    """
    Parse asyncpg record response into JSON format
    """
    return [dict(r.items()) for r in records]


app = Sanic(__name__)



@app.route("/init")
async def init_database():
    tracks = await get_tracks()
    if tracks and len(tracks) > 0:
        return json({'posts': jsonify(tracks)})

    async with app.pool.acquire() as connection:
        for i in range(0, 100):
            name = random_name()
            url = random_url()
            if check_url(url) and check_name(name):
                print(f"Write url {url} and name {name}")
                await connection.execute("""INSERT INTO "Track"
                    (name, url) VALUES ($1, $2)""", name, url)
            else:
                print(f"Wrong url {url} or name {name}")
    results = await get_tracks()
    if results is not None and len(results > 0):
        tracks = "Tracks filled succesfully\n"
    else:
        tracks = "There was some problems\n"


    playlists = await get_playlists()
    if playlists and len(playlists) > 0:
        return json({'posts': jsonify(playlists)})

    async with app.pool.acquire() as connection:
        for i in range(0, 20):
            name = random_name()
            if check_name(name):
                await connection.execute("""INSERT INTO "Playlist"
                    (name) VALUES ($1)""", name)
        results = await get_playlists()
        return json({'posts': jsonify(results)})




@app.listener('before_server_start')
async def register_db(app, loop):
    app.pool = await create_pool(**DB_CONFIG, loop=loop, max_size=100)





@app.route('/', methods=['GET', 'POST'])
async def index(request):
    return response.text("Hello!")


@app.route('/fill_tracks', methods=['GET', 'POST'])
async def fill_tracks(request):

    tracks = await get_tracks()
    if tracks and len(tracks) > 0:
        return json({'posts': jsonify(tracks)})

    async with app.pool.acquire() as connection:
        for i in range(0, 100):
            name = random_name()
            url = random_url()
            if check_url(url) and check_name(name):
                print(f"Write url {url} and name {name}")
                await connection.execute("""INSERT INTO "Track"
                    (name, url) VALUES ($1, $2)""", name, url)
            else:
                print(f"Wrong url {url} or name {name}")
    results = await get_tracks()
    return json({'posts': jsonify(results)})


@app.route('/fill_playlists', methods=['GET', 'POST'])
async def fill_playlists(request):

    playlists = await get_playlists()
    if playlists and len(playlists) > 0:
        return json({'posts': jsonify(playlists)})

    async with app.pool.acquire() as connection:
        for i in range(0, 20):
            name = random_name()
            if check_name(name):
                await connection.execute("""INSERT INTO "Playlist"
                    (name) VALUES ($1)""", name)
        results = await get_playlists()
        return json({'posts': jsonify(results)})


@app.route("/fill_playlist_tracks")
async def fill_playlist_tracks(request):
    tracks = await get_tracks()
    tracks = jsonify(tracks)
    ids = [x['id'] for x in tracks]
    print(ids)
    async with app.pool.acquire() as connection:
        for playlist_id in range(1, 21):
            music = random.sample(ids, 5)
            for track_id in music:
                await connection.execute("""INSERT INTO "Cord"
                    (playlist_id, track_id) VALUES ($1, $2)""", playlist_id, track_id)
    return response.text("good")


@app.route("/insert_track_in_playlist")
async def insert_track_in_playlist(request):
    track_id = 15
    playlist_id = 150
    async with app.pool.acquire() as connection:
        ids = await get_tracks_in_playlist(playlist_id)
        if ids is None or track_id not in ids:
            try:
                await connection.execute("""INSERT INTO "Cord"
                    (playlist_id, track_id) VALUES ($1, $2)""", playlist_id, track_id)
            except exceptions.ForeignKeyViolationError:
                return response.text("This track or playlist does not exists")
        else:
            return response.text("This track is already in playlist")
    return response.text("Track added to playlist")


@app.route("/get_playlists_for_track")
async def get_playlists_for_track(request):
    track_name = "Ixpihgzhqdvazus"
    async with app.pool.acquire() as connection:
        query = f"""
        SELECT name
        FROM "Playlist" p
        JOIN
	        (SELECT playlist_id
	        FROM "Track" t
	        JOIN "Cord" c
	        ON t.id = c.track_id
	        WHERE name='{track_name}') p_id
        ON p.id = p_id.playlist_id
        """
        results = await connection.fetch(query)
        print(results)
        if not results:
            return response.text("Плэйлистов с таким тректом нет.")
        else:
            return json({'Playlists': jsonify(results)})


@app.route("/check_invalid_track_name")
async def check_invalid_track(request):
    async with app.pool.acquire() as connection:
        name = "Srukxmrrqiczgkl"
        url = "http://sukbmrbj.com"
        try:
            res = await connection.execute("""INSERT INTO "Tracks"
                (name, url) VALUES ($1, $2)""", name, url)
            print(res)
            return response.html("<h1>HOW ARE YOU?</h1>")
        except exceptions.UniqueViolationError:
            return response.html(f"<h1>duplicate track name in tracks {name}</h1>")


@app.route("/check_invalid_track_url")
async def check_invalid_track_url(request):
    async with app.pool.acquire() as connection:
        name = "Srukxmrrqiczgklssss"
        url = "http://seotamzp.com"
        try:
            await connection.execute("""INSERT INTO "Tracks"
                (name, url) VALUES ($1, $2)""", name, url)
            return response.html("<h1>HOW ARE YOU?</h1>")
        except exceptions.UniqueViolationError:
            return response.html(f"<h1>duplicate track url in tracks {url}</h1>")


if __name__ == '__main__':
    print(check_url("http://www.example.com"))
    app.run(host='0.0.0.0', port=8080)