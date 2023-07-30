#!/usr/bin/python3
""" defining routes """
from api.v1.views import app_views
from models import storage
from models.user import User
from flask import jsonify, request, abort


@app_views.route("/users", strict_slashes=False)
def all_users():
    """ List all the user instances """
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)

@app_views.route("/users/<user_id>", strict_slashes=False)
def get_user(user_id):
    """ gets a single user instance from the users table """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    return jsonify(user.to_dict())

@app_views.route(
        '/users/<user_id>', methods=['Delete'], strict_slashes=False
        )
def delete_user(user_id):
    """ deletes a user instance """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@app_views.route(
        '/users', methods=['POST'], strict_slashes=False
        )
def user_post():
    """ Adding user row in the users table """
    # Checking if the request is json formated
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 404

    # since the request is json formated, we parse it to python dict
    user = request.get_json()

    # here we check if the data contains the 'email' and 'password' key
    if 'email' not in user.keys():
        return jsonify({'error': 'Missing Email'}), 404
    if 'password' not in user.keys():
        return jsonify({'error': 'Missing Password'}), 404

    created_user = User(**user)
    storage.new(created_user)
    storage.save()

    return jsonify(created_user.to_dict()), 201

@app_views.route(
        '/users/<user_id>', methods=['PUT'], strict_slashes=False
        )
def user_put(user_id):
    """ Updating user instance """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    new_data = request.get_json()
    if not new_data:
        return jsonify({'error': 'Not a JSON'}), 404

    for key, value in new_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)

    storage.save()
    return jsonify(user.to_dict())
