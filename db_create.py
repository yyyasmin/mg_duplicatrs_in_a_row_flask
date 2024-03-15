#!flask/bin/python

from flask import Flask, jsonify
import os
import config
from flask import current_app
import os.path

########## usually called in run.py ################
from app import create_app, db

from app.models import  *

app = create_app() 
SQLALCHEMY_DATABASE_URI = app.config.get('SQLALCHEMY_DATABASE_URI')

from sqlalchemy import *
from sqlalchemy.schema import *
from sqlalchemy.engine import reflection


from sqlalchemy.engine import reflection
from sqlalchemy.schema import (
        MetaData,
        Table,
        DropTable,
        ForeignKeyConstraint,
        DropConstraint,
        )
        
print("111111111111111111111")

def db_DropEverything(app, db):
	# From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything
	with app.app_context():
		conn=db.engine.connect()

		# the transaction only applies if the DB supports
		# transactional DDL, i.e. Postgresql, MS SQL Server
		trans = conn.begin()

		inspector = reflection.Inspector.from_engine(db.engine)

		# gather all data first before dropping anything.
		# some DBs lock after things have been dropped in 
		# a transaction.
		metadata = MetaData()

		tbs = []
		all_fks = []

		for table_name in inspector.get_table_names():
			fks = []
			for fk in inspector.get_foreign_keys(table_name):
				if not fk['name']:
					continue
				fks.append(
					ForeignKeyConstraint((),(),name=fk['name'])
					)
			t = Table(table_name,metadata,*fks)
			tbs.append(t)
			all_fks.extend(fks)

		for fkc in all_fks:
			conn.execute(DropConstraint(fkc))

		for table in tbs:
			conn.execute(DropTable(table))
        
		trans.commit()			
		#FROM https://www.mbeckler.org/blog/?p=218	
			
		db.reflect()
		db.drop_all()
		db.create_all()
print("2222222222222222222222222222")

		
		#db.session.commit()  Check if changes are actually made even without this cmd	
		
db_DropEverything(app, db)


	