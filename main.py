
from tornado.web import Application
from tornado.ioloop import IOLoop
from config import settings
from handlers.instances import Instances


def app_factory():
    urls = [
        ("/instances/?(.*)?", Instances)
    ]
    return Application(urls, debug=True)


if __name__ == '__main__':
   app = app_factory()
   app.listen(settings.port)
   IOLoop.instance().start()
