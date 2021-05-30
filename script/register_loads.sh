#!/usr/bin/env bash
#
# Author: Jorge Toro <jolthgs at gmail dot com>
# Copyright © 2021
#
# script to load data to a column of a table sequentially using a csv file.
# 
# USAGE:
#   bash register_loads.sh file.csv
#
# DESCRIPTION:
# The csv must be separated by commas (,) with the following structure:
#       key_to_search,data_to_insert
# 
# NOTE: the file must not have a title
#

DBNAME=""
TABLE="gps"
KEYTOSEARCH="name"
COLUMNTOINSERT="imei"
DBPASSWORD="m|m"

insert_record() {
  items=$1
  
  PGPASSWORD=$DBPASSWORD psql -d $DBNAME -w -c "UPDATE $TABLE SET $COLUMNTOINSERT=${items[1]} WHERE $KEYTOSEARCH='${items[0]}'"
  PGPASSWORD=$DBPASSWORD psql -d $DBNAME -w -c "SELECT * FROM $TABLE WHERE $KEYTOSEARCH='${items[0]}'"
}

items=();

main() {
  while read line; do
    items=($(echo $line|cut -d',' -f1) $(echo $line|cut -d',' -f2))
    
    insert_record $items
  done < $1
}

main $1
