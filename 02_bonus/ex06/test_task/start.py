from sanic import response
from app import app
from app.routes import init_database, tracks_list, playlists_list, tracks_in_playlists
from app.add_to_db import add_track, add_playlist


static_folder = './app/static/templates/'


@app.route("/menu", methods=['GET', 'POST'])
async def menu(request):
    return response.json({"hello": "world"})


@app.route("/tracks", methods=['GET', 'POST'])
async def menu(request):
    tracks = await tracks_list()
    return response.text(tracks)


@app.route("/playlists", methods=['GET', 'POST'])
async def menu(request):
    playlists = await playlists_list()
    return response.text(playlists)


@app.route("/music_in_playlists")
async def music_in_playlists(request):
    music = await tracks_in_playlists()
    return response.text(str(music))


@app.route("/add_track", methods=['GET', 'POST'])
async def track(request):
    income = request.form
    if not income:
        return response.redirect('/')
    ack = await add_track(income)
    return response.text(ack)


@app.route("/add_playlist", methods=['GET', 'POST'])
async def playlist(request):
    income = request.form
    if not income:
        return response.redirect('/')
    ack = await add_playlist(income)
    return response.text(ack)


@app.route("/")
async def test(request):
    return await response.file(static_folder + 'index.html')


@app.route("/init")
async def init(request):
    tracks, playlist, cord = await init_database()
    if tracks and playlist and cord:
        return await response.file(static_folder + 'init.html')
    else:
        tracks = "" if tracks else " Не заполнились треки\n "
        playlist = "" if playlist else " Не заполнились плейлисты\n "
        tracks = "" if tracks else " Не заполнились треки\n "

        return response.text("Произошли ошибки при инициализации базы" + tracks + playlist + cord)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
