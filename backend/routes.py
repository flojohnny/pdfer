from flask import jsonify, request
from backend.pdfly import Pdfly


def configure_routes(app, app_data: Pdfly):

    @app.route("/api/update_index", methods=["GET"])
    def update_index():
        app_data.update_index()
        return jsonify(success=True), 200

    @app.route("/api/update_query", methods=["POST"])
    def update_query():
        data: dict = request.get_json()
        new_query = data.get("query")

        if new_query:
            matches = app_data.update_query(new_query)
            return jsonify(matches=matches), 200

        return jsonify(error="query not provided"), 400

    @app.route("/api/update_pdf", methods=["POST"])
    def update_pdf():
        active_results: dict = request.get_json()

        app_data.update_pdf(active_results)
        return jsonify(success=True), 200
