from tg import expose, TGController
from tg import MinimalApplicationConfigurator

class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World'

config = MinimalApplicationConfigurator()
config.update_blueprint({
    'root_controller': RootController()
})

application = config.make_wsgi_app()

from wsgiref.simple_server import make_server

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()