# -*- coding: utf-8 -*-
from . import session


class TV(object):

    def __init__(self, id):
        self.id = id

    def info(self):
        path = 'https://api.themoviedb.org/3/tv/{}'.format(self.id)
        response = session.get(path)
        return response.json()

    @staticmethod
    def popular():
        path = 'https://api.themoviedb.org/3/tv/popular'
        response = session.get(path)
        return response.json()
