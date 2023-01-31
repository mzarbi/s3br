from flask import Blueprint, g, jsonify, request, send_file
import os

from .file_system import last_updated, access_log, file_columns, add_to_bookmarks, bookmark_groups, \
    bookmark_groups_keys, get_script_list
from .notifications import latest_notifications

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix="/api")


@api_blueprint.before_request
def before_request():
    g.user = "e63551"


@api_blueprint.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@api_blueprint.route('/')
def index():
    return "API"


@api_blueprint.route('/notifications', methods=["POST"])
def notifications():
    """A entry point to get the 5 latest notification for a certain user"""
    data = request.json
    if data.get("page", None):
        page = 30
    return jsonify(latest_notifications(g.user, page)), 202


@api_blueprint.route('/serve-file-structure', methods=["GET"])
def serve_file_structure():
    structure_path = os.path.join(os.environ["CACHE_PATH"], "MANIFEST", 'structure.json')
    return send_file(structure_path, attachment_filename='structure.json')


@api_blueprint.route('/last-updated', methods=["GET"])
def last_updated_():
    return jsonify({"last_updated": last_updated()})


@api_blueprint.route('/file-preview', methods=["POST"])
def file_preview():
    return jsonify({"message": "Preview Not Available"})


@api_blueprint.route('/access-log', methods=["POST"])
def access_log_():
    return jsonify({"access_log": access_log(request.json["key"])})


@api_blueprint.route('/file-columns', methods=["POST"])
def file_columns_():
    return jsonify({"file_columns": file_columns(request.json["key"])})


@api_blueprint.route('/add-to-bookmarks', methods=["POST"])
def add_to_bookmarks_():
    add_to_bookmarks(request.json["key"], g.user, request.json["group"], request.json["label"])
    return jsonify({})


@api_blueprint.route('/bookmark-group')
def bookmark_groups_():
    return jsonify({"bookmarks_list": bookmark_groups(g.user)})


@api_blueprint.route('/bookmark-group-keys', methods=["POST"])
def bookmark_groups_keys_():
    return jsonify({"bookmarks_keys": list(bookmark_groups_keys(g.user, request.json["list"]).values())})


@api_blueprint.route('/script-list')
def get_script_list_():
    return jsonify({"script_list": get_script_list()})

