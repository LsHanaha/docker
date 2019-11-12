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


async def get_tracks_for_playlists():
    query = \
    """
        SELECT n.name AS playlist, t.name AS track
        FROM
        (SELECT name, track_id, p.id
            FROM public."Cord" c
            JOIN "Playlist" p
            ON p.id = c.playlist_id) n
        JOIN "Track" t
        ON t.id = n.track_id
        ORDER BY n.id
    """
    async with app.pool.acquire() as connection:
        results = await connection.fetch(query)
        return results

