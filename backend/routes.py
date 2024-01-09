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

    @app.route("/api/update_pdf", methods=["POST"])
    def update_pdf():
        active_results: dict = request.get_json()

        if active_results:
            app_data.update_pdf(active_results)
            return jsonify(message="page updated"), 200
        
        return jsonify(error="page not provided"), 400