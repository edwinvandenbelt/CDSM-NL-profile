#!/usr/bin/env python3

import connexion
import flask
from flask import request

from swagger_server import encoder
from admin.import_controller import ImportController
from admin.clear_controller import ClearController

FUNCTIONS_ROUTES = [ {"url": "admin/import", "func": ImportController().import_all},
                     {"url": "admin/clear", "func": ClearController().clear} 
                    ]

def create_view_func(func):
    def view_func():
        dict_output = func()
        return flask.jsonify(dict_output)
    return view_func

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Dutch profile CDS-M.'}, pythonic_params=True)
    for func in FUNCTIONS_ROUTES:
        app.add_url_rule(rule=f"/{func['url'] }",
                        endpoint=func['func'].__name__,
                        view_func=create_view_func(func['func']),
                        methods=["GET"])
    app.run(port=8080)

if __name__ == '__main__':
    main()
