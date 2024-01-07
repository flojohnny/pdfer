from flask import jsonify, request
from backend.pdfly import Pdfly


def configure_routes(app, app_data: Pdfly):
    @app.route("/api/update_query", methods=["POST"])
    def update_query():
        data: dict = request.get_json()
        new_query = data.get("query")

        if new_query:
            matches = app_data.update_query(new_query)
            return jsonify(matches=matches), 200
        
        return jsonify(error="query not provided"), 400
