#!flask/bin/python

from app import create_app
from app.models import *
import os

app = create_app()
           
if __name__ == "__main__":
    flask_port = os.getenv("PORT", default=8000)
    print("flask_port: ", flask_port)
    app.run(debug=True, port=flask_port)
