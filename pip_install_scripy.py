python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

pip install flask

pip install flask_sqlalchemy;
pip install jsonify
pip install psycopg2;
pip install gunicorn;
pip install psycopg2-binary;
pip install requests;
pip install flask_cors;
pip install pprintpp;
pip install flask_migrate;

set FLASK_ENV=development
set FLASK_DEBUG=1
set FLASK_APP=run.py

