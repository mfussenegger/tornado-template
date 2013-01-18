#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler, HTTPError
from jinja2.exceptions import TemplateNotFound


class BaseHandler(RequestHandler):
    @property
    def env(self):
        return self.application.env

    @property
    def db(self):
        return self.application.db

    def get_error_html(self, status_code, **kwargs):
        try:
            self.render('error/{}.html'.format(status_code))
        except (TemplateNotFound, HTTPError):
            try:
                self.render('error/50x.html', status_code=status_code)
            except (TemplateNotFound, HTTPError):
                self.write("You aren't supposed to see this")

    def render(self, template, **kwargs):
        try:
            template = self.env.get_template(template)
        except TemplateNotFound:
            raise HTTPError(404)
        self.env.globals['static_url'] = self.static_url
        self.write(template.render(kwargs))


class NoDestinationHandler(RequestHandler):
    def get(self):
        raise HTTPError(404)


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        return self.redirect('/')
