#!/bin/bash

# SET ABSOLUTE PATH BELOW TO WORK AS EXPECTED

#rm /usr/local/apps/dev-compass/mediaroot/csvs/*.csv
rm /tmp/tmp_rc.local.log
tail -n 10000 /var/log/rc.local.log > /tmp/tmp_rc.local.log
cp /tmp/tmp_rc.local.log /var/log/rc.local.log
