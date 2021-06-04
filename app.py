#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zeep
from zeep import Client
from clt_client import vehicles_fetchall, factory

username = ''
password = 'm|m'
soap_sname = 'controlt'
wsdl = 'http://controlt.net/APP/HUB/service.asmx?WSDL'


if __name__ == '__main__':
    client = zeep.Client(wsdl=wsdl)

    vehicles = vehicles_fetchall(soap_sname)
    for obj_ctl in factory(vehicles):
        print(obj_ctl.parse())
        v = obj_ctl.parse()
        #v = list(v)
        #c = client.service.InsertEventAndLoginBulk(username, password, v)
        c = client.service.InsertEventAndLogin(username, password, v[0], v[1], 
            v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11],
            v[12], v[13], v[14], v[15], v[16], v[17], v[18], v[19], v[20],
            v[21], v[22], v[23])
        print(c)
