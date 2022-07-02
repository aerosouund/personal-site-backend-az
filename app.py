import json
from flask import Flask, jsonify, request, Response
import azure.cosmos.cosmos_client as cosmos_client
import config


HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']


client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )
db = client.get_database_client(DATABASE_ID)
container = db.get_container_client(CONTAINER_ID)


app = Flask(__name__)

@app.route('/positions')
def get_positions():
    ''' Get all job history from the database '''
    response = jsonify(list(container.query_items(
        query='SELECT * FROM resume_data d WHERE d.type = @type',
        parameters=[
            dict(name='@type', value='position')
        ],
        enable_cross_partition_query=True
    )))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/degrees')
def get_degrees():
    ''' Get all formal education from the database '''
    response = jsonify(list(container.query_items(
        query='SELECT * FROM resume_data d WHERE d.type = @type',
        parameters=[
            dict(name='@type', value='degree')
        ],
        enable_cross_partition_query=True
    )))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/skills')
def get_degrees():
    ''' Get all formal education from the database '''
    response = jsonify(list(container.query_items(
        query='SELECT * FROM resume_data d WHERE d.type = @type',
        parameters=[
            dict(name='@type', value='skill')
        ],
        enable_cross_partition_query=True
    )))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/courses')
def get_degrees():
    ''' Get all formal education from the database '''
    response = jsonify(list(container.query_items(
        query='SELECT * FROM resume_data d WHERE d.type = @type',
        parameters=[
            dict(name='@type', value='course')
        ],
        enable_cross_partition_query=True
    )))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run()
