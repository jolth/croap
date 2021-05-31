#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""SOAP ControlT
By: Jorge Toro 
    <jorge.toro at devmicrosystems dot com>
    <jolth at gmail dot com>

Copyright May 2021
"""
#from contextlib import closing
from db import vehicles_fetchall
#from psycopg2.extras import RealDictCursor


class ControlT:
    def __init__(self, soap_server, placa, gps_id, imei, gps_name, fechahora,
                 velocidad, odometer, position, altura, grados, ubicacion,
                 codigo, descrip, motor, late_payment, drop): 
        self.plate = placa

    def __str__(self):
        return '%s' % self.plate

    def __dir__(self):
        return ['parse']

    def parse(self):
        """return analized"""
        return (self.placa,)


#def vehicles_fetchall(ws_name):
#    """Lookup all vehicle data for a service.
#    ws_name = is the web service name
#    """
#    select_query = """SELECT ss.name AS soap_server,
#    v.placa, v.gps_id, g.imei, g.name AS gps_name,
#    lpg.fecha AS fechahora, lpg.velocidad, lpg.odometer, lpg.position, 
#    lpg.altura, lpg.grados, lpg.ubicacion,
#    te.codigo, te.descrip, vst.motor, 
#    v.active AS late_payment, g.active AS drop
#    FROM vehicle_soap AS vs
#    LEFT JOIN vehiculos AS v ON (v.id=vs.vehicle_id)
#    LEFT JOIN gps AS g ON (v.gps_id=g.id)
#    LEFT JOIN last_positions_gps AS lpg ON (g.id=lpg.gps_id)
#    LEFT JOIN eventos AS e ON (lpg.id=e.positions_gps_id)
#    LEFT JOIN type_event AS te ON (e.type=te.codigo)
#    LEFT JOIN vehicle_state AS vst ON (v.id=vst.vehicle_id)
#    LEFT JOIN soap_server AS ss ON (ss.id=vs.soap_server)
#    WHERE ss.name = %s"""

#    with connect(credentials) as conn:
#        with conn.cursor(cursor_factory=RealDictCursor) as cur:
#            cur.execute(select_query, (ws_name,))
#            return cur.fetchall()


if __name__ == '__main__':
    vehicles = vehicles_fetchall('controlt')
    print(vehicles)
    print(vehicles[0])
    
    objs = map(lambda record: ControlT(**record), vehicles)
    for o in objs:
        print(o)
