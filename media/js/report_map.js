var topoLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: 'Sources: <a href="https://www.esri.com">ESRI</a>, HERE, Garmin, ' +
    'Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, ' +
    'Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), &copy; OpenStreetMap contributors, ' +
    'and the GIS User Community',
  id: 'esri.topo'
});
var aerialLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: 'Sources: <a href="https://www.esri.com">ESRI</a>, i-cubed, USDA, USGS, AEX, GeoEye, ' +
    'Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and others',
  id: 'esri.aerial'
});
var labelsLayer = L.tileLayer('https://server.arcgisonline.com/arcgis/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: 'Boundaries: <a href="https://www.esri.com">ESRI</a>, HERE, Garmin, &copy; OpenStreetMap contributors, and the GIS user community',
  id: 'esri.boundaries'
});
var roadsLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: 'Roads: <a href="https://www.esri.com">ESRI</a>, HERE, Garmin, &copy; OpenStreetMap contributors',
  id: 'esri.roads'
});
// var roadsLayer = L.vectorGrid.protobuf('https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/{z}/{y}/{x}.pbf');

roadsLayer.setZIndex(3);
labelsLayer.setZIndex(4);

topoLabel = " Esri Topo";
aerialLabel = " Esri Aerial";
featureLabel = " Report Area";

var baseMaps = {
  "Esri Aerial": aerialLayer,
  "Esri Topo": topoLayer
};

var vectorStyle = {
  "color": 'orange',
  "fillOpacity": 0.3
};

// Get GeoJSON and add layer
var featureLayer = L.geoJSON(
  geojsonFeature,
  {
    style: vectorStyle
  }
);

var overlayMaps = {
  "Report Area": featureLayer,
  // RDH: Adding these to the switcher but toggling with add/removeLayer breaks the click event.
  // "Cities & Boundaries": labelsLayer,
  // "Roads": roadsLayer
};

var map = L.map('topomapid', {
  center: [44, -120.7],
  zoom: 6,
  layers: [aerialLayer, roadsLayer, labelsLayer, featureLayer]
});

layerSwitcher = L.control.layers(baseMaps, overlayMaps);
layerSwitcher.addTo(map);

scaleBar = L.control.scale({
  maxWidth: 250,
  metric: false,
  position: 'bottomright'
});

scaleBar.addTo(map);

// Zoom mapa to geojson feature
map.fitBounds(featureLayer.getBounds());

$('.leaflet-control-layers-selector').click(
  function(evt) {
    if (evt.currentTarget.nextSibling.innerHTML == topoLabel) {
      $('.show-attribution').removeClass('show-attribution');
      $('#topo-attribution').addClass('show-attribution');
      map.removeLayer(labelsLayer);
      map.removeLayer(roadsLayer);
    } else if (evt.currentTarget.nextSibling.innerHTML == aerialLabel) {
      $('.show-attribution').removeClass('show-attribution');
      $('#sat-attribution').addClass('show-attribution');
      map.addLayer(labelsLayer);
      map.addLayer(roadsLayer);
    }
  }
);
