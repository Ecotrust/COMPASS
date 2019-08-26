# m h  dom mon dow   command
30 09 * * 1 /bin/bash /usr/local/apps/COMPASS/scripts/purge_logs.sh
0 10 * * * /bin/bash /usr/local/apps/COMPASS/scripts/purge_csvs.sh
# 0 10 * * * /bin/bash /usr/local/apps/dev-compass/scripts/purge_csvs.sh
