from flask import Flask
from flask_cors import CORS
from backend.routes import configure_routes
from backend.pdfly import Pdfly

def main():
    app = Flask(__name__)
    CORS(app)

    # Create an instance of AppData
    pdfly = Pdfly()

    # Configure routes from the routes module
    configure_routes(app, pdfly)

    app.run(debug=True)


if __name__ == "__main__":
    main()