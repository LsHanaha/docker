from .refactor_db_answers import jsonify
from .get_data_from_db import get_tracks, get_playlists, get_cord
from .random_data import random_name, random_url
from .check_data import check_url, check_name
from . import app
import random


async def fill_tracks():
    tracks = await get_tracks()
    if tracks and len(tracks) > 0:
        return {'posts': "Tracks filled succesfully\n"}

    async with app.pool.acquire() as connection:
        for i in range(0, 100):
            name = random_name()
            url = random_url()
            if check_url(url) and check_name(name):
                await connection.execute("""INSERT INTO "Track"
                    (name, url) VALUES ($1, $2)""", name, url)
            else:
                print(f"Wrong url {url} or name {name}")
    results = await get_tracks()
    if results is not None and len(results) > 0:
        ack = "Tracks filled successfully\n"
    else:
        ack = "There was some problems with tracks\n"
    return {"Tracks": ack}


async def fill_playlists():

    playlists = await get_playlists()
    if playlists and len(playlists) > 0:
        return {'posts': "Playlists filled successfully\n"}

    async with app.pool.acquire() as connection:
        for i in range(0, 20):
            name = random_name()
            if check_name(name):
                await connection.execute("""INSERT INTO "Playlist"
                    (name) VALUES ($1)""", name)
        results = await get_playlists()
        if results is not None and len(results) > 0:
            ack = "Playlists filled successfully\n"
        else:
            ack = "There was some problems with playlists\n"
        return {'Playlists': ack}


async def insert_tracks_in_playlists():
    cord = await get_cord()
    if cord is not None and len(cord) > 0:
        return {"Tracks in playlists": "yep"}
    tracks = await get_tracks()
    tracks = jsonify(tracks)
    tracks_ids = [x['id'] for x in tracks]
    playlists = await get_playlists()
    playlists = jsonify(playlists)
    playlists_ids = [x['id'] for x in playlists]

    async with app.pool.acquire() as connection:
        for playlist_id in playlists_ids:
            music = random.sample(tracks_ids, 5)
            for track_id in music:
                await connection.execute("""INSERT INTO "Cord"
                    (playlist_id, track_id) VALUES ($1, $2)""", playlist_id, track_id)
    return {"Tracks in playlists": "yep"}
