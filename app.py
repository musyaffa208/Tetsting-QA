import click
from flask import Flask, jsonify
from flask.cli import with_appcontext
from flasgger import Swagger
from api.routes import home_api
from api.utils import create_table
from http import HTTPStatus

@click.command(name='create')
@with_appcontext
def create():
    create_table()
    print('tables is created!')
    return jsonify({'message': 'data created'}), HTTPStatus.OK.value

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Simple Cart API',
    }
    Swagger(app)

    # Initialize Config
    app.config.from_pyfile('config.py')
    app.json_sort_keys = False
    app.register_blueprint(home_api, url_prefix='/api')
    app.cli.add_command(create)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)