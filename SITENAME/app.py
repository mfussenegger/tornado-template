#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tornado.web import Application, StaticFileHandler
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options, parse_command_line
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import scoped_session, sessionmaker
from os.path import dirname, join, isfile

here = dirname(__file__)
project_root = join(here, '..')

try:
    import SITENAME
    assert SITENAME  # silence pyflakes
except ImportError:
    sys.path.append(project_root)

from SITENAME.models import engine
from SITENAME.handlers import IndexHandler, NoDestinationHandler

define('port', default=8080, help='run on the given port', type=int)


class SITENAMEApplication(Application):
    def __init__(self):

        static_path = join(here, 'static')
        template_path = join(here, 'templates')

        handlers = [
            (r'/', IndexHandler),
            (r'/static/(.*)', StaticFileHandler),
            (r'/.*$', NoDestinationHandler)
        ]

        settings = {
            'debug': isfile(join(project_root, 'debug')),
            'static_path': static_path
        }

        super().__init__(handlers, **settings)
        self.env = Environment(loader=FileSystemLoader(template_path))
        self.db = scoped_session(sessionmaker(bind=engine))


def main():
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(SITENAMEApplication())
    http_server.listen(options.port, '0.0.0.0')

    print('Starting Tornado on http://localhost:{}/'.format(options.port))
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
