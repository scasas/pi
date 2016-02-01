#!/usr/bin/python
# -*- coding: utf-8 -*-
# si el modulo python-mysql no se encuentra instalado: apt-get install python-mysqldb

import sys
#import random
import time
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(
    host="localhost" # tu host, usualmente es localhost
    , user="root" # tu nombre de usuarios de las base de datos
    , passwd="serdaca" # tu contrasenia de la base de datos
    , db="pi" # nombre de la base de datos
    , cursorclass=MySQLdb.cursors.DictCursor
    )

# you must create a Cursor object. It will let
# you execute all the query you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT id, identificador FROM stock_impresoras")

for row in cur.fetchall() :

    aux = 'IMP-' + str(100+row['id'])
    
    query = "UPDATE stock_impresoras SET identificador = '%s' WHERE id=%i" %(aux, row['id'])
    cur.execute(query)
    # ejecuto un commit
    db.commit()

    print("%i %s " %(row['id'], row['identificador']))