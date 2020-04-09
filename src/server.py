
from tornado import (ioloop, web)
from json import loads

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        self.write(loads(self.request.body))

def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()