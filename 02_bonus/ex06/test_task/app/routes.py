from .init_database import fill_playlists, fill_tracks, insert_tracks_in_playlists


async def init_database():
    tracks = await fill_tracks()
    playlists = await fill_playlists()
    cord = await insert_tracks_in_playlists()
    return tracks, playlists, cord
