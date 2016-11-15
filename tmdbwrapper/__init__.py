# -*- coding: utf-8 -*-
import os
import requests


BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = os.environ.get('TMDB_API_KEY', None)


class APIKeyMissingError(Exception):
    pass


if not API_KEY:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database"
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = API_KEY

from .tv import TV
