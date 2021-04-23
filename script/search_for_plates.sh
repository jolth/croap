#!/usr/bin/env bash
#
# Author: Jorge Toro <jolthgs at gmail dot com>
# Copyright © 2021
#
# script insert all vehicles register in CONTROLT to sopa_controlt table. 
# 
# USAGE:
#   bash load_vehicles.sh file.csv
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
TABLE=""
KEYTOSEARCH=""
DBPASSWORD="m|m"

# searh a them for plate
search_vehicle() {
  local plate=$1
}

main() {
  while read line; do
    #echo $line
    PGPASSWORD=$DBPASSWORD psql -d $DBNAME -w -c "SELECT * FROM $TABLE WHERE $KEYTOSEARCH=lower('$line')"
  done < $1
}

main $1
