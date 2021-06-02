#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""SOAP ControlT Client
By: Jorge Toro 
    <jorge.toro at devmicrosystems dot com>
    <jolth at gmail dot com>

Copyright May 2021
"""
from db import vehicles_fetchall
import requests


class ControlT:
    def __init__(self, soap_server, placa, gps_id, imei, gps_name, fechahora,
                 velocidad, odometer, position, altura, grados, ubicacion,
                 codigo, descrip, motor, late_payment, drop): 
        self.late_payment = late_payment
        self.plate = placa
        self.serial = gps_name if imei is None else imei
        self.dateeventgps, self.houreventgps = self.__datetime(fechahora)
        self.dateeventavl, self.houreventavl = self.__datetime(fechahora)
        self.status = True # reliable GPS position, yes=1
        self.code_event = '5' if codigo is None else str(codigo)
        self.event_message = 'Reporte Periodico' if descrip is None else descrip
        self.priority = 5 if self.code_event == 1 else 0 
        self.velocity = int(velocidad)
        #self.odometer = float(odometer.replace(',',''))  if odometer is not None else 0
        self.odometer = 0.0
        self.ignition = motor
        self.battery = 50 # 0 - 100
        self.altitude = altura if altura != None else 0.0
        self.course = self.__courses(grados) 
        self.movil = ''
        self.temperature1 = 0
        self.temperature2 = 0
        if late_payment is True:
            self.latitude, self.longitude = self.__latlong(position)
            self.address, self.city, self.department = self.__reverse_geocoding(self.latitude, self.longitude)
        else:
            self.latitude, self.longitude = -2.728822, 1.981992
            self.address, self.city, self.department = ('SERVICIO EN MORA',) * 3



    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (
          self.plate, self.serial, self.dateeventgps, self.houreventgps,
          self.code_event, self.event_message, self.priority, self.velocity, 
          self.odometer, self.longitude, self.latitude, self.ignition,self.battery, 
          self.altitude, self.course, self.address, self.city, self.department)

    def __dir__(self):
        return ['parse']

    def __datetime(self, dt):
        return dt.strftime('%m/%d/%Y'), dt.strftime('%H:%M:%S')

    def __latlong(self, position):
        s = position[1:-1]
        lat, long = s.split(',')
        return (float(lat), float(long))

    def __courses(self, grados):
        if grados is None:
            return str(grados)

        if grados == 0:
            return 'Norte'
        elif grados == 90:
            return 'oriente'
        elif grados == 180:
            return 'sur'
        elif grados == 270:
            return 'occidente'
        elif 360 > grados > 270:
            return 'nor-occidente'
        elif 270 > grados > 180:
            return 'sur-occidente'
        elif 180 > grados > 90:
            return 'sur-oriente'
        elif 90 > grados > 0:
            return 'nor-oriente'

    def __reverse_geocoding(self, lat, lon):
        params = {'format': 'jsonv2', 'lat': lat, 'lon': lon}
        #r = requests.get('http://127.0.0.1:8181/nominatim/reverse.php?')
        r = requests.get('https://nominatim.openstreetmap.org/reverse?', params=params)
        address = r.json()['address']
         
        if 'county' in address: city = address['county']
        elif 'town' in address: city = address['town']
        else: 
            city = address['city']
        state = address.get('state', None)
        stree = address.get('road', None)
        
        return (stree, city, state)

    def parse(self):
        """return analized"""
        return (self.plate, self.serial, self.dateeventgps, self.houreventgps, 
                self.dateeventavl, self.houreventavl, self.status, self.code_event,
                self.event_message, self.priority, self.velocity, self.odometer,
                self.longitude, self.latitude, self.ignition, self.battery,
                self.altitude, self.course, self.movil, self.temperature1,
                self.temperature2, self.address, self.city, self.department)


def factory(vehicles):
    return  map(lambda record: ControlT(**record), vehicles)


if __name__ == '__main__':
    vehicles = vehicles_fetchall('controlt')
    
    for o in factory(vehicles):
        print(o)
        print(list(o.parse()))
