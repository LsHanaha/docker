from sanic import response
from app import app
from app.routes import init_database


@app.route("/menu", methods=['GET', 'POST'])
async def menu(request):

    return response.json({"hello": "world"})


@app.route("/")
async def test(request):
    return response.redirect('/menu')


@app.route("/init")
async def init(request):
    ack = await init_database()

    return response.text(str(ack))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
