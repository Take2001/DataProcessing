ogr2ogr \
    -f 'ESRI Shapefile' \
    -t_srs 'EPSG:102024' \
    -where "continent IN ('Africa')" \
    africa-projected.shp \
    ne_50m_admin_0_countries.shp

topojson \
    --width 960 \
    --height 800 \
    --margin 20 \
    --properties admin \
    --properties adm0_a3 \
    --properties geounit \
    -o africa.json \
    -- countries=africa-projected.shp