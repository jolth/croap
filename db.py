#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""By: Jolth <jolthgs at gmail dot com>
"""
import psycopg2
from contextlib import closing
from psycopg2 import Error
from psycopg2.extras import RealDictCursor


credentials = {'user': 'postgres', 
               'dbname': 'rastree', 
               'host': '127.0.0.1', 
               'port': '5432', 
               'password': 'qwerty'
            }


def connect(ctls):
    """create a connection to postgres and return connection 
    objec.
    
    "ctls" is a credentials dictionary
    {'user': 'user', 
     'dbname': 'database_name', 
     'host': 'localhost', 
     'port': '5432', 
     'password': 'database_password'}
    """
    try:
        conn = psycopg2.connect(**ctls)
        return conn
    except (Exception, Error) as error:
        print('Error while connecting to postgres:', error, sep='\n')


def vehicles_fetchall(ws_name):
    """Lookup all vehicle data for a service.
    ws_name = is the web service name
    """
    select_query = """SELECT ss.name AS soap_server,
    v.placa, v.gps_id, g.imei, g.name AS gps_name,
    lpg.fecha AS fechahora, lpg.velocidad, lpg.odometer, lpg.position, 
    lpg.altura, lpg.grados, lpg.ubicacion,
    te.codigo, te.descrip, vst.motor, 
    v.active AS late_payment, g.active AS drop
    FROM vehicle_soap AS vs
    LEFT JOIN vehiculos AS v ON (v.id=vs.vehicle_id)
    LEFT JOIN gps AS g ON (v.gps_id=g.id)
    LEFT JOIN last_positions_gps AS lpg ON (g.id=lpg.gps_id)
    LEFT JOIN eventos AS e ON (lpg.id=e.positions_gps_id)
    LEFT JOIN type_event AS te ON (e.type=te.codigo)
    LEFT JOIN vehicle_state AS vst ON (v.id=vst.vehicle_id)
    LEFT JOIN soap_server AS ss ON (ss.id=vs.soap_server)
    WHERE g.active='t' AND ss.name = %s"""

    with connect(credentials) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(select_query, (ws_name,))
            return cur.fetchall()
