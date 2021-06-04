#!/usr/bin/env bash
#
# Author: Jorge Toro <jolthgs at gmail dot com>
# Copyright © 2021
#
# script insert all vehicles register in CONTROLT to sopa_controlt table. 
# 
# USAGE:
#   bash insert_vehicle_soap.sh file.csv
#
# DESCRIPTION:
# The csv must have all the plates, as well:
#       plate
#       plate
#       plate...
# 
# NOTE: the file must not have a title
#
DBNAME=""
INSERTTABLE="vehicle_soap"
KEYTOSEARCH="placa"
DBPASSWORD="m|m"
SOAPSNAME="controlt"


# searh a them for plate
search_vehicle() {
  local plate=$1

  PGPASSWORD=$DBPASSWORD psql -d $DBNAME -w -c "INSERT INTO $INSERTTABLE (vehicle_id, last_position_gps_id, gps_id, soap_server, last_delivery)
  SELECT v.id, lpg.id, v.gps_id, ss.id, lpg.fecha
  FROM vehiculos AS v
  LEFT JOIN last_positions_gps AS lpg ON (v.gps_id=lpg.gps_id)
  LEFT JOIN soap_server AS ss ON (ss.name='$SOAPSNAME') -- ---> OJO: poner el nombre del service
  WHERE $KEYTOSEARCH=lower('$plate');"
}

main() {
  while read line; do
    echo -n "$line -> "
    search_vehicle $line
  done < $1
}

main $1
