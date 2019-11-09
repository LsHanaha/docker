from sanic import response
from app.sanic_app import sanic_app
from sanic.exceptions import NotFound
from sanic.exceptions import ServerError

@sanic_app.route('/killme')
async def i_am_ready_to_die(request):
	raise ServerError("Something bad happened", status_code=500)

@sanic_app.exception(NotFound)
async def ignore_404s(request, exception):
	return response.text("Yep, I totally found the page: {}".format(request.url))



