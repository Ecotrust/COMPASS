#!/bin/bash
# process_grid.sh
# Input: shapefile (epsg 3857) with planning grids
# Output: postgres sql file

thisdir=`dirname $BASH_SOURCE`

# Variables that change frequently/on every import
# SHP="$thisdir/../docs/Notes/Converted_sample/FieldsHexagonSelection_3857.shp"
if [ -n "$1" ]
  then
    SHP=$1
  else
    echo "Input shapefile is not defined. Using default..."
    SHP="$thisdir/../docs/Notes/mike_processed/FieldsHexagonSelection_3857.shp"
fi

if [ -n "$2" ]
  then
    FINAL=$2
  else
    echo "Final output is not defined. Using default..."
    FINAL="$thisdir/../docs/Notes/Converted_sample/compass_planning_grid_20160620.sql"
fi

if [ -n "$3" ]
  then
    PYTHON_BIN=$3
  else
    echo "Python binary is not defined. Using default..."
    PYTHON_BIN="python"
fi


################################################################################
# Probably no need to touch anything below here
################################################################################

# Path will not change by json file may need to be updated
FIELDMAP="$thisdir/field_map.json"

# Probably won't need to touch these if running from root project dir
TMP="/tmp/compass_planning_grid.sql"
TRANSLATE="$PYTHON_BIN $thisdir/translate.py"
VALIDATE="$PYTHON_BIN $thisdir/validate_fields.py"

# Do some sanity checks on the fieldnames
$VALIDATE $SHP $FIELDMAP
if [ $? -ne 0 ]; then
    echo "NOT VALID"
    exit 1
fi

# export shp to dump format sql
# -d option handles dropping table before creation
# -g option specifies geometry column name
shp2pgsql -d -D -s 3857 -i -I -W LATIN1 \
    -g geometry $SHP public.scenarios_gridcell > $TMP

# Replace gid with id
sed -i 's/gid serial/id serial/' $TMP
sed -E -i 's/PRIMARY KEY \(gid\)/PRIMARY KEY \(id\)/' $TMP

# Change field names to match django model
$TRANSLATE $TMP $FIELDMAP > $FINAL

# Add a centroid geometry column in new transaction
cat << EOT >> $FINAL

BEGIN;
SELECT AddGeometryColumn('public','scenarios_gridcell','centroid','3857','POINT',2);
UPDATE "public"."scenarios_gridcell" SET "centroid" = ST_Centroid("geometry");
CREATE INDEX ON "public"."scenarios_gridcell" USING GIST ("centroid");
COMMIT;
EOT

echo "------"
echo "SUCCESS. sql file created; load into database on VM/Prod server with"
echo "psql -U postgres -d marco -f $FINAL"
echo "------"
