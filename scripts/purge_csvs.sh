#!/bin/bash

# SET ABSOLUTE PATH BELOW TO WORK AS EXPECTED


if [ -e "/usr/local/apps/COMPASS" ]
  then
    rm /usr/local/apps/COMPASS/mediaroot/csvs/*.csv
fi

if [ -e "/usr/local/apps/dev-compass" ]
  then
    rm /usr/local/apps/dev-compass/mediaroot/csvs/*.csv
fi
