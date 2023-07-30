#!/usr/bin/python3
""" Registering blue prints """

from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
"""
A blueprint is a way to organize routes and views in a Flask
application. here, the app_views blueprint is registered with
the main app.

The actual definition and implementation of the routes are
present in the api/v1/views directory.
"""

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
"""
cross-origin requests from any origin (origins: "*")
to the endpoints under the path /api/v1/.
"""

@app.teardown_appcontext
def teardown_db(exception):
    """
    define a function that is executed after each request
    is processed.

    function teardown_db closes the database storage after
    each request to avoid resource leaks.
    """
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """If the route requested, does not exist """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    import os

    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5001"))
    app.run(host=host, port=port, threaded=True, debug=True)
