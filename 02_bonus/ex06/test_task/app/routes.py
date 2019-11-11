from .init_database import fill_playlists, fill_tracks, insert_tracks_in_playlists
from .get_data_from_db import get_tracks, get_playlists, get_cord, get_tracks_for_playlists
from .refactor_db_answers import jsonify


async def tracks_list():
    tracks = await get_tracks()
    print('tracks_list = ', tracks)
    if tracks is None:
        ack = "Список пустой"
    else:
        tracks = jsonify(tracks)
        print(tracks)
        ack = []
        for track in tracks:
            ack.append(' '.join([track['name'], track['url']]))
        ack = '\n'.join(ack)

    return ack


async def playlists_list():
    playlists = await get_playlists()
    if playlists is None:
        ack = "Список пустой"
    else:
        playlists = jsonify(playlists)
        ack = []
        for playlist in playlists:
            ack.append(playlist['name'])
        ack = '\n'.join(ack)

    return ack


async def tracks_in_playlists():
    playlists_tracks = await get_tracks_for_playlists()
    if playlists_tracks is None:
        return "No links tracks-playlists"
    playlists_tracks = jsonify(playlists_tracks)
    ack = {}
    for row in playlists_tracks:
        if row['playlist'] not in ack:
            ack[row['playlist']] = {'tracks': [row['track']]}
        else:
            ack[row['playlist']]['tracks'].append(row['track'])
    print(type(ack))
    dict_keys = ack.keys()
    for val in dict_keys:
        ack[val] = '\n'.join(ack[val]['tracks']) + '\n'
    res = ""
    for val in dict_keys:
        res += val + ":\n" + ack[val] + "\n"
    return res


async def init_database():
    ack = None
    try:
        tracks = await fill_tracks()
    except Exception:
        tracks = None
    try:
        playlists = await fill_playlists()
    except Exception:
        playlists = None
    try:
        cord = await insert_tracks_in_playlists()
    except Exception:
        cord = None
    return tracks, playlists, cord
