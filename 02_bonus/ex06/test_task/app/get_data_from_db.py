from . import app
from .refactor_db_answers import jsonify


async def get_tracks():
    async with app.pool.acquire() as connection:
        results = await connection.fetch('''SELECT * FROM "Track"''')
        return results


async def get_playlists():
    async with app.pool.acquire() as connection:
        results = await connection.fetch('''SELECT * FROM "Playlist"''')
        return results


async def get_cord():
    async with app.pool.acquire() as connection:
        results = await connection.fetch('''SELECT * FROM "Cord"''')
        return results


async def get_tracks_in_playlist(playlist_id):
    async with app.pool.acquire() as connection:
        results = await connection.fetch(f'''SELECT track_id FROM "Cord" WHERE playlist_id={playlist_id}''')
        if not (results and len(results)):
            return None
        results = jsonify(results)
        results = [list(x.values())[0] for x in results if x is not None]
        return results
