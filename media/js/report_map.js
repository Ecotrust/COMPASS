var topoLayer = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
  maxZoom: 18,
  attribution: 'Sources: <a href="https://www.esri.com">ESRI</a>, HERE, Garmin, ' +
    'Intermap, increment P Corp., GEBCO, USGS, FAO, NPS, NRCAN, GeoBase, IGN, Kadaster NL, ' +
    'Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), &copy; OpenStreetMap contributors, ' +
    'and the GIS User Community',
  id: 'esri.topo'
});

var aerialLayer = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
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

labelsLayer.setZIndex(3);
roadsLayer.setZIndex(3);

topoLabel = " Esri Topo";
aerialLabel = " Esri Aerial";
featureLabel = " Report Area";

var baseMaps = {
  "Esri Topo": topoLayer,
  "Esri Aerial": aerialLayer
};

// Get GeoJSON and add layer
// var geojsonFeature = {{ map|safe }};
var topoFeatureLayer = L.geoJSON(geojsonFeature);

var overlayMaps = {
  "Report Area": topoFeatureLayer,
  // "Cities & Boundaries": labelsLayer,
  // "Roads": roadsLayer
};

var map = L.map('topomapid', {
  center: [44, -120.7],
  zoom: 6,
  layers: [topoLayer, topoFeatureLayer]
});

layerSwitcher = L.control.layers(baseMaps, overlayMaps);
layerSwitcher.addTo(map);

// Zoom mapa to geojson feature
map.fitBounds(topoFeatureLayer.getBounds());

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
