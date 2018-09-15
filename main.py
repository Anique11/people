#! /usr/bin/env python3

from api import Api

api = Api()
team = api.load()


api.save()
