from hello.lib.base import BaseController
from tg import expose, flash

class RootController(BaseController):
   movie = MovieController()
   @expose()
   def index(self):
      return "<h1>Hello World</h1>"
		
   @expose()
   def _default(self, *args, **kw):
      return "This page is not ready"